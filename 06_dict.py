def mensaje(op,key,new_mensage):
    my_dict={
        1:"hola mundo",
        2:"hola python",
        3:"hola user"
    }
    my_dict[key]=new_mensage

    return my_dict[op],my_dict
    #return my_dict.get(op)   
op=int(input("ingrese el mesaje quiere imprimir:\n[1]hola mundo\n[2]hola python\n[3]hola user \n :"))
key=input("ingrese el clave del mendaje: ")
new_mensaje=input("ingrese el mensaje que quiere que salga: ")
print(f"el mesaje que elejiste es: {mensaje(op,key,new_mensaje)}")

print("otro dict")

my_dict={
        1:"hola mundo",
        2:"hola python",
        3:"hola user"
    }
print(my_dict)

for clave,valor in my_dict.items():
    print(f"{clave}:{valor}")

print("\n otra forma de recorrer los valores del diciionario: \n")
for clave in my_dict:
    print(f"{clave}:{my_dict[clave]}")