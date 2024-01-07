def main():
    text = input("Input: ")
    print(f"Output: {shorten(text)}")


def shorten(word):
    vowels = ["a", "o", "i", "e", "u"]

    text_without_vowels = ""
    for i in word:
        if i.lower() not in vowels:
            text_without_vowels += i

    return text_without_vowels


if __name__ == "__main__":
    main()
