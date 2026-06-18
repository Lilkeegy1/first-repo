tries = 0
import random
import time
num = random.randint(1,100)

print("Hi! Welcome to the Number Guessing Game. Here are the rules:")
_ = input(""" - I will think of a number between 1 and 100 (inclusive)
 - You will have to guess the number
 - I will tell you if it is too high or too low
 - "Much lower/higher" means my number is at least 20 less/more than your guess
 - "Lower/higher" means my number is 6 to 20 less/more than your guess.
 - "Lower/higher, but close" means my number is 5 values higher or lower than yours

Press enter (or any key) to play!
""")

ges = int(input("I've thought of a number between 1 and 100. Guess which! "))
start = time.time()

while True:
    tries += 1
    if num < ges: # Guess is too high
        if ges - num > 20:
            ges = int(input("Nope, much lower! "))
        elif ges - num < 21 and ges - num > 5:
            ges = int(input("Nope, lower! "))
        elif ges - num < 6 and ges - num > 0:
            ges = int(input("Nope, lower, but close! "))
    elif num > ges: # Guess is too low
        if num - ges > 20:
            ges = int(input("Nope, much higher! "))
        elif num - ges < 21 and num - ges > 5:
            ges = int(input("Nope, higher! "))
        elif num - ges < 6 and num - ges > 0:
            ges = int(input("Nope, higher, but close! "))
    else: #  Guess is right
        end = time.time()
        total_time = end-start
        print (f"Yes! You got it in {tries} turns, and took ~{total_time:.2f} seconds!")
        break
