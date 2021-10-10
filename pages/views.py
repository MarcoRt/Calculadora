from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'

class FAQPageView(TemplateView):
    template_name = "faq.html"

class AboutPageView(TemplateView):
    template_name = "acerca.html"

class ContactPageView(TemplateView):
    template_name = "contacto.html"

class TeoriaPageView(TemplateView):
    template_name = "teoria.html"

class SeleccionPageView(TemplateView):
    template_name = "teoria-seleccion.html"

class ProyeccionPageView(TemplateView):
    template_name = "teoria-proyeccion.html"

class UnionPageView(TemplateView):
    template_name = "teoria-union.html"

class ProductoCartesianoPageView(TemplateView):
    template_name = "teoria-producto.html"

class ReunionPageView(TemplateView):
    template_name = "teoria-reunion.html"

class DiferenciaPageView(TemplateView):
    template_name = "teoria-diferencia.html"    

class PracticaPageView(TemplateView):
    template_name = "practica.html"

class EjemplosPageView(TemplateView):
    template_name = "ejemplos.html"

class SintaxisPageView(TemplateView):
    template_name = "sintaxis.html"