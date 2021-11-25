import Proyeccion
class Seleccion:
    #Constructor vacío
    def __init__(self):
        pass
    #Traduce las consultas con sentencias que contienen una sola selección
    def reemplazar_se(self,consulta):
        consulta = consulta.replace("SE_1"," WHERE ")
        consulta = consulta.replace("^^"," OR ")
        consulta = consulta.replace("^"," AND ")
        inicio = consulta.find("(")
        final = consulta.find(")")
        aux = consulta[inicio:final+1]
        if(">" in aux or "<" in aux):
            inicio = final+1
            aux = consulta[inicio:]
        consulta = consulta.replace(aux,"\0")
        aux = aux.replace("EQUIS",",")
        consulta = "select * from "+aux+consulta+";"
        #consulta = consulta+";"
        return consulta
    #Traduce las consultas con sentencias que tienen selección y diferencia
    def reemplazar_minus(self, consulta):
        aux = consulta.find("-")
        primera_sentencia = consulta[:aux]
        segunda_sentencia = consulta[aux+1:]
        primera_sentencia = self.reemplazar_se(primera_sentencia)
        primera_sentencia = primera_sentencia.replace(";","")
        segunda_sentencia = self.reemplazar_se(segunda_sentencia)
        print(primera_sentencia + " MINUS " + segunda_sentencia)
        return (primera_sentencia + " MINUS " + segunda_sentencia)
    def reemplazar_union_interseccion(self, consulta):
        pro = Proyeccion.Proyeccion()
        print("CONSULTA: ", consulta)
        if "UNION" in consulta:
            aux = consulta.index("UNION")
            primera_sentencia = consulta[:aux]
            segunda_sentencia = consulta[aux+5:]
            print("PRIMERA SENTENCIA: ", primera_sentencia)
            print("SEGUNDA SENTENCIA: ", segunda_sentencia)
            if "PI_1" in primera_sentencia and "SE_1" not in primera_sentencia:
                primera_sentencia = pro.reemplazar_pi(primera_sentencia)
            elif "PI_1" not in primera_sentencia and "SE_1" in primera_sentencia:
                primera_sentencia = self.reemplazar_se(primera_sentencia)
            elif "PI_1" in primera_sentencia and "SE_1" in primera_sentencia:
                primera_sentencia = pro.ProyeccionYSeleccion(primera_sentencia)
            if "PI_1" in segunda_sentencia and "SE_1" not in segunda_sentencia:
                segunda_sentencia = pro.reemplazar_pi(segunda_sentencia)
            elif "PI_1" not in segunda_sentencia and "SE_1" in segunda_sentencia:
                segunda_sentencia = self.reemplazar_se(segunda_sentencia)
            elif "PI_1" in segunda_sentencia and "SE_1" in segunda_sentencia:
                segunda_sentencia = pro.ProyeccionYSeleccion(segunda_sentencia)
            #primera_sentencia = self.reemplazar_se(primera_sentencia)
            primera_sentencia = primera_sentencia.replace(";","")
            #segunda_sentencia = self.reemplazar_se(segunda_sentencia)
            #print("PRIMERA SENTENCIA: ", primera_sentencia)
            #print("SEGUNDA SENTENCIA: ", segunda_sentencia)
            #print(primera_sentencia + " UNION " + segunda_sentencia)
            return primera_sentencia + " UNION " + segunda_sentencia
        else:
            aux = consulta.index("INTER")
            primera_sentencia = consulta[:aux]
            segunda_sentencia = consulta[aux+5:]
            primera_sentencia = self.reemplazar_se(primera_sentencia)
            primera_sentencia = primera_sentencia.replace(";","")
            segunda_sentencia = self.reemplazar_se(segunda_sentencia)
            return primera_sentencia + " INTERSECT " + segunda_sentencia +";"
