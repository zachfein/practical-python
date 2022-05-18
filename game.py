import random

number = random.randint(1, 100)

name = input("Hi, what's your name?\n")

print(name + ",", "I'm thinking of a number between 1 and 100.\n")

guess = int(input("Try to guess my number.\n"))
count = 0

for num in range(number):
    if guess > number:
        print("Your guess is too high.")
        guess = int(input("Try to guess my number.\n"))
        count = count + 1
    elif guess < number:
        print("Your guess is too low")
        guess = int(input("Try to guess my number.\n"))
        count = count + 1
    else:
        count = count + 1
        print("Well done,", name + ", you guessed my number in", count, "tries")
        break