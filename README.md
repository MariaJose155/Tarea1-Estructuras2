Universidad de Costa Rica

Estructuras de computadoras digitales II - IE0521

María José Arce Marín B60561

maria.arcemarin@ucr.acr.cr

# INTRODUCCIÓN
Código para predecir por medio de diferentes métodos como se comporta el archivo adjunto
# Como correrlo
gunzip -c branch-trace-gcc.trace.gz|python3 main.py s bp gh ph
# Especificaciones importantes
bp = 1 implica el método bimodal

bp = 2 implica el método global

bp = 3 implica el método privado

bp = 4 implica el método torneo
