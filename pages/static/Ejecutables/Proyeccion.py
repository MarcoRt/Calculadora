from re import findall
class Proyeccion:
    #Constructor vacío
    def __init__(self):
        pass
    #Traduce consultas que solo tienen la sentencia de proyección
    def reemplazar_pi(self,consulta):
        consulta = consulta.replace("PI","SELECT ")
        consulta = consulta.replace("("," from (")
        consulta = consulta+";"
        #print(consulta)
        return consulta
    #Traduce consultas con sentencias de proyeción y diferencia
    def pi_diferencia(self, consulta):
        aux = consulta.find("-")
        primera_sentencia = consulta[:aux]
        segunda_sentencia = consulta[aux+1:]
        primera_sentencia = self.reemplazar_pi(primera_sentencia)
        primera_sentencia = primera_sentencia.replace(";","")
        segunda_sentencia = self.reemplazar_pi(segunda_sentencia)
        #print(primera_sentencia + " MINUS " + segunda_sentencia)
        return (primera_sentencia + " MINUS " + segunda_sentencia)
    #Analiza si la sentencia tiene sentencias de proyección y selección o sentencias proyección y más de una selección
    def ProyeccionYSeleccion(self, consulta):
        if(len(findall("SE",consulta)) == 1):
            self.SeleccionSimple(consulta)
        elif(len(findall("SE",consulta))>1):
            self.SeleccionMultiple(consulta)
    #Traduce consultas con una sola sentencia de selección
    def SeleccionSimple(self,consulta):
        consulta = consulta.replace("PI","select ")
        nombre_sel = consulta[:consulta.find("SE")-1]
        consulta = consulta.replace(nombre_sel,"")
        consulta = consulta[1:-1]
        nombre_cond = consulta[consulta.find("SE"):consulta.find("(")]
        nombre_cond = nombre_cond.replace("SE"," where ")
        tabla = consulta[consulta.find("("):]
        #print(nombre_sel+" from "+tabla+nombre_cond+";")
        return(nombre_sel+" from "+tabla+nombre_cond+";")
    #Traduce consultas con más de una sentencia de selección
    def SeleccionMultiple(self, consulta):
        consulta = consulta.replace("PI","select ")
        nombre_proyeccion = consulta[:consulta.find("SE")-1]
        consulta = consulta.replace(nombre_proyeccion,"")
        nombre_seleccion = consulta.replace(")","")
        tablas = consulta[:consulta.find("SE"):-1]
        selecciones = []
        aux = ""
        for i in nombre_seleccion:
            if(i != "("):
                aux +=i
            elif("SE" in aux):
                aux = aux.replace("SE","")
                selecciones.append(aux)
                aux = ""
        for i in selecciones:
            consulta = consulta.replace(i,"")
        selecciones = " AND ".join(selecciones)
        tablas = consulta.replace("(","")
        tablas = tablas.replace(")","")
        tablas = tablas.replace("SE","")
        if("EQUIS" in tablas):
            tablas = tablas.replace("EQUIS",",")
        #print(nombre_proyeccion+" from "+tablas +" where "+selecciones+";")
        return(nombre_proyeccion+" from "+tablas +" where "+selecciones+";")
