#Universidad de Costa Rica
#Estructuras de computadoras digitales II - IE0521
#María José Arce Marín B60561
#maria.arcemarin@ucr.acr.cr

#librerias utilizadas
import numpy as np
from predictorGlobal import xor
from predictorBinomial import actualizacionbth
from predictorBinomial import contador
from predictorBinomial import vectam
from predictorGlobal import Historiaa
from predictorBinomial import imprimir
import sys
#METODO PREDICTORTORNEO
#es el metodo destinado a predecir con un predictor de torneo
#recibe como parametros s,bp, gh ph (esto debido a que se necesita para imprimir la informacion)
#retorna el porcentaje de de prediccion correctas
def predictorTorneo(s,bp,gh,ph):
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
    Historia1 = 0#iniciliazamos en 0
    Historia2 = 0#inicializamos en 0
    for r in range(rango):#recorremos el archivo
        linea = sys.stdin.readline() #leemos linea por linea
        if linea == "":
            break#si no tiene nada entonces termina el programa
        else:
            recorte = linea.split(" ") #recortamos c/linea al ver un espacio
            #entonces la posicion 0 sera pc y la posicion 1 letra
            valorPC = recorte[0]#guardamos la direccion en valorPC
            valorLetra = recorte[1]#guardamos la salida T o N en valorLetra
            #verificamos si la prediccion es igual a la letra 
            if valorLetra == 'T\n':
                xorG = xor(valorPC,Historia1)#hacemos la xor para el predictor global
                prediccionG = contador(xorG,0)#hacemos una prediccion para el predictor global de T o N
                xorP = xor(valorPC,Historia2)#hacemos la xor para el predictor privado
                prediccionP = contador(xorP,0)#hacemos una prediccion para el predictor privado  de T o N
            elif valorLetra == 'N\n':
                xorG = xor(valorPC,Historia1)#hacemos la xor para el predictor global
                prediccionG = contador(xorG,0)#hacemos una prediccion para el predictor global de T o N
                xorP = xor(valorPC,Historia2)#hacemos la xor para el predictor privado
                prediccionP = contador(xorP,0)#hacemos una prediccion para el predictor privado de T o N
            actualizacionbth(xorG,valorLetra)#actualizamos la tabla bth 
            actualizacionbth(xorP,valorLetra)#actualizamos la tabla bth 
            prediccion = contador(valorPC,1) ##hacemos una prediccion de P o G
            Historia1 = Historiaa(xorG,valorLetra)#encontramos la historia del predictor global
            Historia2 = Historiaa(xorP,valorLetra)#encontramos la historia del predictor privado
            #entonces verificamos el valor de prediccion    
            if prediccion == 'G':
                if prediccionG == 'N\n':
                    if prediccionG == valorLetra:
                        prediccionCorrectaN = prediccionCorrectaN + 1 #aumentamos el contador
                
                    else:
                        prediccionIncorrectaN = prediccionIncorrectaN +1 #aumentamos el contador
                
                elif prediccionG == 'T\n':
                    if prediccionG == valorLetra:
                        prediccionCorrectaT = prediccionCorrectaT + 1#aumentamos el contador
                
                    else:
                        prediccionIncorrectaT = prediccionIncorrectaT + 1#aumentamos el contador
                if prediccionP == 'N\n':
                    if prediccionP == valorLetra:
                        prediccionCorrectaN = prediccionCorrectaN + 1 #aumentamos el contador
                
                    else:
                        prediccionIncorrectaN = prediccionIncorrectaN +1 #aumentamos el contador
                
                elif prediccionP == 'T\n':
                    if prediccionP == valorLetra:
                        prediccionCorrectaT = prediccionCorrectaT + 1#aumentamos el contador
                
                    else:
                        prediccionIncorrectaT = prediccionIncorrectaT + 1#aumentamos el contador
                actualizacionbth(xorG,valorLetra,tabla)
            elif prediccion  == 'P':
                if prediccionG == 'N\n':
                    if prediccionG == valorLetra:
                        prediccionCorrectaN = prediccionCorrectaN + 1 #aumentamos el contador
                
                    else:
                        prediccionIncorrectaN = prediccionIncorrectaN +1 #aumentamos el contador
                
                elif prediccionG == 'T\n':
                    if prediccionG == valorLetra:
                        prediccionCorrectaT = prediccionCorrectaT + 1#aumentamos el contador
                
                    else:
                        prediccionIncorrectaT = prediccionIncorrectaT + 1#aumentamos el contador
                if prediccionP == 'N\n':
                    if prediccionP == valorLetra:
                        prediccionCorrectaN = prediccionCorrectaN + 1 #aumentamos el contador
                
                    else:
                        prediccionIncorrectaN = prediccionIncorrectaN +1 #aumentamos el contador
                
                elif prediccionP == 'T\n':
                    if prediccionP == valorLetra:
                        prediccionCorrectaT = prediccionCorrectaT + 1#aumentamos el contador
                
                    else:
                        prediccionIncorrectaT = prediccionIncorrectaT + 1#aumentamos el contador
                actualizacionbth(xorP,valorLetra,tabla)#actualizamos tabla bth
               
    mul = (prediccionCorrectaT + prediccionCorrectaN)*100
    porcentaje = mul/rango#encontramos % de predicciones correctas
    imprimir(rango,prediccionCorrectaT,prediccionCorrectaN ,prediccionIncorrectaT,prediccionIncorrectaN,s,bp,gh,ph,porcentaje)
    return porcentaje#retornamos porcentaje


            


