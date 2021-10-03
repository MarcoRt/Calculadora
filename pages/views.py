from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Customers
import logging
# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'

class FAQPageView(TemplateView):
    template_name = "faq.html"

class AboutPageView(TemplateView):
    template_name = "about.html"

class ContactPageView(TemplateView):
    template_name = "contact.html"

class TeoriaPageView(TemplateView):
    template_name = "teoria.html"

class SeleccionPageView(TemplateView):
    template_name = "seleccion.html"

class ProyeccionPageView(TemplateView):
    template_name = "proyeccion.html"

class ConjuntosPageView(TemplateView):
    template_name = "conjuntos.html"

class ProductoCartesianoPageView(TemplateView):
    template_name = "productoCartesiano.html"

class ReunionPageView(TemplateView):
    template_name = "reunion.html"

class PracticaPageView(TemplateView):
    template_name = "practica.html"

def probando(request):
    for c in Customers.objects.raw("Select * from customers;"):
        print(c)
    context = {'nombre':'marco'}
    return render(request, 'test.html',context)
