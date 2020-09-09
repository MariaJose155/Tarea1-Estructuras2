#librerias utilizadas
import numpy as np
from predictorBinomial import tamanoUPC
from predictorBinomial import contador
from predictorBinomial import vectam
from predictorBinomial import actualizacionbth
from predictorGlobal import xor
from predictorGlobal import Historiaa
from predictorBinomial import imprimir
import sys
#METODO PREDICTORHISTORIAPRIVADA
#es el metodo destinado a predecir con un predictor de historia privada
#recibe como parametros s,bp, gh ph (esto debido a que se necesita para imprimir la informacion)
#retorna el porcentaje de de prediccion correctas
def predictorHistoriaPrivada(s,bp,gh,ph):
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
    Historia = 0 #inicializamos en 0 
    for r in range(rango):#recorremos el archivo
        linea = sys.stdin.readline() #leemos linea por linea el zip
        if linea == "":
            break #si no tiene nada entonces termina el programa
        else:
            recorte = linea.split(" ") #recortamos c/linea al ver un espacio
            #entonces la posicion 0 sera pc y la posicion 1 letra
            valorPC = recorte[0] #guardamos la direccion en valorPC
            valorLetra = recorte[1] #guardamos la salida T o N en valor letra
            direccion = xor(valorPC,Historia) #hacemos una xor con el valor del PC y la historia
            prediccion = contador(direccion,0) #guadamos la prediccion
            #verificamos si la prediccion es igual a la letra en la cola
            if prediccion == 'N\n':
            
                if prediccion == valorLetra:
                
                    prediccionCorrectaN = prediccionCorrectaN + 1#aumentamos contador
                    Historia = Historiaa(direccion,valorLetra) #nos dice como va la tabla pht
                else:
                
                    prediccionIncorrectaN = prediccionIncorrectaN +1#aumentamos contador
                    Historia = Historiaa(direccion,valorLetra)#nos dice como va la tabla pht
            elif prediccion == 'T\n':
                
                if prediccion == valorLetra:
                    
                    prediccionCorrectaT = prediccionCorrectaT + 1#aumentamos contador
                    Historia = Historiaa(direccion,valorLetra)#nos dice como va la tabla pht
                else:
                    
                    prediccionIncorrectaT = prediccionIncorrectaT + 1#aumentamos contador
                    Historia = Historiaa(direccion,valorLetra)#nos dice como va la tabla pht
            actualizacionbth(uPC,letra,tabla) #actualizamos la bth ingresando la direccion optenida de la xor y la letra actual y la tabla que al puro inicio es inicializada en 0
    mul = (prediccionCorrectaT + prediccionCorrectaN)*100
    porcentaje = mul/rango #encontramos el % de predicciones correctas
    imprimir(rango,prediccionCorrectaT,prediccionCorrectaN ,prediccionIncorrectaT,prediccionIncorrectaN,s,bp,gh,ph,porcentaje)
    return porcentaje #retornamos el porcentaje
