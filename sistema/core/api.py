from core.models import OrdenCombustible
from rest_framework import viewsets, permissions
from .serializers import *

class TipoCombustibleViewSet(viewsets.ModelViewSet):
  queryset = TipoCombustible.objects.all()
  permission_classes = [permissions.AllowAny]
  serializer_class = TipoCombustibleSerializer

class GasolineraViewSet(viewsets.ModelViewSet):
  queryset = Gasolinera.objects.all()
  permission_classes = [permissions.AllowAny]
  serializer_class = GasolineraSerializer

class OrdenCombustibleViewSet(viewsets.ModelViewSet):
  queryset = OrdenCombustible.objects.all()
  permission_classes = [permissions.AllowAny]
  serializer_class = OrdenCombustibleSerializer

class DespachoCombustibleViewSet(viewsets.ModelViewSet):
  queryset = DespachoCombustible.objects.all()
  permission_classes = [permissions.AllowAny]
  serializer_class = DespachoCombustibleSerializer