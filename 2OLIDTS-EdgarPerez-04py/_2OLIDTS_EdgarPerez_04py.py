maxf=3
maxc=3
a=[[0.0]*maxc for _ in range (maxf)] #creacion de matrix de ceros (Arreglo bidimencional)
#leer el arrary
for f in range (maxf):
    for c in range (maxc):
        print ("Ingrese un valor: ")
        a[f][c]=float (input())
#escribir el array
print ("Impresion de Balores almacenados")
for f in range (maxf):
    for c in range (maxc):
        print(a[f][c], end=" ")
    print ()