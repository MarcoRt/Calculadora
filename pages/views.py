from os import system
from pathlib import Path
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseNotFound
from datetime import datetime
from time import sleep
import subprocess
# Create your views here.
def getNombreDeColumnas(cadena):
    aux = cadena.find("(")
    cadena = cadena[aux+1:]
    cadena = cadena.replace(")","")
    print(cadena)
    if(chr(88) in cadena):
        cadena = cadena.split(chr(88))
        columnas = []
        for i in cadena:
            columnas+= Realizar_consultas("select COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '%s'" % i)
        cadena = columnas
    else:
        cadena = Realizar_consultas("select COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '%s'" % cadena)
    return cadena
def getNombreDeColumna(cadena):
    if(chr(960) in cadena):
        inicio = cadena.find(chr(960))
        final = cadena.find("(")
        cadena = cadena[inicio+1:final]
        cadena = cadena.replace(" ","")
        cadena = list(cadena.split(","))
        return cadena
    else:
        return getNombreDeColumnas(cadena)

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
    resultados = Realizar_consultas(consulta_sql)
    #print(resultados)
    if(ejecucion_correcta == 0):
        system("rm "+path+"/pages/static/Ejecutables/Archivos_consulta/%s" % nombre_archivo)
    return resultados

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
        cadena = cadena.replace(chr(963),"SE ")
    if chr(960) in cadena:
        cadena = cadena.replace(chr(960),"PI ")
        if("PI  " in cadena):
            cadena = cadena.replace("PI  ","PI ")
    if chr(88) in cadena:
        cadena = cadena.replace(chr(88),"EQUIS")
    if chr(8746) in cadena:
        cadena = cadena.replace(chr(8746),"UNION")
    if chr(8745) in cadena:
        cadena = cadena.replace(chr(8745),"REVISAR")
    return ejecutarAnalizador(cadena)

def Realizar_consultas(cadena):
    from django.db import connection, transaction
    cursor = connection.cursor()
    cursor.execute("%s" % cadena)
    row = cursor.fetchone()
    resultados = []
    while row is not None:
        #print(row)
        resultados.append(list(row))
        row = cursor.fetchone()
    return resultados

def ConsultaPageView(request):
    context = {}
    if(request.POST):
        aux = request.POST['tu_consulta']
        context['columnas'] = getNombreDeColumna(aux)
        context['tu_consulta'] = getConsultaParaAnalizador(aux)
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