from django.urls import path
from . import views
from .views import (HomePageView,
    FAQPageView,
    AboutPageView,
    ContactPageView, SintaxisPageView,
    TeoriaPageView,
    SeleccionPageView,
    ProyeccionPageView,
    UnionPageView,
    ProductoCartesianoPageView,
    ReunionPageView,
    PracticaPageView,
    EjemplosPageView,
    SintaxisPageView,
    DiferenciaPageView,
    SubirArchivoPageView
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
    path('teoria/union/',UnionPageView.as_view(),name='teoria-union'),
    path('teoria/producto/',ProductoCartesianoPageView.as_view(),name='teoria-producto'),
    path('teoria/reunion/',ReunionPageView.as_view(),name='teoria-reunion'),
    path('teoria/diferencia/',DiferenciaPageView.as_view(),name='teoria-diferencia'),
    path('practica/',PracticaPageView.as_view(),name='practica'),
    path('practica/consulta/',views.ConsultaPageView,name='consulta'),
    path('practica/subir-archivo/',views.SubirArchivoPageView,name='subir-archivo'),
    path('ejemplos/',EjemplosPageView.as_view(),name='ejemplos'),
    path('sintaxis/',SintaxisPageView.as_view(),name='sintaxis'),
]
