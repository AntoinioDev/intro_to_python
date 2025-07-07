"""
modulos ? que es? como funcoina? para que sirve?
basicamente es un archivo de python que contiene codigo reutilizable
"""
# Importar un modulo
import complemeto as m # importando el modulo completo
# from complemeto import suma, div, multiplicacion, prom # importando funciones especificas

suma = m.suma(5, 10)# m.suma(5, 10) # llamando a la funcion suma del modulo m
print(suma)# imprimiendo el resultado de la suma
div = m.div(10, 2)# llamando a la funcion div del modulo m
print(div)
multiplicacion = m.multiplicacion(5, 10)# llamando a la funcion multiplicacion del modulo m
print(multiplicacion)
num_alumnos=input("Ingrese el numero de alumnos: ")# convirtiendo el input a entero
m.prom(num_alumnos)


