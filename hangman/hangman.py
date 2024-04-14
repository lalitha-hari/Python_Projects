
import random
lg=[]
def iswordguessed(sw,lg):
    count=0
    for i in sw:
        if i in lg:
           count+=1
    return count==len(sw)
            

def getguessedword(sw,lg):
    s=""
    for i in sw:
        if i in lg:
            s=s+i
        else:
            s=s+"_"
    return s


def getavailableletters(lg):
   char="abcdefghijklmnopqrstuvwxyz"
   s=''
   for i in char:
       if i not in lg:
           s=s+i
   return s


def hangman(sw):
    count=8
    print("Welcome to the game hangman!")
    print(" I am thinking of a word that is",len(sw),"letters long")
    print("----------------------------------")
    while count>0:
        print("you have",count,"guesses left")
        print("Available Letters:",getavailableletters(lg))
        letter=input("Please guess a letter:")
        if letter in lg:
            print("already exist",getguessedword(sw,lg))
        else:
            lg.append(letter)
            if letter not in sw:
                print("oops! that letter is not in my word:",getguessedword(sw,lg))
                count-=1
            elif letter in sw:
                print("Good Guess:",getguessedword(sw,lg))

        if iswordguessed(sw,lg):   
            print("Congratulations the word is correct",sw)
            break
            
    if count==0:
        print(" Sorry yoy ran out of guesses, the word was",sw)

def chooseword(reader):
    word=reader.split()
    index=random.randint(0,len(word)-1)
    w=word[index]
    return w



def loadwords():
    f = open("C:/Users/lalit/OneDrive/Documents/CSPP-1/remedials of python/exam code/hangman/sgb-words.txt", "r")
    reader = f.read()
    w=chooseword(reader)
    f.close()
    print(w)
    return w


sw=loadwords()
sw=sw.lower()
hangman(sw)



