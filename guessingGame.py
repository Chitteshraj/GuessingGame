import random
import time
import os

print("Guess the number challenge!\n")
time.sleep(1)

difficulty = input("Select difficulty (Baby, Easy, Normal, Hard, Hardest, Impossible):\n")
time.sleep(2.5)

while difficulty != "Baby" and difficulty != "Easy" and difficulty != "Normal" and difficulty != "Hard" and difficulty != "Hardest" and difficulty != "Impossible":
    difficulty = input("Select difficulty (Baby, Easy, Normal, Hard, Hardest, Impossible):\n")

if difficulty == "Baby":
    randoy = random.randint(1,3)
    max = int(3)
elif difficulty == "Easy":
    randoy = random.randint(1,5)
    max = int(5)
elif difficulty == "Normal":
    randoy = random.randint(1,10)
    max = int(10)
elif difficulty == "Hard":
    randoy = random.randint(1,25)
    max = int(25)
elif difficulty == "Hardest":
    randoy = random.randint(1,50)
    max = int(50)
else:
    randoy = random.randint(1,100)
    max = int(100)

time.sleep(2)
ent = int(input("Guess the number I'm thinking of (Baby= 1-3; Easy= 1-5; Normal= 1=10; Hard= 1-25; Hardest= 1-50; Impossible= 1-100)\n"))
time.sleep(1)

while ent < 1 or ent > max:
    print("Baby= 1-3; Easy= 1-5; Normal= 1=10; Hard= 1-25; Hardest= 1-50; Impossible= 1-100\n")
    time.sleep(2)
    ent = int(input("Guess a number depending on the range 👆:\n"))
    time.sleep(1)

if ent == randoy:
    print("You won!!🥳🥳🥳")
else:
    print("You lost!")
    time.sleep(1)
    print("Better luck next time!")
    time.sleep(2)
    print("The number I was thinking of was ", randoy)