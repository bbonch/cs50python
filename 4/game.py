while True:
    text = input("Level: ")
    try:
        level = int(text)
        if level < 1:
            continue
        else:
            break
    except ValueError:
        continue

from random import randint

level_random = randint(1, level)

while True:
    text = input("Guess: ")
    try:
        guess = int(text)
        if guess < 1:
            continue
        elif guess > level_random:
            print("Too large!")
        elif guess < level_random:
            print("Too small!")
        else:
            print("Just right!")
            break
    except ValueError:
        continue
