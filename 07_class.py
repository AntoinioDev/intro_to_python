### class ###
"""
una clase se define coom si estuvieras
haciendo un objeto con sus caracteristicas
y funciones que puede realizar 
"""
#ejemplos
class MyCar: # aqui esta el nombre de mi clase (objeto)
    def __init__(self,marca,modelo): # ponemos sus caracteristicas(las variables que le pasemos)
      self.marca=marca # marca es igual a la variable que le pasemos
      self.modelo=modelo # modelo es igual a el parametro que le pasamos
      self.encendido=False # encendido se refiero aque esta apagado
      self.piloto_auto=False
    
    def ecender(self): # encender es una funcion que canbia es valor que se tenia arriba
       self.encendido=True # ahora le pone uqe ya esta encendido
       print("auto encendido") # hace el print a el auto se encendio ya que al final se le llamo a esta funcion

    def apagar(self): # apgar cuando llamas a esta funcion te devuelve su valor
       self.encendido=False # ahora canbia el valor a falso
       print("coche apagado") # ahora print al mensaje de que este apagado
    
    def piloto_auto_encendido(self):
       self.piloto_auto=True
       print("piloto automatico encendido")
    
    def piloto_auto_apagar(self):
       self.piloto_auto=False
       print("piloto automatico apagado")
       

mi_coche=MyCar("porsche",963) # llamamos a la funcion y le pasamos los parametros y la renombramos
print(mi_coche.marca)  # hacemos el print a mi coche y marca te devuelve su caracteristica
mi_coche.ecender() # ahora llamas a la funcion de encender
mi_coche.apagar() # llamamos a la funcion de apagar    
### podemos poner varios objetos
micoche2=MyCar("porche",911)
micoche2.piloto_auto_encendido()

marca=input("ingrese marca: ")
modelo="cybertruck"
micoche3=MyCar(marca,modelo)
print(micoche3.marca)
print(micoche3.modelo)