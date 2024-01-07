def main():
    text = input("What time is it? ")
    time = convert(text)

    if time >= 7 and time <= 8:
        print("breakfast time")
    elif time >= 12 and time <= 13:
        print("lunch time")
    elif time >= 18 and time <= 19:
        print("dinner time")


def convert(time: str):
    h, m = time.split(":")

    return int(h) + int(m) / 60


if __name__ == "__main__":
    main()
