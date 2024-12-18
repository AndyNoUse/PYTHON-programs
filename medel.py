#Uppgift 2 Medel av Love Nilsson

# Input scores from tests
first = float (input ("First Test score: "))
second = float (input ("Second Test score: "))
third = float (input ("Third Test score: "))

#Calculations to figure out the result.
result = first + second + third
result = result / 3

#Product and success or fail 
print (result)
if result > 90:
    print ("Bra jobbat!\n")
else:
    print ("Woops. Inte bra jobbat.\n")

#Buffer to have time to read the score.
input ("Press Enter to exit")