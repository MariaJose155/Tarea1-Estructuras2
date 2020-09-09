#Universidad de Costa Rica
#Estructuras de computadoras digitales II - IE0521
#María José Arce Marín B60561
#maria.arcemarin@ucr.acr.cr

#librerias utilizadas
from predictorBinomial import predictorBimonal
from predictorGlobal import predictorHistoriaGlobal
from predictorPrivado import predictorHistoriaPrivada
from predictorTorneo import predictorTorneo
from sys import argv
import sys
from os import remove
#argumentos de consola
scrip,arg1,arg2,arg3,arg4 = argv

s = int(arg1) #Deber ser mayor a 1
bp = int(arg2)
gh = int(arg3)
ph = int(arg4)
#menu
if bp == 1:
    predictorBimonal(s,bp,gh,ph)
    
elif bp == 2:
    predictorHistoriaGlobal(s,bp,gh,ph)
  
elif bp == 3:
    predictorHistoriaPrivada(s,bp,gh,ph)
    
elif bp == 4:
    predictorTorneo(s,bp,gh,ph)
    
 




