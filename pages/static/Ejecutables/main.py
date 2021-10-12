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
    print(path)
    nombre_archivo = sys.argv[1]
    print("Nombre del archivo ",nombre_archivo)
    system("/home/marco/Documentos/GitHub/Calculadora/pages/static/Ejecutables/compilar.sh")
    archivo_entrada = "<" + path+"/pages/static/Ejecutables/Archivos_consulta/%s" % nombre_archivo
    archivo_entrada = "SE importe<120 (TABLA EQUIS TABLA2 EQUIS TABLA3)"
    cmd = subprocess.run(["./pages/static/Ejecutables/a.out"],input=archivo_entrada, capture_output=True, text=True)
    archivo_consulta = str(cmd.stdout)
    abecedario = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMÑOPQRSTUVWXYZ"
    for i in archivo_consulta:
        if i in abecedario:
            archivo_consulta = archivo_consulta.replace(i,'')
    #print(archivo_consulta)
    archivo = open(path+"/pages/static/Ejecutables/Archivos_consulta/%s" % archivo_consulta)
    consulta = archivo.readline()
    archivo.close()
    print("Valor original: ",consulta)
    pro = Proyeccion.Proyeccion()
    sel = Seleccion.Seleccion()
    if("PI" in consulta and "SE" not in consulta and "-" not in consulta):
        consulta_sql = pro.reemplazar_pi(consulta)
    if("PI" in consulta and "SE" not in consulta and "-" in consulta):
        consulta_sql = pro.pi_diferencia(consulta)
    if("SE" in consulta and "PI" not in consulta):
        consulta_sql = sel.reemplazar_se(consulta)
    if("SE" in consulta and "PI" not in consulta and "-" in consulta):
        consulta_sql = sel.reemplazar_minus(consulta)
    if("PI" in consulta and "SE" in consulta):
        consulta_sql = pro.ProyeccionYSeleccion(consulta)
    archivo = open(path+'/pages/static/Ejecutables/Archivos_consulta/%s' % nombre_archivo, "w")
    archivo.write(consulta_sql)
    archivo.close()
    system("rm "+path+"/pages/static/Ejecutables/Archivos_consulta/%s" % archivo_consulta)
