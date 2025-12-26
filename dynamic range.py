import random
previous = 100
print("This is a game where you have to guess a number, but the range decreases with time.")
number = random.randint(1, previous)
while True:
    try:
        previous -= 5
        if number > previous: number = random.randint(1, previous); print('A new number has been generated. It fits inside the range of', previous)
        userguess = int(input("Please insert your guess here (number higher than 1, initially lower than 100) >>"))
        if userguess == number: print("Congrats! You've just guessed the number."); break
        if userguess != number: print("Wrong guess. Try again!")
    except ValueError:
        print("Please insert a correct value. Range was decreased.")
input("Press any key to close this window.")


