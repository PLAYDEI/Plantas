from django.shortcuts import render
from .models import Usuario

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

def listadoSQL(request):
    web= Usuario.objects.raw('SELECT * FROM web_usuario')
    print(web)
    context={"web":web}
    return render(request, 'web/listadoSQL.html', context)


