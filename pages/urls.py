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
    path('acerca/',AboutPageView.as_view(),name='acerca'),
    path('contacto/',ContactPageView.as_view(),name='contacto'),
    path('teoria/',TeoriaPageView.as_view(),name='teoria'),
    path('teoria/seleccion/',SeleccionPageView.as_view(),name='teoria-seleccion'),
    path('teoria/proyeccion/',ProyeccionPageView.as_view(),name='teoria-proyeccion'),
    path('teoria/conjuntos/',ConjuntosPageView.as_view(),name='teoria-conjuntos'),
    path('teoria/producto/',ProductoCartesianoPageView.as_view(),name='teoria-producto'),
    path('teoria/reunion/',ReunionPageView.as_view(),name='teoria-reunion'),
    path('practica/',PracticaPageView.as_view(),name='practica'),
    path('practica/consulta/',views.ConsultaPageView,name='consulta'),
]
