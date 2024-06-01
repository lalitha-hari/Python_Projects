import random

def deck_creation():
    deck = []
    for i in range(2, 12):
        deck += [i] * 4  
    
    deck += [10] * 12 
    return deck


def dealing_cards(deck):
    player1 = []
    player2 = []
    
    
    while len(deck) > 0:
        player1.append(deck.pop())

        player2.append(deck.pop())
    
    return player1, player2



def main_game(player1,player2):
    score_player1=0
    score_player2=0
    while len(player1)>0:
        input("Press enter to pick your card ")
        player1_turn=player1.pop()
        print("player1 card is",player1_turn)
        player2_turn=player2.pop()
        print("player2 card is",player2_turn)
        if player1_turn > player2_turn:
            print("player1 card is greater than player2")
            score_player1+=player1_turn+player2_turn
            print("The score of player1 is ",score_player1)
        elif player2_turn>player1_turn:
            print("player2 card is greater than player1")
            score_player2+=player1_turn+player2_turn
            print("The score of player2 is ",score_player2)
        else:
            print("player1 card and player2 is equal")
            score_player1+=player1_turn
            score_player2+=player2_turn
            print("The score of player1 is ",score_player1)
            print("The score of player2 is ",score_player2)
        print("------------------------------------------------------------------------------------------")

    return score_player1,score_player2

def win(score1,score2):
    print("player1 score: ",score1)
    print("player2 score: ",score2)
    if score1>score2:
        print("Player 1 won the game ",)
    elif score2>score1:
        print("player 2 won the match")
    else:
        print("It's a tie")



def game():
    print("--------------WELCOME TO PYCAEDDUEL----------------")
    deck = deck_creation()
    print("Deck before shuffle:", deck)
    print("Length of deck before shuffle:", len(deck))
    random.shuffle(deck)
    player1, player2= dealing_cards(deck)
    print("Player 1 cards:", player1)
    print("Player 2 cards:", player2)
    print("--------------Start the game---------------------")
    score1,score2=main_game(player1,player2)
    win(score1,score2)

game()