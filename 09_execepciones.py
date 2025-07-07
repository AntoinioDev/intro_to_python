"""
las excepciones se usan en los bloques de tu codigo cuando hay un error
y  en vez de que tu app se cierre
"""

try: # este hace que el bloque dentro de ello se ejecute y pase por un flujo para verificarlo
    print("DIVISOR") # titulo
    numerador=int(input("ingrese el numerador: ")) # le pasamos el primer parametro
    denominador=int(input("ingrese el denominador: ")) # le pasamos el suiguiente parametro
    print(f"el resultado de {numerador}/{denominador} ={numerador/denominador}") # print al resultado
except ZeroDivisionError: # execpt hace que verifique el codigo y si el error es zerodivisioinerror pasa 
    print("ERROR division entre 0") # imprime el error
except ValueError: # y si no es zero division error pasas a verificar si es value error
    print("ERROR de valores no validos") # imprime lo dentro del print
except Exception as e: # y si solo me detecta un error y no es de los suiguientes, captura la execpcioin y lo guarda en e
    print(f"ERROR: {e}") # printea el error y como ya capturamos el nombre en e solo lo printeamos
else: # else tambie se utiliza pasa cuando el programa funaciona
    print("se ejcuto correctamente") # print ael mensaje
finally: # siempre se ejecuta este bloque
    print("Programa finalizado") # print a lo ultimo