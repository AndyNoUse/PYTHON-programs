#ChatGPT Lesson
# i = 1
# while i < 6:
#     print(i)
#     i += 1 
##########################
# i = 10
# while i > 0:
#     print (i)
#     i -= 1
##########################
# word = "hello"
# for x in word:
#     print (x)
#######################
#Skriv en Python-funktion som tar en lista 
# av heltal som indata och använder en for-loop för att 
# beräkna summan av alla element i listan.
#########################
#FEL
# heltal = input ("Skriv tre heltal:")
# heltal = heltal.split()
# calculatedHeltal = int(heltal [0]) + int(heltal[1]) + int(heltal [2])

# print (calculatedHeltal)
##################################
#GPT Version
# try:
#     heltal = input("Skriv tre heltal separerade med mellanslag: ")
#     heltal = heltal.split()

#     if len(heltal) != 3:
#         raise ValueError("Du måste skriva in exakt tre heltal.")

#     calculatedHeltal = int(heltal[0]) + int(heltal[1]) + int(heltal[2])
#     print("Summan av heltalen är:", calculatedHeltal)

# except ValueError as e:
#     print("Fel:", e)
# except IndexError:
#     print("Fel: Du måste skriva in exakt tre heltal.")
#############################
# i = 0
# while i < 10:
# 	print (i)
# 	i += 1
# ###########
# for x in (1, 2, 3, 4, 5):
#     print (x)
lista = 1, 2, 3, 4
for x in (lista):
    print (x)

#chatgpt
#for i, x in enumerate(range(10)): print(i, x)
x = "Hello"
y = "World"
print(x, y)

