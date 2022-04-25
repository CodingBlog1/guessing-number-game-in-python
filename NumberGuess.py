import random

secretnumber = random.randint(1,20)
print("Guess the number between  1 to 20 ")

#user input 
for guesstaken in range(1,7):
    print("guess number")

    guess = int(input())
    if guess < secretnumber:
        print("U guess is to low!")
    elif guess > secretnumber:
        print("U guess is to high!")
    else:
        break
if guess == secretnumber:
    print("Good job : u guess my number in" + str(guesstaken) + "guesses")

else:
    print("NOpe: " + str(secretnumber))