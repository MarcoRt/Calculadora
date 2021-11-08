from os import system
import os.path, time
from pathlib import Path
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseNotFound
from datetime import datetime
from time import sleep
from string import ascii_letters, digits
from random import choice
from django.core.files.storage import FileSystemStorage
from django.db import connections, transaction, utils
# Create your views here.
def getNombreDeLaBase():
    bases = ["mytest1","mytest2","mytest3","mytest4",
    "mytest5","mytest6","mytest7","mytest8","mytest9","mytest10",
    "mytest11","mytest12","mytest13","mytest14","mytest15","mytest16",
    "mytest17","mytest18","mytest19","mytest20","mytest21","mytest22",
    "mytest23","mytest24","mytest25","mytest26","mytest27","mytest28",
    "mytest29","mytest30","mytest31","mytest32","mytest33","mytest34",
    "mytest35","mytest36","mytest37","mytest38","mytest39","mytest40"]
    tiempos = {}
    for base in bases:
        cursor = connections[base].cursor()
        try:
            cursor.execute("select MAX(ts) from timeDate;")
            row = cursor.fetchone()
            aux = str(row[0])
            aux = aux.replace("datetime.datetime()","")
            aux = aux.replace(":","")
            aux = aux.replace("-","")
            aux = aux.replace(" ","")
            tiempos[aux] = base
            row = ""
        except utils.ProgrammingError:
            pass
    aux = sorted(tiempos)
    nombre_bd = tiempos[aux[0]]
    LimpiarBase(nombre_bd)
    return nombre_bd

def ejecutarArchivoSql(NombreDeLaBase,NombreDelArchivo):
    cursor = connections[NombreDeLaBase].cursor()
    path = str(Path().absolute())
    path = path + "/pages/static/media/"
    file = open(path+"%s" % NombreDelArchivo,"r")
    script = file.read()
    now = datetime.now()
    try:
        cursor.execute("insert into timeDate values(1,'%s');" % (now,))
        cursor.execute("%s" % script)
    except utils.ProgrammingError:
        pass
def getEstadoDeLaBase(NombreDeLaBase):
    cursor = connections[NombreDeLaBase].cursor()
    cursor.execute("show tables;")
    row = cursor.fetchone()
    resultado = []
    while row is not None:
        resultado.append(list(row))
        row = cursor.fetchone()
    if len(resultado) > 0:
        return False
    else:
        return True

def LimpiarBase(NombreDeLaBase):
    cursor = connections[NombreDeLaBase].cursor()
    cursor.execute("show tables;")
    row = cursor.fetchone()
    Resultados_Consulta = []
    while row is not None:
        Resultados_Consulta.append(list(row))
        row = cursor.fetchone()
    ListaTablas = []
    for i in Resultados_Consulta:
        for y in i:
            ListaTablas.append(y)
    ListaTablas.pop(ListaTablas.index("timeDate"))
    for tabla in ListaTablas:
        cursor.execute("drop table %s;" % tabla)

def getClaveDeUsuario():
    letters = digits
    clave_usuario = ''.join(choice(letters) for i in range(5))
    letters = ascii_letters
    clave_usuario += ''.join(choice(letters) for i in range(5))
    clave_usuario += "@"
    return clave_usuario

def getNombreDeArchivos(clave_usuario):
    path = str(Path().absolute())
    path = path + "/pages/static/media"
    system("ls %s > %s/lista_de_archivos " % (path,path))
    lista_de_archivos = open("%s/lista_de_archivos" % path, "r")
    lista_de_archivos = lista_de_archivos.readlines()
    lista_de_archivos_para_mostrar = []
    for archivo in lista_de_archivos:
        if clave_usuario in archivo:
            aux = archivo.replace(clave_usuario,"")
            lista_de_archivos_para_mostrar.append(aux.replace(".sql\n",""))
    lista_de_archivos_para_mostrar.insert(0,"Otra")
    lista_de_archivos_para_mostrar.insert(0,"Escuela")
    return lista_de_archivos_para_mostrar

def getNombreDeColumnas(cadena, nombre_bd):
    aux = cadena.find("(")
    cadena = cadena[aux+1:]
    cadena = cadena.replace(")","")
    if(chr(88) in cadena):
        cadena = cadena.split(chr(88))
        columnas = []
        for i in cadena:
            try:
                columnas+= Realizar_consultas("select COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '%s'" % i,nombre_bd)
            except utils.ProgrammingError:
                pass
        cadena = columnas
    else:
        try:
            cadena = Realizar_consultas("select COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '%s'" % cadena,nombre_bd)
        except utils.ProgrammingError:
            pass
    resultado = []
    for i in cadena:
        for y in i:
            resultado.append(y)
    return resultado

def getNombreDeColumna(cadena, nombre_bd):
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
        cadena = cadena.replace(")","")
        cadena = list(cadena.split(","))
        return cadena
    else:
        return getNombreDeColumnas(cadena,nombre_bd)

def ejecutarAnalizador(cadena, nombre_bd):
    path = str(Path().absolute())
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
        resultados = Realizar_consultas(consulta_sql,nombre_bd)
    system("rm "+path+"/pages/static/Ejecutables/Archivos_consulta/%s" % nombre_archivo)
    return resultados

def getConsultaParaAnalizador(cadena, nombre_bd):
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
        cadena = cadena.replace(chr(88)," EQUIS ")
    if chr(8746) in cadena:
        cadena = cadena.replace(chr(8746)," UNION ")
    if chr(8745) in cadena:
        cadena = cadena.replace(chr(8745),"INTER")
    return ejecutarAnalizador(cadena,nombre_bd)

def Realizar_consultas(cadena, nombre_bd):
    cadena = cadena.replace("\x00","")
    cursor = connections[nombre_bd].cursor()
    resultados = []
    cursor.execute("%s" % (cadena,))
    row = cursor.fetchone()
    while row is not None:
        resultados.append(list(row))
        row = cursor.fetchone()
    return resultados
def SeleccionarArchivoView(request):
    context= {}
    context["lista_de_archivos"] = {"Escuela","Otra"}
    if(request.method == 'POST'):
        nombre_usuario = request.POST.get("nombre_usuario_db",False)
        nombre_bd = request.POST.get("nombre_bd",False)
        db_seleccionada = request.POST.get("nombre_bd_2",False)
        if nombre_usuario != "":
            context["lista_de_archivos"] = {"Escuela","Otra",nombre_usuario}
    context["nombre_usuario_db"] = nombre_usuario
    context["nombre_bd"] = nombre_bd
    context["nombre_bd_2"] = db_seleccionada
    return render(request,'practica.html',context)

def SubirArchivoPageView(request):
    context = {}
    clave_usuario = getClaveDeUsuario()
    archivo_arriba = request.POST.get("document",False)
    if(archivo_arriba == False):
        uploaded_file = request.FILES['document']
        if(uploaded_file.size > 2621440 or uploaded_file.content_type != "application/sql"):
            context["success"] = False
            context["successmsg"] = "Error al subir archivo."
        else:
            context["success"] = True
            context["successmsg"] = "El archivo se subió correctamente."
            fs = FileSystemStorage()
            nombre_archivo = clave_usuario+uploaded_file.name
            fs.save(nombre_archivo, uploaded_file)
            nombre_db = ""
            nombre_db = getNombreDeLaBase()
            context["nombre_bd"] = nombre_db
            ejecutarArchivoSql(nombre_db,nombre_archivo)
    else:
        context["success"] = False
        context["successmsg"] = "Error al subir archivo."
    context["lista_de_archivos"] = getNombreDeArchivos(clave_usuario)
    nombre_usuario_db = context["lista_de_archivos"]
    if(len(nombre_usuario_db) > 2):
        context["nombre_usuario_db"] = nombre_usuario_db[-1]

    return render(request,'practica.html',context)

def ConsultaPageView(request):
    context = {}
    columnas = []
    if request.method == 'POST':
        nombre_bd = request.POST.get("nombre_bd",False)
        nombre_usuario_db = request.POST.get("nombre_usuario_db",False)
        db_seleccionada = request.POST.get("nombre_bd_2",False)
        if(db_seleccionada == "" or db_seleccionada=="Escuela"):
            db_seleccionada = "escuela"
        else:
            db_seleccionada = nombre_bd
        aux = request.POST.get("tu_consulta",False)
        if(aux == ""):
            context["consulta_vacia"] = "Error en la consulta."
        else:
            columnas = getNombreDeColumna(aux,db_seleccionada)
            if(len(columnas) > 1):
                context['columnas'] = columnas
                context['columna'] = ""
                context["consulta_vacia"] = ""
            else:
                context['columna'] = columnas
                context['columnas'] = ""
                context["consulta_vacia"] = ""
            tu_consulta = getConsultaParaAnalizador(aux,db_seleccionada)
            if(len(tu_consulta) == 0):
                context['tu_consulta'] = ""
                context['columnas'] = ""
                context['columna'] = ""
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

def PracticaPageView(request):
    context = {}
    context["lista_de_archivos"] = {"Escuela","Otra"}
    context["clave_usuario"] = ""
    return render(request,'practica.html',context)

class EjemplosPageView(TemplateView):
    template_name = "ejemplos.html"

class SintaxisPageView(TemplateView):
    template_name = "sintaxis.html"
