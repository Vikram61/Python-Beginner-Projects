import random
from words import words
import string
from hangman_visual import lives_visual_dict

def get_valid_word(words):

    word=random.choice(words)

    while '-' in word or " " in word:
        word=random.choice(words)
    
    word=word.upper()
    return word


def hangman():

    word=get_valid_word(words)
    word_letters=set(word) #letters in the word
    alphabet= set(string.ascii_uppercase)
    used_letters=set() # what the user has guessed
    lives=7
    #getting user input
    while len(word_letters) > 0 and lives>0 :

        #letters used
        print(' You have ',lives,' left and You have used these letters:', ' '.join(used_letters))
        #What the current word is
        word_list=[letter if letter in used_letters else '__' for letter in word]
        print("Your current life",lives_visual_dict[lives])

        print('Current word:',' '.join(word_list))

        user_letter=input('Guess a letter : ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("")
            else:
                lives-=1
                print("\nYour letter",user_letter, "is not in the word")
        elif user_letter in used_letters:
            print('\nYou have already guessed the character')
            
        else:
            print('Invalid character')
        
    if lives==0:
        print(lives_visual_dict[lives])
        print(f"Sorry you died the word was : ",word)
    else:
        print(f"Yay you guessed the word correctly it is {word}")
    


hangman()
