from django.urls import path
from . import views
from .views import (HomePageView,
    FAQPageView,
    AboutPageView,
    ContactPageView,
    TeoriaPageView,
    SeleccionPageView,
    ProyeccionPageView,
    ConjuntosPageView,
    ProductoCartesianoPageView,
    ReunionPageView,
    PracticaPageView
    )
urlpatterns = [
    path('faq/',FAQPageView.as_view(),name='faq'),
    path('',HomePageView.as_view(),name='index'),
    path('index/',HomePageView.as_view(),name='index'),
    #path('',views.probando,name='probando'),
    path('about/',AboutPageView.as_view(),name='about'),
    path('contact/',ContactPageView.as_view(),name='contact'),
    path('teoria/',TeoriaPageView.as_view(),name='teoria'),
    path('teoria/seleccion/',SeleccionPageView.as_view(),name='seleccion'),
    path('teoria/proyeccion/',ProyeccionPageView.as_view(),name='proyeccion'),
    path('teoria/conjuntos/',ConjuntosPageView.as_view(),name='conjuntos'),
    path('teoria/productoCartesiano/',ProductoCartesianoPageView.as_view(),name='productoCartesiano'),
    path('teoria/reunion/',ReunionPageView.as_view(),name='reunion'),
    path('practica/',PracticaPageView.as_view(),name='practica'),
    path('test/',views.probando,name='test'),
]
