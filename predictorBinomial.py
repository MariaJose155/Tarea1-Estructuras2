#Universidad de Costa Rica
#Estructuras de computadoras digitales II - IE0521
#María José Arce Marín B60561
#maria.arcemarin@ucr.acr.cr

#librerias utilizadas
import numpy as np
import patoolib
import os
import sys

#METODO VECTAM
#es un metodo para ver el tamano del archivo.trace
#no recibe parametros
#retorna el numero de filas del archico.trace
def vectam():
    vec = 16416279
    return vec


#sabemos lo siguiente
#significado = binario = decimal
#STRONG NOT TAKEN = 00 = 0
#WEAK NOT TAKEN = 01 = 1
#WEAK TAKEN = 10 = 2
#STRONG TAKEN = 11 = 3

#METODO CONTADOR
#metodo donde se hacen las predicciones por medio de un contador
#recibe como parametro uPC que es el que nos dice si se trata de un 
#strong not taken, strong taken, weak not taken, weak taken
#retorna la prediccion como T o N
def contador(uPC,tipo):
    contador = uPC
    if tipo == 0:
        if contador == 3:
            return 'T\n'
        elif contador == 1:
            return 'N\n'
        elif contador == 2:
            return 'T\n'
        elif contador == 0:
            return 'N\n'
    elif tipo == 1:
        if contador == 0:   
            return 'P'
        elif contador == 1:
            return 'P'
        elif contador == 2:       
            return 'G'
        elif contador == 3:       
            return 'G'
#METODO ACTUAILIZACION1
#es un sub-metodo de metodo actualizacion que solo nos indica que uPC es 0
# donde uPC es numero que nos dice si se trata de un 
#strong not taken, strong taken, weak not taken, weak taken
#recibe como parametro uPC
#retorna uPC

def actualizacion1(uPC):
    uPC = 0
    return uPC
#METODO ACTUAILIZACION2
#es un sub-metodo de metodo actualizacion que solo nos indica que uPC es 1
# donde uPC es numero que nos dice si se trata de un 
#strong not taken, strong taken, weak not taken, weak taken
#recibe como parametro uPC
#retorna uPC
def actualizacion2(uPC):
    uPC = 1
    return uPC
#METODO ACTUAILIZACION3
#es un sub-metodo de metodo actualizacion que solo nos indica que uPC es 2
# donde uPC es numero que nos dice si se trata de un 
#strong not taken, strong taken, weak not taken, weak taken 
#recibe como parametro uPC
#retorna uPC
def actualizacion3(uPC):
    uPC = 2
    return uPC
#METODO ACTUAILIZACION4
#es un sub-metodo de metodo actualizacion que solo nos indica que uPC es 3
# donde uPC es numero que nos dice si se trata de un 
#strong not taken, strong taken, weak not taken, weak taken
#recibe como parametro uPC
#retorna uPC
def actualizacion4(uPC):
    uPC = 3
    return uPC
#METODO ACTUALIZACION
#es un metod que verifica que nos ingresa como letra y que una vez 
#conociendo que es letra (T o N) revisa el valor del contador = uPC
#donde uPC es numero que nos dice si se trata de un 
#strong not taken, strong taken, weak not taken, weak taken
#donde letra es T o N
#recibe como parametro uPC,letra
#no retorna nada porque sus metodos internos lo hacen
def actualizacionbth(uPC,letra,tabla):
    contador = tabla[uPC]
    tamano = len(tabla)
    for t in range(tamano):
        if letra == 'N\n':
            if contador == 0:
                actualizacion1(uPC)
            elif  contador == 1:
                actualizacion1(uPC)
            elif contador == 2:
                actualizacion2(uPC)
            elif contador == 3:
                actualizacion3(uPC)
        elif letra == 'T\n':
            if contador == 0:
                actualizacion2(uPC)
            elif  contador == 1:
                actualizacion3(uPC)
            elif contador == 2:
                actualizacion4(uPC)
            elif contador == 3:
                actualizacion4(uPC)
    
#METODO TAMANOUPC
#es un metodo verifica uPC por uPC para encontrar en binario si sus ultimos 2 bits son
#00 01 10 11 
#recibe como parametro uPC o la direccion PC
# donde uPC es numero que nos dice si se trata de un 
#strong not taken, strong taken, weak not taken, weak taken, es 0 
#retorna un numero que equivale a 00 01 10 11 pero en decimal osea 0 1 2 3 segun sea el caso
def tamanoUPC(uPC):
    entero = int(uPC)#hacemos que la direccion entre como un entero
    binario = bin(entero)#encontramos el binario del entero
    num = str(binario) #hacemos ese binario un string
    tamano = len(num)#encontramos el tamano del string
    uno = num[tamano-2]#encontramos el penultimo valor 0 o 1
    dos = num[tamano-1]#encontramos el ultimo valor 0 o 1
    nuevo = uno + dos #concatenamos
    nuevoo = 0 #inicializamos variable
    #hacemos condiciones para saber que retornar en entero apartir de un numero en binario de 2 bits
    if nuevo == '00':
        nuevoo = 0
    elif nuevo == '01':
        nuevoo = 1
    elif nuevo == '10':
        nuevoo = 2
    elif nuevo == '11':
        nuevoo = 3
    else:
        return "error"
   
    return nuevoo

#METODO PREDICTORBINOMIAL
#es el metodo destinado a predecir con un predictor de bimodal
#recibe como parametros s,bp, gh ph (esto debido a que se necesita para imprimir la informacion)
#retorna el porcentaje de de prediccion correctas
def predictorBimonal(s,bp,gh,ph):
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
    for r in range(rango): #recorremos el archivo
        linea = sys.stdin.readline() #leemos linea por linea
        if linea == "":
            break #si no tiene nada entonces termina el programa
        else:
            recorte = linea.split(" ") #recortamos c/linea al ver un espacio
            #entonces la posicion 0 sera pc y la posicion 1 letra
            valorPC = recorte[0]#guardamos la direccion en valorPC
            valorLetra = recorte[1]#guardamos la salida T o N en valorLetra

            uPC = tamanoUPC(valorPC) #encontramos los ultimos 2 bits 
            prediccion = contador(uPC,0)#guardamos prediccion
            #verificamos si la prediccion es igual a la letra en la cola
            if prediccion == 'N\n':
                if prediccion == valorLetra:
                    prediccionCorrectaN = prediccionCorrectaN + 1 #aumentamos contador
                
                else:
                    prediccionIncorrectaN = prediccionIncorrectaN +1#aumentamos contador
                
            elif prediccion == 'T\n':
                if prediccion == valorLetra:
                    prediccionCorrectaT = prediccionCorrectaT + 1#aumentamos contador
                
                else:
                    prediccionIncorrectaT = prediccionIncorrectaT + 1#aumentamos contador
              
            actualizacionbth(uPC,valorLetra,tabla) #actualizamos la bth ingresando la direccion optenida de la xor y la letra actual y la tabla que al puro inicio es inicializada en 0
    mul = (prediccionCorrectaT + prediccionCorrectaN)*100
    porcentaje = mul/rango#encontramos el % de predicciones correctas
    imprimir(rango,prediccionCorrectaT,prediccionCorrectaN ,prediccionIncorrectaT,prediccionIncorrectaN,s,bp,gh,ph,porcentaje)
    return porcentaje#retornamos el porcentaje
#METODO IMPRIMIR
#es el metodo destinado a desplegar toda la informacion obtenida
# recibe como parametos: rango,prediccionCorrectaT,prediccionCorrectaN ,prediccionIncorrectaT,prediccionIncorrectaN,s,bp,gh,ph,porcentaje
#no retorna nada
def imprimir(rango,prediccionCorrectaT,prediccionCorrectaN ,prediccionIncorrectaT,prediccionIncorrectaN,s,bp,gh,ph,porcentaje):
    print ("______________________________________________________")
    print ("Prediction parameters")
    print ("______________________________________________________")
    lista(bp)
    print ("BHT size:                                         " + str(s))
    print ("Global history register size:                     " + str(gh))
    print ("Private history register size:                    " + str(ph))
    print ("______________________________________________________")
    print ("Simulation results")
    print ("______________________________________________________")
    print ("Number of branch:                                 " + str(rango))
    print ("Number of correct prediction of taken branches:   " + str(prediccionCorrectaT))
    print ("Number of incorrect prediction of taken branches: " + str(prediccionIncorrectaT))
    print ("Correct prediction of not taken branches:         " + str(prediccionCorrectaN))
    print ("Incorrect prediction of not taken branches:       " + str(prediccionIncorrectaN))
    print ("Percentage of correct predictions:       " + str(porcentaje))
    ("______________________________________________________")
#METODO LISTA
#es el metodo destinado para apartir de bp imprimir que predictor es
def lista(bp):
    if (bp == 1):
        print ("Branch prediction type: predictor Bimodal")
    elif (bp == 2):
        print ("Branch prediction type: predictor Global")
    elif (bp == 3):
        print ("Branch prediction type: predictor Privado")
    elif (bp == 4):
        print ("Branch prediction type:  predictor Torneo")



    







