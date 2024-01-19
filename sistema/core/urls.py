from django.urls import include, path
from .api import *
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('api/OrdenCombustible', OrdenCombustibleViewSet, 'OrdenCombustible')
router.register('api/TipoCombustible', TipoCombustibleViewSet, 'TipoCombustible')
router.register('api/Gasolinera', GasolineraViewSet, 'Gasolinera')
router.register('api/DespachoCombustible', DespachoCombustibleViewSet, 'DespachoCombustible')

urlpatterns = [
    path('', views.home, name='home'),
    path('start/', views.start, name='start'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('paises/', views.paises, name='paises'),
    path('pais/crear', views.crear_pais, name='crear_pais'),
    path('pais/editar/<int:idPais>', views.editar_pais, name='editar_pais'),
    path('pais/borrar/<int:idPais>', views.borrar_pais, name='borrar_pais'),
    path('provincias/', views.provincias, name='provincias'),
    path('provincia/crear', views.crear_provincia, name='crear_provincia'),
    path('provincia/editar/<int:idProvincia>', views.editar_provincia, name='editar_provincia'),
    path('provincia/borrar/<int:idProvincia>', views.borrar_provincia, name='borrar_provincia'),
    path('distritos/', views.distritos, name='distritos'),
    path('distrito/crear', views.crear_distrito, name='crear_distrito'),
    path('distrito/editar/<int:idDistrito>', views.editar_distrito, name='editar_distrito'),
    path('distrito/borrar/<int:idDistrito>', views.borrar_distrito, name='borrar_distrito'),
    path('tipoPeticiones/', views.tipoPeticiones, name='tipoPeticiones'),
    path('tipoPeticion/crear', views.crear_tipoPeticion, name='crear_tipoPeticion'),
    path('tipoPeticion/editar/<int:idTipoPeticion>', views.editar_tipoPeticion, name='editar_tipoPeticion'),
    path('tipoPeticion/borrar/<int:idTipoPeticion>', views.borrar_tipoPeticion, name='borrar_tipoPeticion'),
    path('peticiones/', views.peticiones, name='peticiones'),
    path('peticion/crear', views.crear_peticion, name='crear_peticion'),
    path('circuitos/', views.circuitos, name='circuitos'),
    path('circuito/crear', views.crear_circuito, name='crear_circuito'),
    path('circuito/editar/<int:idCircuito>', views.editar_circuito, name='editar_circuito'),
    path('circuito/borrar/<int:idCircuito>', views.borrar_circuito, name='borrar_circuito'),
    path('subCircuitos/', views.subCircuitos, name='subCircuitos'),
    path('subCircuito/crear', views.crear_subCircuito, name='crear_subCircuito'),
    path('subCircuito/editar/<int:idSubCiruito>', views.editar_subCircuito, name='editar_subCircuito'),
    path('subCircuito/borrar/<int:idSubCiruito>', views.borrar_subCircuito, name='borrar_subCircuito'),
    path('tipoCombustibles/', views.tipoCombustibles, name='tipoCombustibles'),
    path('tipoCombustible/crear', views.crear_tipoCombustible, name='crear_tipoCombustible'),
    path('tipoCombustible/editar/<int:idTipoCombustible>', views.editar_tipoCombustible, name='editar_tipoCombustible'),
    path('tipoCombustible/borrar/<int:idTipoCombustible>', views.borrar_tipoCombustible, name='borrar_tipoCombustible'),
    path('gasolineras/', views.gasolineras, name='gasolineras'),
    path('gasolinera/crear', views.crear_gasolinera, name='crear_gasolinera'),
    path('gasolinera/editar/<int:idGasolinera>', views.editar_gasolinera, name='editar_gasolinera'),
    path('gasolinera/borrar/<int:idGasolinera>', views.borrar_gasolinera, name='borrar_gasolinera'),
    path('ordenCombustibles/', views.ordenCombustibles, name='ordenCombustibles'),
    path('ordenCombustible/crear', views.crear_ordenCombustible, name='crear_ordenCombustible'),
    path('ordenCombustible/editar/<int:idOrdenCombustible>', views.editar_ordenCombustible, name='editar_ordenCombustible'),
    path('ordenCombustible/borrar/<int:idOrdenCombustible>', views.borrar_ordenCombustible, name='borrar_ordenCombustible'),
    path('despachoCombustibles/', views.despachoCombustibles, name='despachoCombustibles'),
    path('despachoCombustible/crear', views.crear_despachoCombustible, name='crear_despachoCombustible'),
    path('despachoCombustible/editar/<int:idDespachoCombustible>', views.editar_despachoCombustible, name='editar_despachoCombustible'),
    path('despachoCombustible/borrar/<int:idDespachoCombustible>', views.borrar_despachoCombustible, name='borrar_despachoCombustible'),
    #Orden de Personal
    path('personales/', views.personales, name='personales'),
    path('personal/crear', views.crear_personal, name='crear_personal'),
    path('personal/editar/<int:idPersonal>', views.editar_personal, name='editar_personal'),
    path('personal/borrar/<int:idPersonal>', views.borrar_personal, name='borrar_personal'),

    #Solicitud de Vehiculo
    path('vehiculos/', views.vehiculos, name='vehiculos'),
    path('vehiculo/crear', views.crear_vehiculo, name='crear_vehiculo'),
    path('vehiculo/editar/<int:idVehiculo>', views.editar_vehiculo, name='editar_vehiculo'),
    path('vehiculo/borrar/<int:idVehiculo>', views.borrar_vehiculo, name='borrar_vehiculo'),

    #Solicitud de Movilizacion
    path('solicitudMovilizaciones/', views.solicitudMovilizaciones, name='solicitudMovilizaciones'),
    path('solicitudMovilizacion/crear', views.crear_solicitudMovilizacion, name='crear_solicitudMovilizacion'),
    path('solicitudMovilizacion/editar/<int:idSolicitudMovilizacion>', views.editar_solicitudMovilizacion, name='editar_solicitudMovilizacion'),
    path('solicitudMovilizacion/borrar/<int:idSolicitudMovilizacion>', views.borrar_solicitudMovilizacion, name='borrar_solicitudMovilizacion'),

    #Orden de Movilizacion
    path('ordenMovilizaciones/', views.ordenMovilizaciones, name='ordenMovilizaciones'),
    path('ordenMovilizacion/crear', views.crear_ordenMovilizacion, name='crear_ordenMovilizacion'),
    path('ordenMovilizacion/editar/<int:idOrdenMovilizacion>', views.editar_ordenMovilizacion, name='editar_ordenMovilizacion'),
    path('ordenMovilizacion/borrar/<int:idOrdenMovilizacion>', views.borrar_ordenMovilizacion, name='borrar_ordenMovilizacion'),


    path('', include(router.urls)),
]