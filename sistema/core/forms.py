from django import forms
from django.urls import reverse_lazy
from .models import *
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
        fields = ['idDistrito', 'numCircuito', 'codigo', 'nombre',]
        widgets = { 'idDistrito': 
            forms.Select(
            attrs={
                "class": "form-control chosen-select",
                "data-placeholder": "Selecciona un Distrito",
                "style": "width: 100%;",
            }
        )}
    
    def __init__(self, *args, **kwargs):
        super(CircuitoForm, self).__init__(*args, **kwargs)
        self.fields['idDistrito'].queryset = Distrito.objects.all().filter(estado = True)

class SubCircuitoForm(forms.ModelForm):
    
    class Meta:
        model = SubCiruito
        fields = ['idCircuito', 'numSubCircuito', 'codigo', 'nombre',]
        widgets = { 'idCircuito': 
            forms.Select(
            attrs={
                "class": "form-control chosen-select",
                "data-placeholder": "Selecciona un Circuito",
                "style": "width: 100%;",
            }
        )}
    
    def __init__(self, *args, **kwargs):
        super(SubCircuitoForm, self).__init__(*args, **kwargs)
        self.fields['idCircuito'].queryset = Circuito.objects.all().filter(estado = True)
        

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

class TipoCombustibleForm(forms.ModelForm):
    class Meta:
        model = TipoCombustible
        fields = ['nombre',]

class GasolineraForm(forms.ModelForm):
    class Meta:
        model = Gasolinera
        fields = ['nombre', 'direccion',]

class OrdenCombustibleForm(forms.ModelForm):
    class Meta:
        model = OrdenCombustible
        fields = ['idGasolinera', 
                'idPersonal',
                'idVehiculo',
                'idTipoCombustible',
                'galones',
                'kilometrajeSalida',
                'horaSalida',
                'horaLlegada',]
        
        widgets = { 'idGasolinera': 
            forms.Select(
            attrs={
                "class": "form-control chosen-select",
                "data-placeholder": "Selecciona un Gasolinera",
                "style": "width: 100%;",
            }
        ),
        'idPersonal': 
            forms.Select(
            attrs={
                "class": "form-control chosen-select",
                "data-placeholder": "Selecciona un Personal",
                "style": "width: 100%;",
            }
        ),
        'idVehiculo': 
            forms.Select(
            attrs={
                "class": "form-control chosen-select",
                "data-placeholder": "Selecciona un Vehiculo",
                "style": "width: 100%;",
            }
        ),
        'idTipoCombustible': 
            forms.Select(
            attrs={
                "class": "form-control chosen-select",
                "placeholder": "Selecciona un Tipo de Combustible",
            }
        ),
        "horaSalida": forms.TimeInput(format='%H:%M',
                                      attrs={'class': 'form-control', 
                                             'type': 'time',}),
        "horaLlegada": forms.TimeInput(format='%H:%M',
                                      attrs={'class': 'form-control', 
                                             'type': 'time',}),
        }

    def __init__(self, *args, **kwargs):
        super(OrdenCombustibleForm, self).__init__(*args, **kwargs)
        self.fields['idGasolinera'].queryset = Gasolinera.objects.all().filter(estado = True)
        self.fields['idPersonal'].queryset = Personal.objects.all().filter(estado = True)
        self.fields['idVehiculo'].queryset = Vehiculo.objects.all().filter(estado = True)
        self.fields['idTipoCombustible'].queryset = TipoCombustible.objects.all().filter(estado = True)
       

class DespachoCombustibleForm(forms.ModelForm):
    
    class Meta:
        model = DespachoCombustible
        fields = ['idOrdenCombustible', 'fechaOrden', 'galones',]
        widgets = { 'idOrdenCombustible': 
            forms.Select(
            attrs={
                "class": "form-control chosen-select",
                "data-placeholder": "Selecciona una orden de combustible",
                "style": "width: 100%;",
            }
        ),
        'fechaOrden': forms.DateInput(format=('%Y-%m-%dT%H:%M'), 
                                          attrs={'class': 'form-control', 'type': 'datetime-local'},
        ), 
        }
    
     
    def __init__(self, *args, **kwargs):
        super(DespachoCombustibleForm, self).__init__(*args, **kwargs)
        self.fields['idOrdenCombustible'].queryset = OrdenCombustible.objects.all().filter(estado = True)


class SolicitudMovilizacionForm(forms.ModelForm):
    class Meta:
        model = SolicitudMovilizacion
        fields = [
                'idPersonal',
                'idVehiculo',
                'fechaSolicitud',
                'fechaSalida',
                'horaSalida',
                'motivo',
                'ruta',
                'kilometraje',
                'numeroOcupantes',
                'datosOcupantes',]
        
        widgets = { 
        'idPersonal': 
            forms.Select(
            attrs={
                "class": "form-control chosen-select",
                "data-placeholder": "Selecciona un Personal",
                "style": "width: 100%;",
            }
        ),
        'idVehiculo': 
            forms.Select(
            attrs={
                "class": "form-control chosen-select",
                "data-placeholder": "Selecciona un Vehiculo",
                "style": "width: 100%;",
            }
        ),
        'fechaSolicitud': forms.DateInput(format=('%Y-%m-%d'), 
                                          attrs={'class': 'form-control', 'type': 'date'},
        ),
        'fechaSalida': forms.DateInput(format=('%Y-%m-%d'), 
                                          attrs={'class': 'form-control', 'type': 'date'},
        ),
        "horaSalida": forms.TimeInput(format='%H:%M',
                                      attrs={'class': 'form-control', 
                                             'type': 'time',}),
        
        }

    def __init__(self, *args, **kwargs):
        super(SolicitudMovilizacionForm, self).__init__(*args, **kwargs)
        self.fields['idPersonal'].queryset = Personal.objects.all().filter(estado = True)
        self.fields['idVehiculo'].queryset = Vehiculo.objects.all().filter(estado = True)


class OrdenMovilizacionForm(forms.ModelForm):
    class Meta:
        model = OrdenMovilizacion
        fields = [
                'idSolicitudMovilizacion',
                'idPersonal',
                'idEstado',
                'fechaSolicitud',]
        
        widgets = { 
        'idPersonal': 
            forms.Select(
            attrs={
                "class": "form-control chosen-select",
                "data-placeholder": "Selecciona un Personal",
                "style": "width: 100%;",
            }
        ),
        'idSolicitudMovilizacion': 
            forms.Select(
            attrs={
                "class": "form-control chosen-select",
                "data-placeholder": "Selecciona un Vehiculo",
                "style": "width: 100%;",
            }
        ),
        'idEstado': 
            forms.Select(
            attrs={
                "class": "form-control chosen-select",
                "data-placeholder": "Selecciona un Estado",
                "style": "width: 100%;",
            }
        ),
        'fechaSolicitud': forms.DateInput(format=('%Y-%m-%d'), 
                                          attrs={'class': 'form-control', 'type': 'date'},
        ),
        }

    def __init__(self, *args, **kwargs):
        super(OrdenMovilizacionForm, self).__init__(*args, **kwargs)
        self.fields['idPersonal'].queryset = Personal.objects.all().filter(estado = True)
        self.fields['idSolicitudMovilizacion'].queryset = SolicitudMovilizacion.objects.all().filter(estado = True)
        self.fields['idEstado'].queryset = Estado.objects.all().filter(estado = True)

class PersonalForm(forms.ModelForm):
    class Meta:
        model = Personal
        fields = [
                'idCanton',
                'idRango',
                'dni',
                'nombre',
                'apellido',
                'tipoSangre',
                'fechaNacimiento',
                'telefonoCelular',
                ]
        
        widgets = { 
        'idCanton': 
            forms.Select(
            attrs={
                "class": "form-control chosen-select",
                "data-placeholder": "Selecciona un Canton",
                "style": "width: 100%;",
            }
        ),
        'idRango': 
            forms.Select(
            attrs={
                "class": "form-control chosen-select",
                "data-placeholder": "Selecciona un Rango",
                "style": "width: 100%;",
            }
        ),
        'fechaNacimiento': forms.DateInput(format=('%Y-%m-%d'), 
                                          attrs={'class': 'form-control', 'type': 'date'},
        ),
        }

    def __init__(self, *args, **kwargs):
        super(PersonalForm, self).__init__(*args, **kwargs)
        self.fields['idCanton'].queryset = Canton.objects.all().filter(estado = True)
        self.fields['idRango'].queryset = Rango.objects.all().filter(estado = True)

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = [
                'idMarca',
                'idTipoVehiculo',
                'placa',
                'chasis',
                'modelo',
                'motor',
                'kilometraje',
                'cilindraje',
                'capacidadCarga',
                'capacidadPasajeros',
                ]
        
        widgets = { 
        'idMarca': 
            forms.Select(
            attrs={
                "class": "form-control chosen-select",
                "data-placeholder": "Selecciona un Marca",
                "style": "width: 100%;",
            }
        ),
        'idTipoVehiculo': 
            forms.Select(
            attrs={
                "class": "form-control chosen-select",
                "data-placeholder": "Selecciona un TipoVehiculo",
                "style": "width: 100%;",
            }
        ),
        }

    def __init__(self, *args, **kwargs):
        super(VehiculoForm, self).__init__(*args, **kwargs)
        self.fields['idMarca'].queryset = Marca.objects.all().filter(estado = True)
        self.fields['idTipoVehiculo'].queryset = TipoVehiculo.objects.all().filter(estado = True)