import random

score = 0

while True:
    user = int(input("Enter your number (1-6): "))

    computer = random.randrange(1, 7)

    print("Computer:", computer)

    if user == computer:
        print("OUT!")
        break
    else:
        score = score + user
        print("Your Score:", score)

print("Game Over!")
print("Final Score:", score)