#Vad menas med "list comprehensions" (listomfattningar på svenska)?
#Visa kodexempel. Ta skärmbilder på koden och resultat vid exekvering. 

masterList = [x**2 for x in range (10)]
print (masterList)

#eller

masterList2 = [tal for tal in range (10)]
print (masterList2)

#
masterlist3 = [int (input(f'enter number {i + 1}: ')) for i in range (5)]
print (masterlist3)