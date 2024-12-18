#Pair up the smallest number in the left list with the smallest number in the right list, then the second-smallest left number with the second-smallest right number, and so on 
#3   4
#4   3
#2   5
#1   3
#3   9
#3   3

#Within each pair, figure out how far apart the two numbers are; you'll need to add up all of those distances.
# For example, if you pair up a 3 from the left list with a 7 from the right list, the distance apart is 4; if you pair up a 9 with a 3, the distance apart is 6.

#In the example list above, the pairs and distances would be as follows:

#The smallest number in the left list is 1, and the smallest number in the right list is 3. The distance between them is 2. L smallest 1 R smallest 3 diff 2
#The second-smallest number in the left list is 2, and the second-smallest number in the right list is another 3. The distance between them is 1. L second smallest 2 and R Second smallest 3 diff 1
#The third-smallest number in both lists is 3, so the distance between them is 0. ????????????
#The next numbers to pair up are 3 and 4, a distance of 1. L fourth smallest 3 R fourth smallest 4 diff 1 
#The fifth-smallest numbers in each list are 3 and 5, a distance of 2. L fifth smallest 3 R fifth smallest 5 diff 2
#Finally, the largest number in the left list is 4, while the largest number in the right list is 9; these are a distance 5 apart. L sixth smallest 4 R sixth smallest 9 diff 5 

#To find the total distance between the left list and the right list, add up the distances between all of the pairs you found. In the example above, this is 2 + 1 + 0 + 1 + 2 + 5, a total distance of 11!
#Your actual left and right lists contain many location IDs. What is the total distance between your lists?


#WEBSCRAPING LEEEETS GOOOOOOOO *GPT Version tyvärr
import urllib.request

url = "https://adventofcode.com/2024/day/1/input"

# Lägg till cookie för autentisering (ersätt 'your_session_token' med din egen session-token) # hitta den i F12 sen network sen headers och sen input. 
headers = {
    "Cookie": "ru=53616c7465645f5f98edcd516c1cfa7aae9d166c4f7832d344adbf10a79305b1; session=53616c7465645f5f1e54a34799e51c4bfe39c43f2b4336c6d3fa329cfbfd4c156a590e02b85b882e04b473828f62406e7c1c711ac918bf42eb6bd7867a52a287"
}
# Hämta data från webbsidan
request = urllib.request.Request(url, headers=headers)
try:
    with urllib.request.urlopen(request) as response:
        data = response.read().decode("utf-8")  # Avkoda innehållet till text
        print("Data hämtad från webbsidan:")
        print(data)
        data
except urllib.error.URLError as e:
    print(f"Kunde inte hämta data: {e.reason}")

rows = data.strip().split("\n")  # Splitta på nya rader

        # Initiera listor för vänster och höger kolumn
left_column = []
right_column = []

        # Gå igenom varje rad och dela upp värden
for row in rows:
            values = row.split()  # Splitta på mellanslag
            if len(values) == 2:  # Kontrollera att det finns två kolumner
                left_column.append(int(values[0]))  # Lägg till i vänsterkolumnen
                right_column.append(int(values[1]))  # Lägg till i högerkolumnen
#* GPT

#print("Vänster kolumn:", left_column)
#print("Höger kolumn:", right_column)

numbers_sortedLeft = sorted(left_column)
numbers_sortedRight = sorted (right_column)

#print ("Sorterad Vänster", numbers_sortedLeft)
#print ("Sorterad Höger", numbers_sortedRight)

difference = [abs(l - r) for l, r in zip(numbers_sortedLeft, numbers_sortedRight)] #GPT lösning
#print("Skillnaden mellan varje tal är:", difference)
print("Summan av skillnaderna är:", sum(difference))


#Del 2 

# Beräkna likhetspoängen #GPT lösning :(
similarity_score = 0
for num in left_column:
    count_in_right = right_column.count(num)  # Antal gånger talet förekommer i höger listan
    similarity_score += num * count_in_right  # Lägg till i totala poängen

print("Total similarity score:", similarity_score)

input ("Press enter to exit")