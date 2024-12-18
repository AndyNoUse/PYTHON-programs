#Bank.py av Love Nilsson

# Main values
money = 100000
interest_rate = input ("Skriv in årsränta(%):")

#Conversion from string to float for the calculation.
interest_rate = float(interest_rate)

#Table and calculation. 
print ('År\tSumma')
for i in range (1, 6):
    money += money * (interest_rate / 100)
    print (i, '\t', money, )

#Buffer to read result.
input ("Press enter to exit")