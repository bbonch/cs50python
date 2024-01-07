import random


def main():
    level = get_level()
    count = 10
    score = 0
    problems = []

    for _ in range(count):
        problems.append([generate_integer(level), generate_integer(level), 0])

    i = 0
    while i < count:
        problem = problems[i]
        if problem[2] == 3:
            print(f"{problem[0]} + {problem[1]} = {problem[1] + problem[0]}")
            i += 1
            continue

        text = input(f"{problem[0]} + {problem[1]} = ")
        try:
            answer = int(text)
            if answer != problem[1] + problem[0]:
                problem[2] += 1
                print("EEE")
            else:
                score += 1
                i += 1
        except ValueError:
            problem[2] += 1
            print("EEE")
            continue

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            text = input("Level: ")
            level = int(text)
            if level < 1 or level > 3:
                continue

            return level
        except ValueError:
            continue


def generate_integer(level):
    if level < 1 or level > 3:
        raise ValueError

    start = 0 if level == 1 else 10 ** (level - 1)
    end = 9 if level == 1 else 10**level - 1
    return random.randint(start, end)


if __name__ == "__main__":
    main()
