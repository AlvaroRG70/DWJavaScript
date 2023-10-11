n1 = int(input("escribe un número"))
n2 = int(input("escribe un número"))
cadena = "Los pares son: "
if n1 < n2:
    for i in range(n1,n2):
        if i%2 == 0:
            cadena += str(i) + " "
else:
    for i in range(n2,n1):
        if i%2 == 0:
            cadena += str(i) + " "
print(cadena)