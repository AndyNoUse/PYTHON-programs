#Bank.py Delta (Differance ver)
#Skriv ett program som beräknar hur mycket pengar man får på ett bankkonto 
#om man sätter in 100 000kr (hundratusen kronor) och låter pengarna stå inne under 5 år.
#När man kör programmet frågar det efter räntesatsen, som anges i procent t.ex. 3.5
#Som resultat visar programmet en tabell där man kan se hur mycket kapitalet har växt efter varje år. 
#Spara programmet i en fil som heter bank.py

#Begränsningar

money = 100000 #input ("Skriv in dina pengar (endast siffror): ")


interest_rate = input ("Skriv in årsränta (endast siffror): ")
interest_rate = float(interest_rate)


#Table and math used.
print ('År\tSumma\t\tDelta')
for i in range (1, 6):
    delta = money * (interest_rate/ 100)
    money += delta
    print (i,  round(money, 2), round(delta, 2), sep='\t')

#buffer to read result
input ("Press enter to exit")