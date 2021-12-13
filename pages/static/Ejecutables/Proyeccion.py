from re import findall
class Proyeccion:
    #Constructor vacío
    def __init__(self):
        pass
    #Traduce consultas que requieren unión sin ninguna especificación
    def producto_cartesiano(self, consulta):
        consulta = consulta.replace("EQUIS",",")
        print(consulta)
        tablas = consulta.split(",")
        tablas = set(tablas)
        print(type(tablas))
        tablas = str(tablas)
        tablas = tablas.replace("'","")
        tablas = tablas.replace("{","")
        print(tablas)
        if tablas.count("}") == 1:
            tablas = tablas.replace("}","")
            consulta = "SELECT * from " + tablas + ";"
        else:
            tablas = tablas.replace("}",",")
            consulta = "SELECT * from " + tablas + ";"
        return consulta
    #Traduce consultas que solo tienen la sentencia de proyección
    def reemplazar_pi(self,consulta):
        consulta = consulta.replace("PI_1","SELECT ")
        consulta = consulta.replace("("," from (")
        consulta = consulta+";"
        if("EQUIS" in consulta):
            consulta = consulta.replace("EQUIS",",")
        return consulta
    #Traduce consultas con sentencias de proyeción y diferencia
    def pi_diferencia(self, consulta):
        aux = consulta.find("-")
        primera_sentencia = consulta[:aux]
        segunda_sentencia = consulta[aux+1:]
        primera_sentencia = self.reemplazar_pi(primera_sentencia)
        primera_sentencia = primera_sentencia.replace(";","")
        segunda_sentencia = self.reemplazar_pi(segunda_sentencia)
        return (primera_sentencia + " MINUS " + segunda_sentencia)
    #Analiza si la sentencia tiene sentencias de proyección y selección o sentencias proyección y más de una selección
    def ProyeccionYSeleccion(self, consulta):
        if(len(findall("SE_1",consulta)) == 1):
            return self.SeleccionSimple(consulta)
        elif(len(findall("SE_1",consulta))>1):
            return self.SeleccionMultiple(consulta)
    #Traduce consultas con una sola sentencia de selección
    def SeleccionSimple(self,consulta):
        consulta = consulta.replace("PI_1","SELECT ")
        consulta = consulta.replace("^^"," OR ")
        consulta = consulta.replace("^"," AND ")
        nombre_sel = consulta[:consulta.find("SE_1")-1]
        consulta = consulta.replace(nombre_sel,"")
        consulta = consulta[1:-1]
        nombre_cond = consulta[consulta.find("SE_1"):consulta.find("(")]
        nombre_cond = nombre_cond.replace("SE_1"," where ")
        tabla = consulta[consulta.find("("):]
        if "EQUIS" in tabla:
            tabla = tabla.replace("EQUIS",",")
        return(nombre_sel+" from "+tabla+nombre_cond+";")
    #Traduce consultas con más de una sentencia de selección
    def SeleccionMultiple(self, consulta):
        consulta = consulta.replace("PI_1","SELECT ")
        nombre_proyeccion = consulta[:consulta.find("SE_1")-1]
        consulta = consulta.replace(nombre_proyeccion,"")
        nombre_seleccion = consulta.replace(")","")
        tablas = consulta[:consulta.find("SE_1"):-1]
        selecciones = []
        aux = ""
        for i in nombre_seleccion:
            if(i != "("):
                aux +=i
            elif("SE_1" in aux):
                aux = aux.replace("SE_1","")
                selecciones.append(aux)
                aux = ""
        for i in selecciones:
            consulta = consulta.replace(i,"")
        selecciones = " AND ".join(selecciones)
        tablas = consulta.replace("(","")
        tablas = tablas.replace(")","")
        tablas = tablas.replace("SE_1","")
        if("EQUIS" in tablas):
            tablas = tablas.replace("EQUIS",",")
        return(nombre_proyeccion+" from "+tablas +" where "+selecciones+";")

    def UnionTablas(self, consulta):
        if "UNION" in consulta:
            tablas = []
            tablas = consulta.split("UNION")
            sentencia = ""
            contador = 0
            for tabla in tablas:
                if contador==0:
                    sentencia= "SELECT * from " + tabla
                    contador=1
                else:
                    sentencia+= " UNION ALL SELECT * from " + tabla
            sentencia = sentencia+";"
        if "-" in consulta:
            tablas = consulta.split("-")
            tablas = set(tablas)
            print(tablas)
            if len(tablas) == 1:
                sentencia = "vacio"
            else:
                sentencia = 'null'
        return sentencia
