### bucles xd ###
"""
existen dos tipos de bucles 
los for y while uno es diferente de otro asi 
como ventajas y desventajas
"""
### for ### funcion con iteador y con dato o de donde a donde(lo asignamos o el usuario lo asigna)
for i in range(1,11): #aqui le estamos diciendo que i vale 0 pero range define su recorrido por lo tanto va de 1 al 10 python no cuenta el ultimo
        print(i)       #y el printimprime los numeros del 1 al 10

## for ### con un dato del usurio o que nosotro le pasamos
suma_total=0  #aqui validamos la suma para que el programa no pete xd
n=int(input("ingrese numero asta donde quiera sumar numeros: ")) # dato de recorrido 
for i in range(1,n+1): #le decimos que i = 1 y recorrera al dato solicitado se le suma 1 por que python no cuenta el ultimo
        num=int(input(f"ingrese el numero a suma n.{i} :")) #le pedimos que ingre el numero a sumar las veces que decida el usuraio
        suma_total+=num # se le suma el numero la veces del iterador 
print(f"la suma de los numeros es: {suma_total}") #print a la suma fuera del for(si no hacemos haci lo imprime la veces del iterador)

### for ### con un dato que le pasamos(una,lista etc)
print("### for ### con un dato que le pasamos(una,lista etc)")
name="Antonio" #le nombramos una variable nombre dentro de comillas para que lo lea como un string
for i in name: #le decimos que desempaquete las letras de name
        print(i) #print a las letras de la variable pasada al for

"""
ahora se pueden usar dos sentecias de los bucles for 
y while para cerrar el bucle o saltar una parte 
""" 
print("### uso de break ###")       
### break ### con for 
for i in range (1,11): #se itera del 1 al 10 (el ultimo no lo cuenta python)
        print(i) #hacemos print a los numero del 1 al 10
        if i == 7: #preguntamos si i(el iterador)= 7 es igual a 7 
            print("se acabo el bucle el numero 7 fue hallado saliendo.....") #print un mesajito haceind que salimos del bucle
            break ## si es igual a 7 salimos del bucle
print("### uso de continue xd ###")
### continue ### con for
for i in range(1,15): # hasta el rango puessto
       if i == 13: # preguntamos si eng¡contro el numero 13 en el iterador
         print("el que lo lea es gay (yo no cuento no soy gay xd)") # en vez de print al numero 13 imprime este mensaje
         continue # como encontro el numero salta ese numero y pone el mensaje anterior
       print(i) #print a todos lo numeros sustituyendo a el numero 13
""""
whhile

"""
print("/// while funcion ///")
limite=int(input("ingrese un limite de repeticiones de hola mundo: ")) #limite de hasta donde quiere que se imprima hola mundo
iterador=0
while iterador<limite: #le decimimos mientras que el iterador sea menor a limite puesto por usario 
      print("hola mundo") #print a las veces puestas en el limite
      iterador+=1          #le sumamos al iterador 1 para que pueda llegar al numero puesto como limite
#### wnile complejo xd ###
print("/// while pero un poco mas complejo ///")
n= int(input("ingrese el numero a sumar(0 para terminar) : ")) # numeros a sumar
suma_num_ingresados=0 # hacemos que sum valga 0 y se rellene con el iterador 
while n!=0: # mienttras que sea diferente a 0 se suma a la variable sum
      n= int(input("ingrese el numero a sumar : ")) # numeros a evluar
      suma_num_ingresados+=n # se le va sumando a la suma los numeros ingresados
print(f"la suma de todo es : {suma_num_ingresados}") # print a la suma de los numeros ingresados

""""
uso del break con while 

"""
print("### uso del break en while ###") 
suma_break_while=0 # declaramos variable
while True : # lo hacemos que sea siempre verdadero(infinito)
      n= int(input("ingrese un numero para sumar (ingrese 0 para terminar la suma de los numeros): ")) # ingreso de numeros para la suma
      suma_break_while+=n # se le asigna a la suma los numeros ingresados
      if n== 0: # preguntamos si es igual a 0
            print(f"la suma de los numeros ingresados: {suma_break_while}")
            print("saliendo del programa.....") # print a un mesajito antes de salir 
            break # salimos del programa
