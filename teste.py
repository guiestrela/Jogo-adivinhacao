#frutas = ["maçã", "banana", "laranja", "melancia"]

#lista = [fruta.upper() for fruta in frutas]
#for fruta in frutas:
   # lista.append(fruta.upper())

#print(lista)


#=====================
#inteiros = [1,3,4,5,7,8]

#quadrados = [n*n for n in inteiros]

#print(quadrados)

#=========================
#inteiros = [1,3,4,5,7,8,9]
#pares = []
#for numero in inteiros:
#    if numero % 2 == 0:
#        pares.append(numero)
#print(pares)

#========================
inteiros = [1,3,4,5,7,8,9]
pares = [x for x in inteiros if x % 2 == 0]
print(pares)
