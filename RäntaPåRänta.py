while True:
    try:
        # Användarinmatning
        money = float(input("Skriv in dina pengar: "))
        interest_rate = float(input("Skriv in årsränta (%): "))
        break
    except ValueError:
        print("Felaktig inmatning. Skriv endast med siffror och punkt. \n>Tillbaka till första steget.")

# Beräkning och utskrift
print(f"{'År':<5}{'Summa':<12}{'Delta':<12}")
for i in range(1, 11):
    delta = round(money * (interest_rate / 100), 2) 
    money = round(money + delta, 2) 
    print(f"{i:<5}{money:<12.2f}{delta:<12.2f}")

# Avslut
input("Tryck på Enter för att avsluta.")