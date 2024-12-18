# #Bok exempel på funktioner
# def skriv_summa (x, y):
#     summa = x + y
#     print ('Summan av', x, 'och', y, 'är', summa)
# x = input (':')
# y = input (':')
# skriv_summa (x, y)
# input ('Press enter to ')

# def funk (x):
#     print ('x i funktionen är först', x)
#     x += 5
#     print ('Nu är x i funktionen', x)
# x = 15
# print ('x i programmet är',)
# funk(x)
# print('x i programmet är fortfarande', x)

# def medel(x , y , z):
#     summa = x + y + z
#     mv = summa / 3
#     print('Medel värdet av', x,'och', y, 'och', z, 'är', mv)

# x = int(input())
# y = int(input())
# z = int(input())
# medel(x, y, z)

# try:
#     a = 2 + "5"
# except TypeError as e:
#     print(f"An error occurred: {e}")
#     a = None

# print(a)


a = 10 
b = 0
try:
    c = a/b
except ZeroDivisionError:
    print ('Division med noll.')
print ('Fortsätter programet')