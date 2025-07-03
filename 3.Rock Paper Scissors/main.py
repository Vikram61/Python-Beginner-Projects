import random

def play(s):

    computer_choice=random.choice(['r','s','p'])

    if s==computer_choice:
        return "It's a tie"
    
    if is_win(s,computer_choice):
        return f"Yay! You won and computer lost. Computer Choice '{computer_choice}' and your choice '{s}'"
    else:
        return  f"Oops! You lost and computer won. Computer Choice '{computer_choice}' and your choice '{s}'"


def is_win(s,computer_choice):
    if (s=="r" and computer_choice=="s") or (s=="p" and computer_choice=="r") or (s=="s" and computer_choice=="p"):
        return True
    return False
#Driver Code

s=input("Enter R for Rock, P for Paper, and S for Scissors : ").lower()

print(play(s))