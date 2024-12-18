#primtal av Love Nilsson
#Programmet skall skriva ut alla primtal mellan 1 och det inlästa talet.

#Imported modul for "sqrt" function
import math

#Checks if the number is a prime. If not skip that number.
def isPrimtal(n):
    #If the number is less than or equal to 1, it is not a prime.
    if n <= 1:
        return False
    #We go through all numbers from 2 up to and including the square root of the number
    # to see if any of them divide the number without a remainder.
    for i in range(2, int(math.sqrt(n)) + 1):
        #If the number is divisible by any number in the range, it is not a prime.
        if n % i == 0:
            return False
        #No divisor means the number is a prime.
    return True

#Number given is converted to a int.
tal = int (input('Skriv in ett tal:'))

#Displays prime numbers between 1 and the inputted number.
def primtal():
    for x in range (1, tal):
        if isPrimtal(x):
            print (x)

#Call the function.
primtal()

#Buffer to have time to read the score.
input("\nTryck Enter för att avsluta")