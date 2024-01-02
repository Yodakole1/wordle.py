#This is wordle game, but not like every other it doesnt tell you if the letter you found is on right place. 
#Thats why user have 10 tries instead of 5.

import random

#Declaration
words =[]
file = open("words.txt","r")
content=file.read()
letters=[]
keyword = ""
i=0
file = open("words.txt","r")

#Take random word from file and lower it
for f in file.readlines():
    words+=[i for i in f.split(" ")]
    
keyword = random.choice(words)
keyword = keyword.lower()

#Main wordle game
while(i<10):
    YourWord = input("Enter your word: ")
    YourWord = YourWord.lower()
    if YourWord in content:
        if(input==keyword):
            print("Nice u found the right word")
            break
        else:
            for leta in YourWord:
                for letb in keyword:
                    if(leta == letb):
                        letters+=leta
                        letters = list(dict.fromkeys(letters))
    else:
        print("Your word doesnt exist try again")
        i=i-1
    
    print(letters)
    
    i=i+1

print("Done. Keyword is " + keyword)    