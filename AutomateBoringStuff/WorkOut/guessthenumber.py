import random

def rng():
    solution = random.randint(1,20)
    tries = 1
    print("I am thinking of a number between 1 and 20.")
    while True:
        number = int(input("Take a guess: "))
        if number < solution:
            print("Your guess is too low.")
            tries = tries + 1
            continue
        elif number > solution:
            print("Your guess is too high.")
            tries = tries + 1
            continue
        else:
            print(f"Good job! You guessed the number in {int(tries)} tries!")
            return

rng()
