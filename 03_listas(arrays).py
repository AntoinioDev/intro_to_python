"""
una lista es un conjusto de datos en los que puedes remover agregar
añadir elementos en un indice propuesto
"""
### list ###

my_list=["manzana","fresa","platano","kiwi ","uva",]
print(my_list)
print(my_list[1])#print a segundo elemento "fresa"
print(my_list[-1])# print al ultimo con numeros negativos
my_list[3]="gta v|" # reemplazamos por un indice 

print(my_list) # lista print
#
my_list.append("diego xd") #agregamos un elemento a la lista
##
print(my_list)# print a lo ya añadido 'diego xd'
##
my_list.remove("uva") # removiendo en la lista 'uva'
#####
print("verfificando el remove a la fruta 'uva' ") #mensajito
print(my_list) # print a my list pero esta vez sin uva
####

vegetables=["cebolla","papa","zanahoria"] # lista de vegetales
items_concatenados= my_list + vegetables # objetos concatenados(listas)
print(items_concatenados)
####
my_list_tasks=["developed","designer","lavar trastes"]
my_list_tasks.insert(1,"hablar con chatgpt") # insertamos un nuevo elemento en elindice 1
print(my_list_tasks) # 
###
my_list_tasks.pop(1)
print(my_list_tasks) #
print(my_list_tasks.pop(2)) # pop es mejor para borrzr el ultimo elmento de una lissta
print(my_list_tasks)

###
del my_list_tasks[1] # es como un remove pero con el indice
print(my_list_tasks)
###
list_pets=["max","boris","firulais"]
list_pets.reverse() # pone el ultimo como el primero
print(list_pets) 
list_pets.sort() # busca crear un orden dependiendo de su tipo string,int asi de mayor menor
print(list_pets)
my_new_list_pets=list_pets.copy() # copia la lista de list_pets y lo pasa a my_new_list_pets
##
list_pets.clear() # limpia dentro de la lista
print(list_pets) # print a la lista vacia porque le hicimos un clear
print(my_new_list_pets) # qui esta la lista ya que le hicimos un copy y es lo nombramos a esta variable