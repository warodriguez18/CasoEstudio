from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

"""Session"""
def signup(request):
    if request.method == 'GET':
        return render(request, 'core/signup.html', {"form": UserCreationForm})
    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('paises')
            except IntegrityError:
                return render(request, 'score/signup.html', {"form": UserCreationForm, "error": "Username already exists."})

        return render(request, 'core/signup.html', {"form": UserCreationForm, "error": "Passwords did not match."})

def home(request):
    return render(request, 'core/home.html')

@login_required
def start(request):
    return render(request, 'core/start.html')

@login_required
def signout(request):
    logout(request)
    return redirect('home')


def signin(request):
    if request.method == 'GET':
        return render(request, 'core/signin.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'core/signin.html', 
                          {"form": AuthenticationForm, "error": "Username or password is incorrect."})

        login(request, user)
        return redirect('paises')


"""Core"""
@login_required
def paises(request):
    paises = Pais.objects.filter(estado=True)
    return render(request, 'pais/index.html', {'paises': paises})

@login_required
def crear_pais(request):
    if request.method == 'GET':
        return render(request, 'pais/crear.html', {'formulario': PaisForm})
    else:
        try:
            formulario = PaisForm(request.POST or None)
            if formulario.is_valid():
                new_formulario = formulario.save(commit=False)
                new_formulario.usuario_creacion = request.user.username
                formulario.save()
                return redirect('paises')
            else:
                return render(request, 'pais/crear.html', {'formulario': formulario})
        except ValueError:
            return render(request, 'pais/crear.html', 
                          {'formulario': PaisForm, 'error': 'Se han pasado datos incorrectos. Inténtalo de nuevo.'})

@login_required
def editar_pais(request, idPais):
    pais = get_object_or_404(Pais, pk=idPais)
    if request.method == 'GET':
        formulario = PaisForm(instance=pais)
        return render(request, 'pais/editar.html', {'formulario': formulario})
    else:
        try:
            formulario = PaisForm(request.POST or None, instance=pais)
            if formulario.is_valid():
                new_formulario = formulario.save(commit=False)
                new_formulario.usuario_modificacion = request.user.username
                formulario.save()
                return redirect('paises')
            else:
                return render(request, 'pais/editar.html', {'formulario': formulario})
        except ValueError:
            return render(request, 'pais/editar.html', 
                          {'formulario': PaisForm, 'error': 'Se han pasado datos incorrectos. Inténtalo de nuevo.'})

@login_required
def borrar_pais(request, idPais):
    pais = get_object_or_404(Pais, pk=idPais)
    pais.estado = False
    pais.usuario_modificacion = request.user.username
    pais.save()
    return redirect('paises')

################################################################################################################
@login_required
def provincias(request):
    provincias = Provincia.objects.filter(estado=True)
    return render(request, 'provincia/index.html', {'provincias': provincias})


@login_required
def crear_provincia(request):
    if request.method == 'GET':
        return render(request, 'provincia/crear.html', {'formulario': ProvinciaForm})
    else:
        try:
            formulario = ProvinciaForm(request.POST or None)
            if formulario.is_valid():
                new_formulario = formulario.save(commit=False)
                new_formulario.usuario_creacion = request.user.username
                formulario.save()
                return redirect('provincias')
            else:
                return render(request, 'provincia/crear.html', {'formulario': formulario})
        except ValueError:
            return render(request, 'provincia/crear.html', 
                          {'formulario': ProvinciaForm, 'error': 'Se han pasado datos incorrectos. Inténtalo de nuevo.'})

@login_required
def editar_provincia(request, idProvincia):
    provincia = get_object_or_404(Provincia, pk=idProvincia)
    if request.method == 'GET':
        formulario = ProvinciaForm(instance=provincia)
        return render(request, 'provincia/editar.html', {'formulario': formulario})
    else:
        try:
            formulario = ProvinciaForm(request.POST or None, instance=provincia)
            if formulario.is_valid():
                new_formulario = formulario.save(commit=False)
                new_formulario.usuario_modificacion = request.user.username
                formulario.save()
                return redirect('provincias')
            else:
                return render(request, 'provincia/editar.html', {'formulario': formulario})
        except ValueError:
            return render(request, 'provincia/editar.html', 
                          {'formulario': ProvinciaForm, 'error': 'Se han pasado datos incorrectos. Inténtalo de nuevo.'})

@login_required
def borrar_provincia(request, idProvincia):
    provincia = get_object_or_404(Provincia, pk=idProvincia)
    provincia.estado = False
    provincia.usuario_modificacion = request.user.username
    provincia.save()
    return redirect('provincias')


###############################################################################################################
@login_required
def distritos(request):
    distritos = Distrito.objects.filter(estado=True)
    return render(request, 'distrito/index.html', {'distritos': distritos})

@login_required
def crear_distrito(request):
    if request.method == 'GET':
        return render(request, 'distrito/crear.html', {'formulario': DistritoForm})
    else:
        try:
            formulario = DistritoForm(request.POST or None)
            if formulario.is_valid():
                new_formulario = formulario.save(commit=False)
                new_formulario.usuario_creacion = request.user.username
                formulario.save()
                return redirect('distritos')
            else:
                return render(request, 'distrito/crear.html', {'formulario': formulario})
        except ValueError:
            return render(request, 'distrito/crear.html', 
                          {'formulario': DistritoForm, 'error': 'Se han pasado datos incorrectos. Inténtalo de nuevo.'})

@login_required
def editar_distrito(request, idDistrito):
    distrito = get_object_or_404(Distrito, pk=idDistrito)
    if request.method == 'GET':
        formulario = DistritoForm(instance=distrito)
        return render(request, 'distrito/editar.html', {'formulario': formulario})
    else:
        try:
            formulario = DistritoForm(request.POST or None, instance=distrito)
            if formulario.is_valid():
                new_formulario = formulario.save(commit=False)
                new_formulario.usuario_modificacion = request.user.username
                formulario.save()
                return redirect('distritos')
            else:
                return render(request, 'distrito/editar.html', {'formulario': formulario})
        except ValueError:
            return render(request, 'distrito/editar.html', 
                          {'formulario': DistritoForm, 'error': 'Se han pasado datos incorrectos. Inténtalo de nuevo.'})

@login_required
def borrar_distrito(request, idDistrito):
    print('distito', idDistrito)
    distrito = get_object_or_404(Distrito, pk=idDistrito)
    distrito.estado = False
    distrito.usuario_modificacion = request.user.username
    distrito.save()
    return redirect('distritos')

###############################################################################################################
@login_required
def tipoPeticiones(request):
    tipoPeticiones = TipoPeticion.objects.filter(estado=True)
    return render(request, 'tipoPeticion/index.html', {'tipoPeticiones': tipoPeticiones})

@login_required
def crear_tipoPeticion(request):
    if request.method == 'GET':
        return render(request, 'tipoPeticion/crear.html', {'formulario': TipoPeticionForm})
    else:
        try:
            formulario = TipoPeticionForm(request.POST or None)
            if formulario.is_valid():
                new_formulario = formulario.save(commit=False)
                new_formulario.usuario_creacion = request.user.username
                formulario.save()
                return redirect('tipoPeticiones')
            else:
                return render(request, 'tipoPeticion/crear.html', {'formulario': formulario})
        except ValueError:
            return render(request, 'tipoPeticion/crear.html', 
                          {'formulario': TipoPeticionForm, 'error': 'Se han pasado datos incorrectos. Inténtalo de nuevo.'})

@login_required
def editar_tipoPeticion(request, idTipoPeticion):
    tipoPeticion = get_object_or_404(TipoPeticion, pk=idTipoPeticion)
    if request.method == 'GET':
        formulario = TipoPeticionForm(instance=tipoPeticion)
        return render(request, 'tipoPeticion/editar.html', {'formulario': formulario})
    else:
        try:
            formulario = TipoPeticionForm(request.POST or None, instance=tipoPeticion)
            if formulario.is_valid():
                new_formulario = formulario.save(commit=False)
                new_formulario.usuario_modificacion = request.user.username
                formulario.save()
                return redirect('tipoPeticiones')
            else:
                return render(request, 'tipoPeticion/editar.html', {'formulario': formulario})
        except ValueError:
            return render(request, 'tipoPeticion/editar.html', 
                          {'formulario': TipoPeticionForm, 'error': 'Se han pasado datos incorrectos. Inténtalo de nuevo.'})

@login_required
def borrar_tipoPeticion(request, idTipoPeticion):
    print('distito', idTipoPeticion)
    tipoPeticion = get_object_or_404(TipoPeticion, pk=idTipoPeticion)
    tipoPeticion.estado = False
    tipoPeticion.usuario_modificacion = request.user.username
    tipoPeticion.save()
    return redirect('tipoPeticiones')

###########################################################################################################
@login_required
def peticiones(request):
    peticiones = Peticion.objects.filter(estado=True)
    return render(request, 'peticion/index.html', {'peticiones': peticiones})


def crear_peticion(request):
    if request.method == 'GET':
        return render(request, 'peticion/crear.html', {'formulario': PeticionForm})
    else:
        try:
            formulario = PeticionForm(request.POST or None)
            if formulario.is_valid():
                new_formulario = formulario.save(commit=False)
                new_formulario.usuario_creacion = request.user.username
                formulario.save()
                return redirect('peticiones')
            else:
                return render(request, 'peticion/crear.html', {'formulario': formulario})
        except ValueError:
            return render(request, 'peticion/crear.html', 
                          {'formulario': PeticionForm, 'error': 'Se han pasado datos incorrectos. Inténtalo de nuevo.'})


def autocomplete_subcircuito(request):
    query = request.GET.get("query", "")
    subCiruito_queryset = SubCiruito.objects.filter(idCircuito=query)
    data = {"results": [
        {"id": SubCiruito.idSubCiruito, "text": SubCiruito.nombre} for SubCiruito in subCiruito_queryset
    ]}
    return JsonResponse(data)

#############################################################################################################
@login_required
def circuitos(request):
    circuitos = Circuito.objects.filter(estado=True)
    return render(request, 'circuito/index.html', {'circuitos': circuitos})

@login_required
def crear_circuito(request):
    if request.method == 'GET':
        return render(request, 'circuito/crear.html', {'formulario': CircuitoForm})
    else:
        try:
            formulario = CircuitoForm(request.POST or None)
            if formulario.is_valid():
                new_formulario = formulario.save(commit=False)
                new_formulario.usuario_creacion = request.user.username
                formulario.save()
                return redirect('circuitos')
            else:
                return render(request, 'circuito/crear.html', {'formulario': formulario})
        except ValueError:
            return render(request, 'circuito/crear.html', 
                          {'formulario': CircuitoForm, 'error': 'Se han pasado datos incorrectos. Inténtalo de nuevo.'})

@login_required
def editar_circuito(request, idCircuito):
    circuito = get_object_or_404(Circuito, pk=idCircuito)
    if request.method == 'GET':
        formulario = CircuitoForm(instance=circuito)
        return render(request, 'circuito/editar.html', {'formulario': formulario})
    else:
        try:
            formulario = CircuitoForm(request.POST or None, instance=circuito)
            if formulario.is_valid():
                new_formulario = formulario.save(commit=False)
                new_formulario.usuario_modificacion = request.user.username
                formulario.save()
                return redirect('circuitos')
            else:
                return render(request, 'circuito/editar.html', {'formulario': formulario})
        except ValueError:
            return render(request, 'circuito/editar.html', 
                          {'formulario': CircuitoForm, 'error': 'Se han pasado datos incorrectos. Inténtalo de nuevo.'})

@login_required
def borrar_circuito(request, idCircuito):
    print('circuito', idCircuito)
    circuito = get_object_or_404(Circuito, pk=idCircuito)
    circuito.estado = False
    circuito.usuario_modificacion = request.user.username
    circuito.save()
    return redirect('circuitos')

#################################################################################################################
@login_required
def subCircuitos(request):
    subCircuitos = SubCiruito.objects.filter(estado=True)
    return render(request, 'subCircuito/index.html', {'subCircuitos': subCircuitos})

@login_required
def crear_subCircuito(request):
    if request.method == 'GET':
        return render(request, 'subCircuito/crear.html', {'formulario': SubCircuitoForm})
    else:
        try:
            formulario = SubCircuitoForm(request.POST or None)
            if formulario.is_valid():
                new_formulario = formulario.save(commit=False)
                new_formulario.usuario_creacion = request.user.username
                formulario.save()
                return redirect('subCircuitos')
            else:
                return render(request, 'subCircuito/crear.html', {'formulario': formulario})
        except ValueError:
            return render(request, 'subCircuito/crear.html', 
                          {'formulario': SubCircuitoForm, 'error': 'Se han pasado datos incorrectos. Inténtalo de nuevo.'})

@login_required
def editar_subCircuito(request, idSubCiruito):
    subCircuito = get_object_or_404(SubCiruito, pk=idSubCiruito)
    if request.method == 'GET':
        formulario = SubCiruito(instance=subCircuito)
        return render(request, 'subCircuito/editar.html', {'formulario': formulario})
    else:
        try:
            formulario = SubCircuitoForm(request.POST or None, instance=subCircuito)
            if formulario.is_valid():
                new_formulario = formulario.save(commit=False)
                new_formulario.usuario_modificacion = request.user.username
                formulario.save()
                return redirect('subCircuitos')
            else:
                return render(request, 'subCircuito/editar.html', {'formulario': formulario})
        except ValueError:
            return render(request, 'subCircuito/editar.html', 
                          {'formulario': SubCircuitoForm, 'error': 'Se han pasado datos incorrectos. Inténtalo de nuevo.'})

@login_required
def borrar_subCircuito(request, idSubCiruito):
    subCircuito = get_object_or_404(SubCiruito, pk=idSubCiruito)
    subCircuito.estado = False
    subCircuito.usuario_modificacion = request.user.username
    subCircuito.save()
    return redirect('subCircuitos')

#####################################################################################################################

@login_required
def tipoCombustibles(request):
    tipoCombustibles = TipoCombustible.objects.filter(estado=True)
    return render(request, 'tipoCombustible/index.html', {'tipoCombustibles': tipoCombustibles})

@login_required
def crear_tipoCombustible(request):
    if request.method == 'GET':
        return render(request, 'tipoCombustible/crear.html', {'formulario': TipoCombustibleForm})
    else:
        try:
            formulario = TipoCombustibleForm(request.POST or None)
            if formulario.is_valid():
                new_formulario = formulario.save(commit=False)
                new_formulario.usuario_creacion = request.user.username
                formulario.save()
                return redirect('tipoCombustibles')
            else:
                return render(request, 'tipoCombustible/crear.html', {'formulario': formulario})
        except ValueError:
            return render(request, 'tipoCombustible/crear.html', 
                          {'formulario': TipoCombustibleForm, 'error': 'Se han pasado datos incorrectos. Inténtalo de nuevo.'})

@login_required
def editar_tipoCombustible(request, idTipoCombustible):
    tipoCombustible = get_object_or_404(TipoCombustible, pk=idTipoCombustible)
    if request.method == 'GET':
        formulario = TipoCombustibleForm(instance=tipoCombustible)
        return render(request, 'tipoCombustible/editar.html', {'formulario': formulario})
    else:
        try:
            formulario = TipoCombustibleForm(request.POST or None, instance=tipoCombustible)
            if formulario.is_valid():
                new_formulario = formulario.save(commit=False)
                new_formulario.usuario_modificacion = request.user.username
                formulario.save()
                return redirect('tipoCombustibles')
            else:
                return render(request, 'tipoCombustible/editar.html', {'formulario': formulario})
        except ValueError:
            return render(request, 'tipoCombustible/editar.html', 
                          {'formulario': TipoCombustibleForm, 'error': 'Se han pasado datos incorrectos. Inténtalo de nuevo.'})

@login_required
def borrar_tipoCombustible(request, idTipoCombustible):
    tipoPeticion = get_object_or_404(TipoCombustible, pk=idTipoCombustible)
    tipoPeticion.estado = False
    tipoPeticion.usuario_modificacion = request.user.username
    tipoPeticion.save()
    return redirect('tipoCombustibles')

#####################################################################################################################
@login_required
def gasolineras(request):
    gasolineras = Gasolinera.objects.filter(estado=True)
    return render(request, 'gasolinera/index.html', {'gasolineras': gasolineras})

@login_required
def crear_gasolinera(request):
    if request.method == 'GET':
        return render(request, 'gasolinera/crear.html', {'formulario': GasolineraForm})
    else:
        try:
            formulario = GasolineraForm(request.POST or None)
            if formulario.is_valid():
                new_formulario = formulario.save(commit=False)
                new_formulario.usuario_creacion = request.user.username
                formulario.save()
                return redirect('gasolineras')
            else:
                return render(request, 'gasolinera/crear.html', {'formulario': formulario})
        except ValueError:
            return render(request, 'gasolinera/crear.html', 
                          {'formulario': GasolineraForm, 'error': 'Se han pasado datos incorrectos. Inténtalo de nuevo.'})

@login_required
def editar_gasolinera(request, idGasolinera):
    gasolinera = get_object_or_404(Gasolinera, pk=idGasolinera)
    if request.method == 'GET':
        formulario = GasolineraForm(instance=gasolinera)
        return render(request, 'gasolinera/editar.html', {'formulario': formulario})
    else:
        try:
            formulario = GasolineraForm(request.POST or None, instance=gasolinera)
            if formulario.is_valid():
                new_formulario = formulario.save(commit=False)
                new_formulario.usuario_modificacion = request.user.username
                formulario.save()
                return redirect('gasolineras')
            else:
                return render(request, 'gasolinera/editar.html', {'formulario': formulario})
        except ValueError:
            return render(request, 'gasolinera/editar.html', 
                          {'formulario': GasolineraForm, 'error': 'Se han pasado datos incorrectos. Inténtalo de nuevo.'})

@login_required
def borrar_gasolinera(request, idGasolinera):
    tipoPeticion = get_object_or_404(Gasolinera, pk=idGasolinera)
    tipoPeticion.estado = False
    tipoPeticion.usuario_modificacion = request.user.username
    tipoPeticion.save()
    return redirect('gasolineras')


#####################################################################################################################
@login_required
def ordenCombustibles(request):
    ordenCombustibles = OrdenCombustible.objects.filter(estado=True)
    return render(request, 'ordenCombustible/index.html', {'ordenCombustibles': ordenCombustibles})

@login_required
def crear_ordenCombustible(request):
    if request.method == 'GET':
        return render(request, 'ordenCombustible/crear.html', {'formulario': OrdenCombustibleForm})
    else:
        try:
            formulario = OrdenCombustibleForm(request.POST or None)
            if formulario.is_valid():
                new_formulario = formulario.save(commit=False)
                new_formulario.usuario_creacion = request.user.username
                formulario.save()
                return redirect('ordenCombustibles')
            else:
                return render(request, 'ordenCombustible/crear.html', {'formulario': formulario})
        except ValueError:
            return render(request, 'ordenCombustible/crear.html', 
                          {'formulario': OrdenCombustibleForm, 'error': 'Se han pasado datos incorrectos. Inténtalo de nuevo.'})

@login_required
def editar_ordenCombustible(request, idOrdenCombustible):
    ordenCombustible = get_object_or_404(OrdenCombustible, pk=idOrdenCombustible)
    if request.method == 'GET':
        formulario = OrdenCombustibleForm(instance=ordenCombustible)
        return render(request, 'ordenCombustible/editar.html', {'formulario': formulario})
    else:
        try:
            formulario = OrdenCombustibleForm(request.POST or None, instance=ordenCombustible)
            if formulario.is_valid():
                new_formulario = formulario.save(commit=False)
                new_formulario.usuario_modificacion = request.user.username
                formulario.save()
                return redirect('ordenCombustibles')
            else:
                return render(request, 'ordenCombustible/editar.html', {'formulario': formulario})
        except ValueError:
            return render(request, 'ordenCombustible/editar.html', 
                          {'formulario': OrdenCombustibleForm, 'error': 'Se han pasado datos incorrectos. Inténtalo de nuevo.'})

@login_required
def borrar_ordenCombustible(request, idOrdenCombustible):
    tipoPeticion = get_object_or_404(OrdenCombustible, pk=idOrdenCombustible)
    tipoPeticion.estado = False
    tipoPeticion.usuario_modificacion = request.user.username
    tipoPeticion.save()
    return redirect('ordenCombustibles')

#####################################################################################################################
@login_required
def despachoCombustibles(request):
    despachoCombustibles = DespachoCombustible.objects.filter(estado=True)
    return render(request, 'despachoCombustible/index.html', {'despachoCombustibles': despachoCombustibles})

@login_required
def crear_despachoCombustible(request):
    if request.method == 'GET':
        return render(request, 'despachoCombustible/crear.html', {'formulario': DespachoCombustibleForm})
    else:
        try:
            formulario = DespachoCombustibleForm(request.POST or None)
            if formulario.is_valid():
                new_formulario = formulario.save(commit=False)
                new_formulario.usuario_creacion = request.user.username
                formulario.save()
                return redirect('despachoCombustibles')
            else:
                return render(request, 'despachoCombustible/crear.html', {'formulario': formulario})
        except ValueError:
            return render(request, 'despachoCombustible/crear.html', 
                          {'formulario': DespachoCombustibleForm, 'error': 'Se han pasado datos incorrectos. Inténtalo de nuevo.'})

@login_required
def editar_despachoCombustible(request, idDespachoCombustible):
    despachoCombustible = get_object_or_404(DespachoCombustible, pk=idDespachoCombustible)
    if request.method == 'GET':
        formulario = DespachoCombustibleForm(instance=despachoCombustible)
        return render(request, 'despachoCombustible/editar.html', {'formulario': formulario})
    else:
        try:
            formulario = DespachoCombustibleForm(request.POST or None, instance=despachoCombustible)
            if formulario.is_valid():
                new_formulario = formulario.save(commit=False)
                new_formulario.usuario_modificacion = request.user.username
                formulario.save()
                return redirect('despachoCombustibles')
            else:
                return render(request, 'despachoCombustible/editar.html', {'formulario': formulario})
        except ValueError:
            return render(request, 'despachoCombustible/editar.html', 
                          {'formulario': DespachoCombustibleForm, 'error': 'Se han pasado datos incorrectos. Inténtalo de nuevo.'})

@login_required
def borrar_despachoCombustible(request, idDespachoCombustible):
    tipoPeticion = get_object_or_404(DespachoCombustible, pk=idDespachoCombustible)
    tipoPeticion.estado = False
    tipoPeticion.usuario_modificacion = request.user.username
    tipoPeticion.save()
    return redirect('despachoCombustibles')