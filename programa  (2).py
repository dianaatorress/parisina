
#inputs
print ("E N T R A D A   A L   C I N E")
edad = int(input("Inserta tu edad: "))

#proceso
if edad <= 12:
    print ("Categoria: niño")
    print ("")
elif edad > 12 and edad <= 18:
    print ("Categoria: adolescente")
elif edad > 18 and edad <= 60:
    print ("Categoria: adulto")
else:
    print ("Categoria: tercera edad")


if edad <= 16:
    print ("Tu descuento es del 10%")
elif edad < 44:
    print ("Tu descuento es del 20%")
elif edad < 66:
    print ("Tu descuento es del 30%")
else:
    print ("Tu descuento es del 30%")
