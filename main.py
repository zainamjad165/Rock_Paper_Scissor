import random

def play():
    computer=random.choice([ 'r' , 's' , 'p' ])
    print(computer)
    user=input ("what is your choice? press (R) for rock, (P) for paper and (S) for scissors:   ").lower()
    if user==computer:
        return("it's a tie")
    if is_win(user,computer):
        return("you won")
    return("you lost")

def is_win(player,opponent):
    if (player=='r' and opponent=='s') or (player=='s' and opponent=='p') or (player=='p' and opponent=='r'):
        return True

print(play())
