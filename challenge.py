op = 0
edad = 0
contador = 0
contador1 = 0
contador2 = 0
contador3 = 0
materia = 0
materia2 = 0
materia3 = 0


print ("En este programa ingresaran la edad y una materia de 10 personas diferentes")




#Proceso
while contador <= 10:
    contador += 1
    edad = int(input("Dame tu edad "))
    print ("1.Español")
    print ("2. Matematicas")
    print ("3. Frances")
    print ("4. Total")
    op = int(input("Elige la opcion"))

    if edad <= 10:
        contador1 += 1
    elif edad == 10 and edad < 20:
        contador2 += 1
    elif edad > 20:
        contador3 += 1
    if op == 1:
        materia += 1
    elif op == 2:
        materia2 += 1
    elif op == 3:
        materia3 + 1
    elif op == 4:
        print (f"{contador1} personas son menores a 10 años")
        print (f"{contador2} personas tienen entre 10 y 20 años")
        print (f"{contador3} personas son mayores a 20 años")
        print (f"{materia} personas estudian Español")
        print (f"{materia2} personas estudian Matematicas")
        print (f"{materia3} personas estudian Frances")
