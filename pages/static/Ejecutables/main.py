from os import system
import Proyeccion
import Seleccion
from pathlib import Path
import sys
import subprocess
from time import sleep
#Es el main del programa. Importa las clases
#y decide a qué función invocar para la traducción de la sentencia.
if __name__ == "__main__":
    path = str(Path().absolute())
    nombre_archivo = sys.argv[1]

    #Descomentar la siguiente línea para compilar el analizador.
    #system("/home/marco/Documentos/GitHub/Calculadora/pages/static/Ejecutables/compilar.sh")

    #Lee la consulta desde un archivo
    consulta = ""
    archivo_entrada = open(path+"/pages/static/Ejecutables/Archivos_consulta/%s" % nombre_archivo)
    cadena_entrada = archivo_entrada.readline()
    if(cadena_entrada[0] == " "):
        cadena_entrada = cadena_entrada[1:]
    elif(cadena_entrada[-1] == " "):
        cadena_entrada = cadena_entrada[:-1]
    cmd = subprocess.run(["./pages/static/Ejecutables/a.out"],input=cadena_entrada, capture_output=True, text=True)
    archivo_consulta = str(cmd.stdout)
    archivo_consulta = archivo_consulta[archivo_consulta.find("\n")+1:]
    abecedario = "()abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMÑOPQRSTUVWXYZ="
    archivo_consulta = archivo_consulta.replace(" ",'')
    archivo_consulta = archivo_consulta.replace("Identificador",'')
    archivo_consulta = archivo_consulta.replace("\n",'')
    archivo = open(path+"/pages/static/Ejecutables/Archivos_consulta/%s" % archivo_consulta)
    consulta = archivo.readline()
    archivo.close()

    #Traduce la consulta en sql
    pro = Proyeccion.Proyeccion()
    sel = Seleccion.Seleccion()
    consulta_sql = "null"
    if("PI" in consulta and "SE" not in consulta and "-" not in consulta):
        consulta_sql = pro.reemplazar_pi(consulta)
    if("PI" in consulta and "SE" not in consulta and "-" in consulta):
        consulta_sql = pro.pi_diferencia(consulta)
    if("SE" in consulta and "PI" not in consulta):
        consulta_sql = sel.reemplazar_se(consulta)
    if("SE" in consulta and "PI" not in consulta and "-" in consulta):
        consulta_sql = sel.reemplazar_minus(consulta)
    if("PI" in consulta and "SE" in consulta and "UNION" not in consulta):
        consulta_sql = pro.ProyeccionYSeleccion(consulta)
    if(("SE" in consulta or "PI" in consulta) and ("UNION" in consulta or "INTER" in consulta)):
        consulta_sql = sel.reemplazar_union_interseccion(consulta)
    if("SE" not in consulta and "PI" not in consulta and "UNION" in consulta):
        consulta_sql = pro.UnionTablas(consulta)
    if("SE" not in consulta and "PI" not in consulta and "INTER" in consulta):
        consulta_sql = sel.reemplazar_union_interseccion(consulta)

    #Lee la consulta en sql desde el archivo y elimina el archivo.
    archivo = open(path+'/pages/static/Ejecutables/Archivos_consulta/%s' % nombre_archivo, "w")
    archivo.write(consulta_sql)
    archivo.close()
    system("rm "+path+"/pages/static/Ejecutables/Archivos_consulta/%s" % archivo_consulta)
