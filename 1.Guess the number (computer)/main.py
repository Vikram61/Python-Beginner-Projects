import random

def guess(x):

    random_number=random.randint(1,x)
    expression=0

    while expression!=random_number:

        expression=int(input(f"Guess a number between 1 and {x}: "))
        
        if expression < random_number:
            print("Sorry Guess Again Too Low !!")
        elif expression > random_number:
            print("Sorry Guess Again Too High !!")
    
    print("Yay! Congrats you have guessed the correct number")





#Driver Code

x=int(input("Enter an ending point : "))
guess(x)
