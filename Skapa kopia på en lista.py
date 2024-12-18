import copy
#Hur skapar man en kopia på en lista?
#Visa fyra olika sätt.
#Visa kodexempel. Ta skärmbilder på koden och resultat vid exekvering. 
lista1 = [1, 2, 3, 4]

lista2 = [x for x in lista1]
print (lista2)
lista2 = 0

lista2 = copy.copy (lista1)
print (lista2)
lista2 = 0

lista2 = copy.deepcopy (lista1)
print (lista2)
lista2 = 0

lista2 = lista1[:]
print (lista2)