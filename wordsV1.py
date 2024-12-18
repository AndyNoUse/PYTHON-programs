#words.py av Love Nilsson

#Put in user sentence
sentence = input ("Skriv en mening med minst 2 ord:")

#Sentence gets broken down into individual words
sentenceWords = sentence.split()

#Each word is counted and first and last one is recorded.
sentenceWordCount = f'Du skrev {len(sentenceWords)} ord' 
sentenceFirstWord = f'Det första ordet är "{sentenceWords[0]}"'
sentenceLastWord = f'Det sista ordet är "{sentenceWords[-1]}"'

#Result is displayed
print (sentenceWordCount)
print (sentenceFirstWord)
print (sentenceLastWord)

#Buffer to read result
input ('\nTryck enter för att avsluta')