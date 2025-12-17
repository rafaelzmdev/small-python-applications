import random
previous = 100
print("This is a game where you have to guess a number, but the range decreases with time.")
while True:
    number = random.randint(1, previous)
    previous -= 5
    try:
        userguess = int(input("Please insert your first guess here (number higher than 1, initially lower than 100) >>"))
        if userguess == number: print("Congrats! You've just guessed the number."); break
        if userguess != number: print("Wrong guess. Try again!")
    except ValueError:
        print("Please insert a correct value.")
input("Press any key to close this window.")