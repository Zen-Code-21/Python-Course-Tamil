import random

print("Welcome to the lucky number guess....")
print("---------------------------------")

randnum = random.randint(0,100)

guess = 0
while True:
    user_input = input("Guess the lucky number between 1 to 100 or press 'q' to quit: ")
    if(user_input == "q"):
        break
    user_input = int(user_input)  
    if(user_input == randnum):
        guess += 1
        print(f"Success : YOU GUESSED THE NUMBER CORRECTLY in {guess} GUESSES !!")
        break
    elif(user_input < randnum):
        print("WRONG GUESS ! Guess a higher number....")
        guess += 1
    else:
        print("WRONG GUESS ! Guess a lower number....")
        guess += 1

print("GAME OVER")






