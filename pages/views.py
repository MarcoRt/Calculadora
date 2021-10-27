from os import system
import os.path, time
from pathlib import Path
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseNotFound
from datetime import datetime
from time import sleep
import subprocess
from django.core.files.storage import FileSystemStorage

# Create your views here.
def getNombreDeArchivos():
    path = str(Path().absolute())
    path = path + "/pages/static/media"
    system("ls %s > %s/lista_de_archivos " % (path,path))
    lista_de_archivos = open("%s/lista_de_archivos" % path, "r")
    lista_de_archivos = lista_de_archivos.readlines()
    lista_de_archivos_para_mostrar = []
    for archivo in lista_de_archivos:
        lista_de_archivos_para_mostrar.append(archivo.replace(".sql\n",""))
    aux = lista_de_archivos_para_mostrar.index("lista_de_archivos\n")
    lista_de_archivos_para_mostrar.pop(aux)
    return lista_de_archivos_para_mostrar

def getNombreDeColumnas(cadena):
    aux = cadena.find("(")
    cadena = cadena[aux+1:]
    cadena = cadena.replace(")","")
    if(chr(88) in cadena):
        cadena = cadena.split(chr(88))
        columnas = []
        for i in cadena:
            columnas+= Realizar_consultas("select COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '%s'" % i)
        cadena = columnas
    else:
        cadena = Realizar_consultas("select COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '%s'" % cadena)
    resultado = []
    for i in cadena:
        for y in i:
            resultado.append(y)
    return resultado

def getNombreDeColumna(cadena):
    if(cadena.count("(") > 1):
        aux = cadena.index("(")
        cadena_lista = list(cadena)
        cadena_lista[aux] = ""
        cadena = "".join(cadena_lista)
        if(cadena[-1] == ")"):
            cadena_lista = list(cadena)
            cadena_lista[-1] = ""
            cadena = "".join(cadena_lista)
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
    resultados = []
    if consulta_sql != 'null':
        resultados = Realizar_consultas(consulta_sql)
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
def SubirArchivoPageView(request):
    context = {}
    uploaded_file = request.FILES['document']
    if(uploaded_file.size > 2621440 or uploaded_file.content_type != "application/sql"):
        context["success"] = False
        context["successmsg"] = "Error al subir archivo."
    else:
        context["success"] = True
        context["successmsg"] = "El archivo se subió correctamente."
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
    context["lista_de_archivos"] = getNombreDeArchivos()
    return render(request,'practica.html',context)

def ConsultaPageView(request):
    context = {}
    columnas = []
    if request.method == 'POST':
        aux = request.POST['tu_consulta']
        columnas = getNombreDeColumna(aux)
        if(len(columnas) > 1):
            context['columnas'] = columnas
            context['columna'] = ""
            context["consulta_vacia"] = ""
        else:
            context['columna'] = columnas
            context['columnas'] = ""
            context["consulta_vacia"] = ""
        tu_consulta = getConsultaParaAnalizador(aux)
        if(len(tu_consulta) == 0):
            context['tu_consulta'] = ""
            context["consulta_vacia"] = "Error en la consulta."
        else:
            context['tu_consulta'] = tu_consulta
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
