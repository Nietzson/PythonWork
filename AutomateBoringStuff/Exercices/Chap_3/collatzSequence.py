import sys, time
def collatz(number):
    global input
    if number%2 == 0:
        input = number // 2
        print(f"{input}")

    else:
        input = 3 * number + 1
        print(f"{input}")

def main():
    global input
    try:
        input = int(input("Enter a number: "))
    except ValueError:
        print("You must enter an integer, dummy!")
        return

    while input != 1:
        collatz(input)
        time.sleep(0.015)
    print("Collatzed!")

main()
