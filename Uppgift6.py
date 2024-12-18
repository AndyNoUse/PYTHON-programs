#Uppgift6 av Love Nilsson
# Ett program som läser in uppgifter om ett antal personer, 
# och beräknar genomsnittsåldern för kvinnor respektive män i gruppen.

#Creation of variables.
a1 = 0  #Men age
a2 = 0  #Women age
g1 = 0  #Number of men
g2 = 0  #Number of women
m1 = 0  #Average men age
m2 = 0  #Average women age

#Input data for a person
while True:
    gender = input("Ange kön (m/k): ").lower()
    if gender not in ['m', 'k']:
        #If input is invalid, ask for a new input.
        print("Felaktig inmatning. Ange 'm' för man eller 'k' för kvinna.")
        continue

    try:
        age = int(input ("Ange personens ålder: "))
        if age <= 0:
            #If age is zero or below, ask for a new input
            print("Åldern får inte vara negativ eller noll. Försök igen.")
            continue

    except ValueError:
        #If the value is anything unexpected 
        print("Felaktig inmatning. Börja om med att ange kön.")
        continue

    #Keeps track of how many men and their age.
    if gender == "m":
        a1 += 1
        g1 += age

    #Keeps track of how many women and their age.
    if gender == "k":
        a2 +=1
        g2 += age
        
    #Check if more persons are to be input. "ja" continues the program.
    while True:
        fler = input('Vill du lägga till flera? (ja/nej): ').lower()
        if fler in ['ja', 'nej']:
            break
        else:
            print ("Felaktig inmatning. Ange 'ja' för att fortsätta eller 'nej' för att avsluta.")
        #"nej" breaks the loop and we continue to the next step
    if fler == 'nej':
        break

#Calculate each groups average age.
if g1 != 0 and a1 != 0:
    m1 = g1 / a1
if g2 != 0 and a2 != 0:
    m2 = g2 / a2

#Display results and number of people of that gender.
print(f'Medel åldern på män var: {m1} år. Antal var: {a1} st')
print(f'Medel åldern på kvinnor var: {m2} år. Antal var: {a2} st')

#Buffer to have time to read the score.
input("\nTryck Enter för att avsluta.")