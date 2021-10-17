class Seleccion:
    #Constructor vacío
    def __init__(self):
        pass
    #Traduce las consultas con sentencias que contienen una sola selección
    def reemplazar_se(self,consulta):
        consulta = consulta.replace("SE"," WHERE ")
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
