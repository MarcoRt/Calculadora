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
        if("EQUIS" in consulta):
            consulta = consulta.replace("EQUIS",",")
        #print("1" + consulta)
        return consulta
    #Traduce consultas con sentencias de proyeción y diferencia
    def pi_diferencia(self, consulta):
        aux = consulta.find("-")
        primera_sentencia = consulta[:aux]
        segunda_sentencia = consulta[aux+1:]
        primera_sentencia = self.reemplazar_pi(primera_sentencia)
        primera_sentencia = primera_sentencia.replace(";","")
        segunda_sentencia = self.reemplazar_pi(segunda_sentencia)
        #print("2" + primera_sentencia + " MINUS " + segunda_sentencia)
        return (primera_sentencia + " MINUS " + segunda_sentencia)
    #Analiza si la sentencia tiene sentencias de proyección y selección o sentencias proyección y más de una selección
    def ProyeccionYSeleccion(self, consulta):
        if(len(findall("SE",consulta)) == 1):
            return self.SeleccionSimple(consulta)
        elif(len(findall("SE",consulta))>1):
            return self.SeleccionMultiple(consulta)
    #Traduce consultas con una sola sentencia de selección
    def SeleccionSimple(self,consulta):
        consulta = consulta.replace("PI","select ")
        consulta = consulta.replace("^^"," OR ")
        consulta = consulta.replace("^"," AND ")
        nombre_sel = consulta[:consulta.find("SE")-1]
        consulta = consulta.replace(nombre_sel,"")
        consulta = consulta[1:-1]
        nombre_cond = consulta[consulta.find("SE"):consulta.find("(")]
        nombre_cond = nombre_cond.replace("SE"," where ")
        tabla = consulta[consulta.find("("):]
        if "EQUIS" in tabla:
            tabla = tabla.replace("EQUIS",",")
        #print("3" + nombre_sel+" from "+tabla+nombre_cond+";")
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
        #print("4" + nombre_proyeccion+" from "+tablas +" where "+selecciones+";")
        return(nombre_proyeccion+" from "+tablas +" where "+selecciones+";")

    def UnionTablas(self, consulta):
        if "UNION" in consulta:
            tablas = []
            tablas = consulta.split("UNION")
            print("Soy las tablas: ",tablas)
            sentencia = ""
            contador = 0
            for tabla in tablas:
                if contador==0:
                    sentencia= "select * from " + tabla
                    contador=1
                else:
                    sentencia+= " UNION ALL select * from " + tabla
            sentencia = sentencia+";"
        print("Soy la sentencia: ",sentencia)
        return sentencia
