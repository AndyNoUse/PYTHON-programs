# Skriv ett program som läser in uppgifter om ett antal personer, 
# och beräknar genomsnittsåldern för kvinnor respektive män i gruppen.
# Följ följande flödesschema.
# https://drive.usercontent.google.com/download?id=18E02CdN4ge_W8RdIbMWSwpGuwGzKFUlX&export=view&authuser=0
# Tips: Läs om flödeschema här:  https://www.codebean.se/algoritmer/
# För att få betyget B 
# Koden måste vara kommenterad och väldokumenterad, 
#så det framgår hur du löst uppgiften!

#Creation of variables.
age1 = 0    #Men age
age2 = 0    #Women age
gender1 = 0 #Number of men
gender2 = 0 #number of female

#Mata in person
i=1
while i > 0:
    gender = input('Ange kön (M)an eller (K)vinna: ').upper()
    age = int (input('Ange ålder: '))
    i += 1
    if gender(M):
        gender1 += 1
        age1 += age
    if gender(f):
        gender2 += 1
        age2 += age
print(age1, age2, gender1, gender2) #Debug
#Kat 1 Yes/no kön?

#Yes add 1 to A1

#Yes add age to g1

#No add 1 to A2

#No add age to g2

#Add more people? Yes return to Mata in person. No continue

#M1 = G1/A1
#print A1 and M1

#M2 = G2/A2
#print A2 and M2
 
#Done