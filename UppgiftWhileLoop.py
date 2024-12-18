#Uppgift2 Medel While Loop av Marivan (Love)
#Skapa ett Python-program som frågar efter poäng på tre olika prov.
#Beräkna medelvärdet av alla tre poängen.
#Skriv ut medelvärdet.
#Om medelvärdet är över 90, skriv också ut "Bra jobbat".

#while input =! ("")
#loop index + 1
#Result + = input
#
#Result / = loop index

a = input ("First Test Score: ")
index = 0
Result = 0
while a != "":
    index+= 1
    Result+= float (a)
    a = input ("Next test score: ")
Result /= index

#
print (Result)
if Result > 90:
    print ("Bra jobbat!")
else:
    print ("Woops. Inte bra jobbat.")

#Buffer to have time to read the score.
input ("Press Enter to exit")
