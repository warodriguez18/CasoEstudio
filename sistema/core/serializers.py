from rest_framework import serializers
from .models import *

class TipoCombustibleSerializer(serializers.ModelSerializer):
  class Meta:
    model = TipoCombustible
    fields = '__all__'
    read_only_fields = ('created_at',)

class GasolineraSerializer(serializers.ModelSerializer):
  class Meta:
    model = Gasolinera
    fields = '__all__'
    read_only_fields = ('created_at',)

class OrdenCombustibleSerializer(serializers.ModelSerializer):
  class Meta:
    model = OrdenCombustible
    fields = '__all__'
    read_only_fields = ('created_at',)

class DespachoCombustibleSerializer(serializers.ModelSerializer):
  class Meta:
    model = DespachoCombustible
    fields = '__all__'
    read_only_fields = ('created_at',)