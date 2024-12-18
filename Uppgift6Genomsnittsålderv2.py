# Skriv ett program som läser in uppgifter om ett antal personer, 
# och beräknar genomsnittsåldern för kvinnor respektive män i gruppen.
# Följ följande flödesschema.
# https://drive.usercontent.google.com/download?id=18E02CdN4ge_W8RdIbMWSwpGuwGzKFUlX&export=view&authuser=0
# Tips: Läs om flödeschema här:  https://www.codebean.se/algoritmer/
# För att få betyget B 
# Koden måste vara kommenterad och väldokumenterad, 
#så det framgår hur du löst uppgiften!

def main():
    # Initialize counters and sums
    A1 = 0  # Counter for Category 1
    G1 = 0  # Sum of ages for Category 1
    A2 = 0  # Counter for Category 2
    G2 = 0  # Sum of ages for Category 2

    while True:
        # Input person
        age = int(input("Ange ålder: "))
        category = int(input("Ange kategori (1 eller 2): "))

        # Check category and update counters and sums
        if category == 1:
            A1 += 1
            G1 += age
        else:
            A2 += 1
            G2 += age

        # Check if more persons are to be input
        fler = input("Fler personer? (ja/nej): ").strip().lower()
        if fler == 'nej':
            break

    # Calculate averages
    M1 = G1 / A1 if A1 != 0 else 0  # Average age for Category 1
    M2 = G2 / A2 if A2 != 0 else 0  # Average age for Category 2

    # Output results
    print(f"A1: {A1}, M1: {M1:.2f}")
    print(f"A2: {A2}, M2: {M2:.2f}")

if __name__ == "__main__":
    main()
