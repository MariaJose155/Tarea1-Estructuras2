#Universidad de Costa Rica
#Estructuras de computadoras digitales II - IE0521
#María José Arce Marín B60561
#maria.arcemarin@ucr.acr.cr

#librerias utilizadas
import numpy as np
from predictorBinomial import tamanoUPC
from predictorBinomial import contador
from predictorBinomial import vectam
from predictorBinomial import actualizacionbth
from predictorBinomial import imprimir
import sys

#METODO XOR
#es el metodo destinado a hacer una xor con la direccion PC y la historia
#le ingresan como paramtros PC y la historia
#retorna xoor que es un valor entero de 0-3 

def xor(uPC,historia):
        entero=int(historia)
        entero2 = int(uPC)
        xor = str(entero^entero2)
        xoor = tamanoUPC(xor)
        return xoor

#METODO HISTORIAA
#es el metodo destinado a apartir de la direccion y letra
# dar un valor a la historia (como un ght)  
# recibe como parametros la direccion y la letra
# retorna la direccion en entero  
def Historiaa(direccion,letra):
    contador = direccion
    dirr = 0
    if letra == 'N\n':
        if contador == 0:
            dirr = 0
        elif  contador == 1:
            dirr = 0
        elif contador == 2:
            dirr = 1
        elif contador == 3:
            dirr = 2
    elif letra == 'T\n':
        if contador == 0:
            dirr = 1
        elif  contador == 1:
            dirr = 2
        elif contador == 2:
            dirr = 3
        elif contador == 3:
            dirr = 3
    return dirr
#METODO HISTORIAGLOBAL
#es el metodo destinado a predecir con un predictor de historia global
#recibe como parametros s,bp, gh ph (esto debido a que se necesita para imprimir la informacion)
#retorna el porcentaje de de prediccion correctas
def predictorHistoriaGlobal(s,bp,gh,ph):
    #bth
    entradasTabla = 2**s
    tabla = [0]*entradasTabla #inicializamos tabla con el tamano de entradas que el usuario desee ademas se inicializa en el estado strong not taken
    #inicializamos contadores
    prediccionCorrectaT = 0
    prediccionCorrectaN = 0
    prediccionIncorrectaT = 0
    prediccionIncorrectaN = 0
    #rango del archivo
    rango = vectam()
    Historia = 0#iniciliazamos en 0
    for r in range(rango):#recorremos el archivo
        linea = sys.stdin.readline() #leemos linea por linea
        if linea == "":
            break#si no tiene nada entonces termina el programa
        else:
            recorte = linea.split(" ") #recortamos c/linea al ver un espacio
            #entonces la posicion 0 sera pc y la posicion 1 letra
            valorPC = recorte[0]
            valorLetra = recorte[1]
            direccion = xor(valorPC,Historia)
            prediccion = contador(direccion,0)
            #verificamos si la prediccion es igual a la letra en la cola
            if prediccion == 'N\n':
            
                if prediccion == valorLetra:
                
                    prediccionCorrectaN = prediccionCorrectaN + 1 #aumentamos el contados
                    Historia = Historiaa(direccion,valorLetra)##nos dice como va la tabla ght
                else:
                
                    prediccionIncorrectaN = prediccionIncorrectaN +1#aumentamos el contador
                    Historia = Historiaa(direccion,valorLetra)#nos dice como va la tabla ght
            elif prediccion == 'T\n':
                
                if prediccion == valorLetra:
                    
                    prediccionCorrectaT = prediccionCorrectaT + 1#aumentamos el contador
                    Historia = Historiaa(direccion,valorLetra)#nos dice como va la tabla gth
                else:
                    
                    prediccionIncorrectaT = prediccionIncorrectaT + 1#aumentamos el contador
                    Historia = Historiaa(direccion,valorLetra)#nos dice como va la tabla gth
            actualizacionbth(uPC,letra,tabla)#actualizamos la bth ingresando la direccion optenida de la xor y la letra actual y la tabla que al puro inicio es inicializada en 0 
    mul = (prediccionCorrectaT + prediccionCorrectaN)*100
    porcentaje = mul/rango#encontramos el % de predicciones correctas
    imprimir(rango,prediccionCorrectaT,prediccionCorrectaN ,prediccionIncorrectaT,prediccionIncorrectaN,s,bp,gh,ph,porcentaje)
    return porcentaje#retornamos porcentaje

       


        
