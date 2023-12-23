from django import forms
from django.urls import reverse_lazy
from .models import Pais, Provincia, Canton, Distrito, TipoPeticion, Peticion, Circuito, SubCiruito
from smart_selects.form_fields import ChainedModelChoiceField

class PaisForm(forms.ModelForm):
    class Meta:
        model = Pais
        fields = ['nombre']

class ProvinciaForm(forms.ModelForm):
    class Meta:
        model = Provincia
        fields = ['nombre', 'idPais',]

class CantonForm(forms.ModelForm):
    class Meta:
        model = Canton
        fields = ['nombre', 'idProvincia',]

class DistritoForm(forms.ModelForm):
    class Meta:
        model = Distrito
        fields = ['numDistrito', 'codigo', 'nombre',]

class CircuitoForm(forms.ModelForm):
    class Meta:
        model = Circuito
        fields = ['numCircuito', 'codigo', 'nombre',]

class SubCircuitoForm(forms.ModelForm):
    class Meta:
        model = SubCiruito
        fields = ['numSubCircuito', 'codigo', 'nombre',]

class TipoPeticionForm(forms.ModelForm):
    class Meta:
        model = TipoPeticion
        fields = ['nombre',]

class PeticionForm(forms.ModelForm):
    circuito = forms.ModelChoiceField(queryset=Circuito.objects.all(), required=True,
                                      widget=forms.Select(
            attrs={
                "class": "form-control chosen-select",
                "data-placeholder": "Selecciona un SubCircuito",
                "style": "width: 50%;",
            }
        ),)
    subCircuito = ChainedModelChoiceField(
        queryset= SubCiruito.objects.all(),
        chained_field="idCircuito",
        chained_model_field="circuito",
        show_all=False,
        auto_choose=True,
        required=True,
        to_app_name="mi circuito",
        to_model_name="mi circuito",
        foreign_key_app_name="circuito",
        foreign_key_model_name= "circuito",
        foreign_key_field_name="idCircuito",
        widget=forms.Select(
            attrs={
                "class": "form-control chosen-select",
                "data-placeholder": "Selecciona un SubCircuito",
                "data-autocomplete-url": reverse_lazy("autocomplete_subcircuito"),
                "style": "width: 50%;",
            }
        ),
    )
    class Meta:
        model = Peticion
        fields = ['idTipoPeticion', 'circuito', 'subCircuito', 'detalle', 'contacto', 'apellidos', 'nombres',]
        widgets = { 'idTipoPeticion': 
            forms.Select(
            attrs={
                "class": "form-control chosen-select",
                "data-placeholder": "Selecciona una Peticion",
                "style": "width: 50%;",
            }
        )}