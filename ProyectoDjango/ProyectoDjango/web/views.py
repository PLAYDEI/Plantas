from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib import messages
from .models import Usuario
from .forms import RegistroForm, LoginForm

# Create your views here.
def Index(request):
    context={}
    return render(request, 'web/Index.html', context)

def Rosas(request):
    context={}
    return render(request, 'web/Rosas.html', context)

def Claveles(request):
    context={}
    return render(request, 'web/Claveles.html', context)

def Tulipanes(request):
    context={}
    return render(request, 'web/Tulipanes.html', context)

def Girasoles(request):
    context={}
    return render(request, 'web/Girasoles.html', context)

def Gerbera(request):
    context={}
    return render(request, 'web/Gerbera.html', context)

def Macetero(request):
    context={}
    return render(request, 'web/Macetero.html', context)

def Arbustos(request):
    context={}
    return render(request, 'web/Arbustos.html', context)

def Tierra(request):
    context={}
    return render(request, 'web/Tierra.html', context)

def Plantas(request):
    context={}
    return render(request, 'web/Plantas.html', context)

def Abono(request):
    context={}
    return render(request, 'web/Abono.html', context)

def Registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Ya se registró!')  # Mensaje de éxito
            return redirect('Accesorios')  # Redirige a la página de Accesorios o donde desees
    else:
        form = RegistroForm()
    
    return render(request, 'web/Registro.html', {'form': form})

def Login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Ya se registró!')  # Mensaje de éxito
            return redirect('Accesorios')  # Redirige a la página de Accesorios o donde desees
    else:
        form = LoginForm()
    
    return render(request, 'web/Login.html', {'form': form})


#Esta en duda
def listadoSQL(request):
    web= Usuario.objects.raw('SELECT * FROM web_usuario')
    print(web)
    context={"web":web}
    return render(request, 'web/listadoSQL.html', context)


