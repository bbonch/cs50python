names = []
while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        break

import inflect

start = "Adieu, adieu, to "
p = inflect.engine()
print(f"{start}{p.join(names)}")
