import random
def userchoice():
    userinput=input("rock,paper,scissors:")
    return userinput

def compinput():
    lst=["rock","paper","scissors"]
    a=random.randint(0,2)
    compinput=lst[a]
    return compinput

def game():
    print("welcome to game")
    i=1
    c=0
    u=0
    while i<4:
        userinput=userchoice()
        cominp=compinput()
        if userinput=="rock" and cominp=="scissor":
            print("user won")
            u+=1
        elif userinput=="scissor" and cominp=="paper":
            print(" user won")
            u+=1
        elif userinput=="paper" and cominp=="rock":
            print("user won")
            u+=1
        elif userinput==cominp:
            print("draw")
        elif cominp=="rock" and userinput=="scissor":
            print("computer won")
            c+=1
        elif cominp=="scissor" and userinput=="paper":
            print(" computer won")
            c+=1
        elif cominp=="paper" and userinput=="rock":
            print("computer won")
            c+=1
        i+=1
    if c>u:
        print("computer won total game")
    else:
        print("user won the game")
game()