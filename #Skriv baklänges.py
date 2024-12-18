#Skriv baklänges
s = input('Skriv något: ')
lgd = len(s)
i = lgd - 1
print('Baklänges blir det: ')
while i >= 0:
    print (s[i], end = '')
    i -= 1