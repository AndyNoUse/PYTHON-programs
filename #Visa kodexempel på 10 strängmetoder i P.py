#Visa kodexempel på 10 strängmetoder i Python.
#Ta skärmbilder på koden och resultat vid exekvering

text = 'love nilsson'

print (text.center (25, '+'))

print (text.count('o'))

print (text.rjust (20, '-'))

print (text.ljust(20,'*'))

print (text.upper())

print (text.lower())

print (text.capitalize())

print (text.title())

print (text.strip('nilsson')) #love innehåller L och O 

print (text.replace('love', 'oskar'))