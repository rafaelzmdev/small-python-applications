import random
number = random.randint(1, 100); attempt = 0
while True:
    diff = str(input("Guess a number between 1 and 100. You can choose how many attempts you'll have based on the difficulty 'Easy', 'Medium' and 'Hard'. Here >"))
    if diff == "Easy": maxattempt = 30; break
    elif diff == "Medium": maxattempt = 15; break
    elif diff == "Hard": maxattempt = 10; break
    else: print("Please insert a valid difficulty.")
while maxattempt - attempt >= 1:
    print("You have:", (maxattempt - attempt), "attempts remaining.")
    try:
        userinput = int(input("Please insert your guess here >>"))
        attempt += 1
        if userinput > number: print("Too high!")
        elif userinput < number: print("Too low!")
        elif userinput == number: print("You got it right! Number of attempts:", attempt); break
    except ValueError:
        print("Please insert a correct value.")
if maxattempt - attempt == 0: input("Oh no! You ran out of guesses. Maybe we should play again sometime? ;) (press a key to close this window.)")
else: input("Congratulations! Maybe we should play again sometime? (press any key to close this window)")