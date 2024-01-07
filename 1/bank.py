text = input("Greeting: ")
text_lower = text.strip().lower()
if text_lower.startswith("hello"):
    print("$0")
elif text_lower.startswith("h"):
    print("$20")
else:
    print("$100")
