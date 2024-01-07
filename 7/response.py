import validators

email = input("What's your email address? ")

print("Valid" if validators.email(email) else "Invalid")
