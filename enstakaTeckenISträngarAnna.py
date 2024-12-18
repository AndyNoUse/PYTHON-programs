#Enstaka tecken I strängar "Anna"

n = 'Anna'
print (n[0])
print (n[1])
print (n[3])
print () #så att vi får ny rad
i = 0
while i < len(n):
    print (n[i] + ' ', end = '')
    i += 1
print ()
for i in range(len(n)):
    print (n[i], end = '')
print ()
for tecken in n:
    print (tecken)
