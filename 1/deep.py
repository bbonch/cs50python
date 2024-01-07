text = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
words = ["42", "forty two", "forty-two"]
if text.strip().lower() in words:
    print("Yes")
else:
    print("No")
