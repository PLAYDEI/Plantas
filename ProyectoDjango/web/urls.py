from django.urls import path
from . import views

urlpatterns = [
    path('Abono/', views.Abono, name='Abono'),
    path('Arbustos/', views.Arbustos, name='Arbustos'),
    path('Index/', views.Index, name='Index'),
    path('Rosas/', views.Rosas, name='Rosas'),
    path('Claveles/', views.Claveles, name='Claveles'),
    path('Tulipanes/', views.Tulipanes, name='Tulipanes'),
    path('Girasoles/', views.Girasoles, name='Girasoles'),
    path('Gerbera/', views.Gerbera, name='Gerbera'),
    path('Macetero/', views.Macetero, name='Macetero'),
    path('Tierra/', views.Tierra, name='Tierra'),
    path('Plantas/', views.Plantas, name='Plantas'),
    path('listadoSQL/', views.listadoSQL, name='listadoSQL'),
]