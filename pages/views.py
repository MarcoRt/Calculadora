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
#Busca los archivos sql que se han creado y los elimina
def EliminarArchivo(nombre_archivo):
    if nombre_archivo != "NULL":
        path = str(Path().absolute())
        path = path + "/pages/static/media/" + nombre_archivo
        system("rm %s" % (path,))

# Busca dentro de los registros de la base cual es la que tiene más tiempo sin usar
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

# Ejecuta el archivo sql que subió el usuario.
def ejecutarArchivoSql(NombreDeLaBase,NombreDelArchivo):
    cursor = connections[NombreDeLaBase].cursor()
    path = str(Path().absolute())
    path = path + "/pages/static/media/"
    file = open(path+"%s" % NombreDelArchivo,"r")
    script = file.read()
    now = datetime.now()
    aux = script.upper()
    inicio = aux.index("CREATE TABLE")
    script = script[inicio:]
    try:
        cursor.execute("insert into timeDate values(1,'%s','%s');" % (now,NombreDelArchivo))
        cursor.execute("%s" % script)
    except utils.ProgrammingError:
        pass

# Elimina todas las tablas creadas dentro de la base.
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
    #cursor.execute("select nombrearchivo from timeDate;")

# Genera una clave cuando el usuario sube un archivo.

def getClaveDeUsuario():
    letters = digits
    clave_usuario = ''.join(choice(letters) for i in range(5))
    letters = ascii_letters
    clave_usuario += ''.join(choice(letters) for i in range(5))
    clave_usuario += "@"
    return clave_usuario

# Genera la lista de archivos como opción de selección de acuerdo a su usuario.
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
    lista_de_archivos_para_mostrar.insert(0,"Trabajo")
    lista_de_archivos_para_mostrar.insert(0,"Escuela")
    return lista_de_archivos_para_mostrar

# Genera el nombre las columnas dentro de la consulta.
def getNombreDeColumnas(cadena, nombre_bd):
    columnas = []
    resultado = []
    # 8746 ∪
    # 8745 ∩
    if(chr(8746) in cadena):
        columnas = cadena.split(chr(8746))
        aux = []
        aux = Realizar_consultas("SELECT column_name FROM information_schema.columns WHERE  table_name = '%s' AND table_schema = '%s';" % (columnas[0],nombre_bd),nombre_bd)
        for i in aux:
            for y in i:
                resultado.append(y)
    if(chr(8745) in cadena):
        columnas = cadena.split(chr(8745))
        aux = []
        aux = Realizar_consultas("SELECT column_name FROM information_schema.columns WHERE  table_name = '%s' AND table_schema = '%s';" % (columnas[0],nombre_bd),nombre_bd)
        for i in aux:
            for y in i:
                resultado.append(y)
        aux = set(resultado)
        aux = list(aux)
        resultado = aux
    aux = cadena.find("(")
    cadena = cadena[aux+1:]
    cadena = cadena.replace(")","")
    if(chr(88) in cadena):
        cadena = cadena.split(chr(88))
        for i in cadena:
            try:
                columnas+= Realizar_consultas("SELECT column_name FROM information_schema.columns WHERE  table_name = '%s' AND table_schema = '%s';" % (i,nombre_bd),nombre_bd)
            except utils.ProgrammingError:
                pass
        cadena = columnas
    else:
        try:
            cadena = Realizar_consultas("SELECT column_name FROM information_schema.columns WHERE  table_name = '%s' AND table_schema = '%s';" % (cadena,nombre_bd,),nombre_bd)
        except utils.ProgrammingError:
            pass
    for i in cadena:
        for y in i:
            resultado.append(y)
    aux = set(resultado)
    aux = list(aux)
    resultado = aux
    return resultado

# Genera el nombre las columna dentro de la consulta.
def getNombreDeColumna(cadena, nombre_bd):
    if(chr(960)+" (" in cadena or chr(960)+"(" in cadena):
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
# Ejecuta el analizador y regresa la consulta en sql.
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
        try:
            resultados = Realizar_consultas(consulta_sql,nombre_bd)
        except (utils.ProgrammingError, utils.OperationalError):
            pass
    system("rm "+path+"/pages/static/Ejecutables/Archivos_consulta/%s" % nombre_archivo)
    return resultados

# Genera la consulta cambiando los símbolos del navegador a expresiones que reconoce
# el analizador.
def getConsultaParaAnalizador(cadena, nombre_bd):
    # 8904 ⋈
    # 963 σ
    # 960 π
    # 88 X
    # 8746 ∪
    # 8745 ∩
    # 8743 ∧
    # 8744 ∨
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
        if "  " in cadena:
            cadena = cadena.replace("  "," ")
    if chr(8745) in cadena:
        cadena = cadena.replace(chr(8745),"INTER")
    if chr(8743) in cadena:
        cadena = cadena.replace(chr(8743),chr(94))
    if chr(8744) in cadena:
        cadena = cadena.replace(chr(8744),chr(94)+chr(94))
    return ejecutarAnalizador(cadena,nombre_bd)

# Genera las consultas sql
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
# View que muestra la selección y cambia la selección de la base.
def SeleccionarArchivoView(request):
    context= {}
    context["lista_de_archivos"] = {"Escuela","Trabajo"}
    if(request.method == 'POST'):
        nombre_usuario = request.POST.get("nombre_usuario_db",False)
        nombre_bd = request.POST.get("nombre_bd",False)
        db_seleccionada = request.POST.get("nombre_bd_2",False)
        if nombre_usuario != "":
            context["lista_de_archivos"] = {"Escuela","Trabajo",nombre_usuario}
    context["nombre_usuario_db"] = nombre_usuario
    context["nombre_bd"] = nombre_bd
    context["nombre_bd_2"] = db_seleccionada
    return render(request,'practica.html',context)

# View que maneja el guardado de los archivos y los prepara para su ejecución.
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
# View que recibe la consulta y la gestiona.
def ConsultaPageView(request):
    context = {}
    columnas = []
    if request.method == 'POST':
        nombre_bd = request.POST.get("nombre_bd",False)
        nombre_usuario_db = request.POST.get("nombre_usuario_db",False)
        db_seleccionada = request.POST.get("nombre_bd_2",False)
        if(db_seleccionada == "" or db_seleccionada=="Escuela"):
            db_seleccionada = "escuela"
        elif(db_seleccionada == "Trabajo"):
            db_seleccionada = "trabajo"
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
# View que genera la pantalla Index
class HomePageView(TemplateView):
    template_name = 'index.html'

# View que genera la pantalla Faq
class FAQPageView(TemplateView):
    template_name = "faq.html"

# View que genera la pantalla Acerca
class AboutPageView(TemplateView):
    template_name = "acerca.html"

# View que genera la pantalla Contacto
class ContactPageView(TemplateView):
    template_name = "contacto.html"

# View que genera la pantalla Teoria
class TeoriaPageView(TemplateView):
    template_name = "teoria.html"

# View que genera la pantalla Teoría - Seleccion
class SeleccionPageView(TemplateView):
    template_name = "teoria-seleccion.html"

# View que genera la pantalla Teoría - Proyeccion
class ProyeccionPageView(TemplateView):
    template_name = "teoria-proyeccion.html"
# View que genera la pantalla Teoría - Union
class UnionPageView(TemplateView):
    template_name = "teoria-union.html"

# View que genera la pantalla Teoría - Producto
class ProductoCartesianoPageView(TemplateView):
    template_name = "teoria-producto.html"

# View que genera la pantalla Teoría - Reunión
class ReunionPageView(TemplateView):
    template_name = "teoria-reunion.html"
# View que genera la pantalla Teoría - Diferencia
class DiferenciaPageView(TemplateView):
    template_name = "teoria-diferencia.html"

# View que genera la pantalla Práctica
def PracticaPageView(request):
    context = {}
    context["lista_de_archivos"] = {"Escuela","Trabajo"}
    context["clave_usuario"] = ""
    return render(request,'practica.html',context)
# View que genera la pantalla ejemplos
class EjemplosPageView(TemplateView):
    template_name = "ejemplos.html"
# View que genera la pantalla sintaxis
class SintaxisPageView(TemplateView):
    template_name = "sintaxis.html"
