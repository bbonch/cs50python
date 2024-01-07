text = input("Input: ")

vowels = ["a", "o", "i", "e", "u"]

text_without_vowels = ""
for i in text:
    if i.lower() not in vowels:
        text_without_vowels += i

print(f"Output: {text_without_vowels}")
