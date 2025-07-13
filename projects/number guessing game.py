import random
print("Hi! Welcome to the Number Guessing Game.\nYou have 10 chances to guess the number. Let's start!")

low = int(input("Enter a min bound value"))
maxx = int(input("enter a max bound value"))
num = random.randint(low,maxx)
ch = 10
gc = 0
print(f'Your give with {ch} chances to guess the number ')
while gc < ch:
    gc+=1
    
    guess = int(input("guess the number "))
    if guess == num:
        print(f"you have guessed correctly with {gc} attempts. hurraihhh ")
        break
    elif guess > num:
        print(f'too high remaining chances {ch-gc}')
    elif guess < num:
        print(f'too low remaining chances {ch-gc}')
    elif gc >= ch and guess != num:
        print(f'orry! The number was {num}. Better luck next time.')
    else:
        print('good bye') # not needed just for fun
    
