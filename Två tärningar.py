#Value of two dice av Love Nilsson
import random

#Creation of a function to cast two die.
def tossDoubleDice():

    #Each dice is given a value between 1 and 6.
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    #Result is displayed 
    print(f"Första tärningen blev {dice1}. Andra tärningen blev {dice2}")

#The function is called.
tossDoubleDice()

#Buffer to read result
input ('\nTryck enter för att avsluta')

#Utvärdering
#Kul att få importera en modul, programmet fungerar som förväntat. 
#Det kan förbättras genom att lägga till input för att bestämma antalet kast
#och lägga till så att man kan se historik på tidigare kast.