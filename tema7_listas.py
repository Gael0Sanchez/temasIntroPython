lista1 = []
lista2 = [1,2,3,4,5]
lista3 = [2.1, 3.2, 6.2]
lista4 = ["Mario","Juan","Beto","Jorge"]
lista5 = [1, 2, 2.1, 3.2, 6.2, "Juan"]

print(type(lista1))
print(lista2[3])
print(len(lista2))
print(lista2)
lista2[2]=7
print(lista2)

lista1.append(1)
lista1.append(11)
lista1.append(10)
print(lista1)
lista1.pop()
print(lista1)

print(lista2)
lista2.sort()
print(lista2)