#This is wordle game.


import random


#Initialization
words = []
keyword = ""
i=0
file = open("words.txt","r")

#Take random word from file and lower it
for f in file.readlines():
    words+=[i for i in f.split(" ")]
    

keyword = random.choice(words)
#All the words in my file are already in lowercase. However, I included this precaution in case someone uses a different file or if i add more content.
keyword = keyword.lower()

print("Wordle is a word puzzle game where players have six attempts to guess a five-letter word, receiving feedback on which letters are correct and in the right position.")
print("Have fun")

def word_check():
    pokusaji = 6
    
    while(pokusaji > 0):
        pogodi = str(input("Guess word:"))
        if(pogodi == keyword):
            print("WOOHOOOO. You guessed correctly.")
            break
        else:
            pokusaji = pokusaji - 1
            print(f"You have {pokusaji} attempts left \n")

            for i,j in zip(keyword,pogodi):
                if j in keyword and j in i:
                    print(j + " right place")
                elif j in keyword:
                    print(j + " wrong place")
                else:
                    print("X")    

        if pokusaji == 0:
            print("You lost")
            print("Solution is " + keyword)
                



word_check()            
