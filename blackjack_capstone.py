import random

def deal_card():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    if u_score==c_score:
        return "draw"
    elif c_score==0:
        return "lose, opponent has blackjack"
    elif u_score>21:
        return "you went over,you lose"
    elif c_score>21:
        return "opponent went over,you win"
    elif u_score>c_score:
        return "you win"
    else:
        return "you lose"

def playgame():
    user_cards=[]
    computer_cards=[]
    computer_score=-1
    user_score=-1
    is_game_over=False

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)
        print(f"your cards: {user_cards}, your score{user_score}")
        print(f"computer cards:{computer_cards[0]}")

        if user_score==0 or computer_score==0 or user_score>21:
            is_game_over=True
        else:
            user_should_deal=input("type y to get another card, type n to pass:")
            if user_should_deal=="y":
                user_cards.append(deal_card())
            else:
                is_game_over=True
    while computer_score!=0 and computer_score<17:
        computer_cards.append(deal_card())
        computer_score=calculate_score(computer_cards)
    print(f"your final hand is {user_cards} and final score: {user_score}")
    print(f"computers final hand is {computer_cards} and final score : {computer_score}")
    print(compare(user_score,computer_score))
while input("do you want to play blackjack,y or n")=="y":
    print("\n"*20)
    playgame()
