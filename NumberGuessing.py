import random

print("Welcome to the number Guessing Game!!")
print("I'm thinking about a number between 1 to 100")
diff = input("Choose your difficulty.Type 'easy' or 'hard'")

def difficulty(diff):
    life = 0
    if diff == 'easy':
        print('You have 10 Chances')
        return life ==  10
    elif diff == 'hard':
        print('You have 5 Chances')
        return life == 5
    else:
        print('invalid entry')

difficulty(diff)
difficulty()
choice = random.randrange(1,100)
print(choice)
correct_guess = False



while not correct_guess:
    for _ in difficulty:
        
        
            
        guess = int(input("Make a guess"))
        if diff == 0:
            correct_guess = True 
            print("you loose , your out of lives")
            if guess == choice:
                correct_guess = True
                print("you won!!")
            elif guess < choice:
                print("To Low")
            else:
                print("To High")
