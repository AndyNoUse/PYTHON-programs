#Visa kodexempel på 10 listmetoder i Python.
#Ta skärmbilder på koden och resultat vid exekvering. 
numberlist = [1, 2, 3]

numberlist.append(4)
print (numberlist)

numberlist.extend([5, 6, 7])
print (numberlist)

numberlist.insert(8, 8.0)
print (numberlist)

numberlist.remove(8.0)
print (numberlist)

numberlist.pop(6)
print (numberlist)

print (numberlist.index(2))

numberlist.reverse()
print (numberlist)

numberlist.sort ()
print (numberlist)

numberlist.clear()
print (numberlist)