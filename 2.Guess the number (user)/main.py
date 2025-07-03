import random


def computer_guess(x:int)->None:

    

    low=1
    high=x
    feedback=''
    while feedback!='c':

        if low!=high:
            random_number=random.randint(low,high)
        else:
            random_number=low
        
        feedback=input(f"Is the number : {random_number} Too High (H) or Too Low (L) or Correct (C) : ").lower()

        if feedback=="h":
            high-=1
        elif feedback=="l":
            low+=1
    
    print(f"Yay ! The Computer guessed your number it is {random_number}")





#Driver Code

x=int(input("Enter an ending point : "))

computer_guess(x)
