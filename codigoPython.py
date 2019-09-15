valor = "1233"
print(valor)

if valor == ("1233"):
    print("True")
else:
    print("False")

def mostrar():
    print ("Pantalla")
    print("Teclado")

mostrar()
mostrar()

def nombres(nombre):
    if nombre == "Mirella":
        print ("hola Mirella")
    elif nombre == "Azucena":
        print ("hola Azucena")
    else:
        print ("hola")

nombres("Mirella")


def persona(nombre):
    print ("Hola" + nombre)

persona("Maria")

####

def alumno(nombre):
    print ("Hola "+ nombre)

chicas=["mirella","azucena"]
for nombre in chicas:
    alumno(nombre)
    print (">>")

for i in range(1,6):
    print(i)
