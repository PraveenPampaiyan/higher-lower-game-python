import random
from art import logo,vs
from game_data import data
import os
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def account_format(account):
    account_name=account['name']
    account_desc= account['description']
    account_country=account['country']
    return f" {account_name},a {account_desc} from {account_country}"

def check_guess(user_guess,count_follower_a,count_follower_b):
    if count_follower_a>count_follower_b:
        return user_guess=="a"
    else:
        return user_guess=="b"


restart_game="y"
while restart_game=="y":
    print(logo)
    score=0
    game_should_continue=True
    account_b=random.choice(data)

    while game_should_continue:
        account_a=account_b
        account_b=random.choice(data)
        while account_a==account_b:
            account_b=random.choice(data)

        print(f"compare A :{account_format(account_a)}")
        print(vs)
        print(f"compare B :{account_format(account_b)}")

        guess=input(" guess you're predict Type 'A' or 'B' ").lower()

        clear()

        if guess not in ["a","b"]:
            print("Type valid Word ")
            continue

        follower_a=account_a['follower_count']
        follower_b=account_b['follower_count']

        is_correct=check_guess(guess,follower_a,follower_b)
        if is_correct:
            score+=1
            print(f"\n you're Right! current score is {score}")
        else:
            print(f"\n your predict is wrong! your score is {score}")
            game_should_continue=False


    restart_game=input(" restart game type 'Y' or 'N' ").lower()
    clear()

    if restart_game=="n":
        print("\n Thank you for playing")





