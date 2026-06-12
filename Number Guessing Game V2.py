tries = 1
import random
num = random.randint(1,100)

ges = int(input("I've thought of a number between 1 and 100. Guess which! "))

while True:
    if num < ges: # Guess is too high
        if ges - num > 20:
            ges = int(input("Nope, much lower! "))
        if ges - num < 21 and ges - num > 5:
            ges = int(input("Nope, lower! "))
        if ges - num < 6 and ges - num > 0:
            ges = int(input("Nope, lower, but close! "))
    elif num > ges: # Guess is too low
        if num - ges > 20:
            ges = int(input("Nope, much higher! "))
        if num - ges < 21 and num - ges > 5:
            ges = int(input("Nope, higher! "))
        if num - ges < 6 and num - ges > 0:
            ges = int(input("Nope, higher, but close! "))
    else: #  Guess is right
        print ("Yes! You got it in", str(tries) + " turns! You have a brain!")
        break
    tries += 1
