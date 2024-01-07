grocery = {}

while True:
    try:
        text = input()

        key = text.strip().lower()
        if key in grocery:
            grocery[key] += 1
        else:
            grocery[key] = 1
    except EOFError:
        break

for key in sorted(grocery.keys()):
    print(f"{grocery[key]} {key.upper()}")