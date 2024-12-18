#words.py av Love Nilsson
#Put in user sentence.
sentence = input ("Skriv en mening med minst 2 ord:").split()

#Each word is counted, first and last one is displayed.
print(f'Du skrev {len(sentence)} ord')
print(f'Det första ordet är "{sentence[0]}"')
print(f'Det sista ordet är "{sentence[-1]}"')

#Buffer to read result.
input ('\nTryck enter för att avsluta')