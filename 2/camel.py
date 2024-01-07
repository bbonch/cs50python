cc = input("camelCase: ")

sc = ""
for i in cc:
    if i.isupper():
        sc += f"_{i.lower()}"
    else:
        sc += i

print(f"snake_case: {sc}")
