def convert(str):
    return str.replace(":)", "🙂").replace(":(", "🙁")


def main():
    text = input()
    print(convert(text))


main()
