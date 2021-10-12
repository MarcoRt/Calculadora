from os import system
from pathlib import Path
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseNotFound
from datetime import datetime
from time import sleep
import subprocess
# Create your views here.
def ejecutarAnalizador(cadena):
    path = str(Path().absolute())
    #print("Ejecutar analizador " + cadena)
    nombre_archivo = str(datetime.now())
    nombre_archivo = nombre_archivo.replace(' ','')
    archivo = open(path+'/pages/static/Ejecutables/Archivos_consulta/%s' % nombre_archivo, "w")
    archivo.write(cadena)
    archivo.close()
    ejecucion_correcta = system("python3 /home/marco/Documentos/GitHub/Calculadora/pages/static/Ejecutables/main.py %s" % nombre_archivo)
    archivo = open(path+'/pages/static/Ejecutables/Archivos_consulta/%s' % nombre_archivo, "r")
    consulta_sql = archivo.readline()
    archivo.close()
    print(consulta_sql)
    if(ejecucion_correcta == 0):
        system("rm "+path+"/pages/static/Ejecutables/Archivos_consulta/%s" % nombre_archivo)

def getConsultaParaAnalizador(cadena):
    # 8904 ⋈
    # 963 σ
    # 960 π
    # 88 X
    # 8746 ∪
    # 8745 ∩
    if chr(8904) in cadena:
        cadena = cadena.replace(chr(8904),"Hola")
    if chr(963) in cadena:
        cadena = cadena.replace(chr(963),"SE")
    if chr(960) in cadena:
        cadena = cadena.replace(chr(960),"PI")
    if chr(88) in cadena:
        cadena = cadena.replace(chr(88),"EQUIS")
    if chr(8746) in cadena:
        cadena = cadena.replace(chr(8746),"UNION")
    if chr(8745) in cadena:
        cadena = cadena.replace(chr(8745),"REVISAR")
    ejecutarAnalizador(cadena)

def Realizar_consultas():
    from django.db import connection, transaction
    cursor = connection.cursor()
    cursor.execute("select CursoID, ProfesorID, Nombre from curso;")
    row = cursor.fetchone()
    while row is not None:
        print(row)
        row = cursor.fetchone()

def ConsultaPageView(request):
    context = {}
    if(request.POST):
        context['nombre'] = 'poll full of liquior'
        aux = request.POST['tu_consulta']
        getConsultaParaAnalizador(aux)
        return render(request,'consulta.html',context)
    else:
        return HttpResponseNotFound('<h1>Page not found</h1>')
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

class ConjuntosPageView(TemplateView):
    template_name = "teoria-conjuntos.html"

class ProductoCartesianoPageView(TemplateView):
    template_name = "teoria-producto.html"

class ReunionPageView(TemplateView):
    template_name = "teoria-reunion.html"

class PracticaPageView(TemplateView):
    template_name = "practica.html"
