text = input("Expression: ")

x, y, z = text.split(" ")
xi = int(x)
zi = int(z)
r = 0

match y:
    case "+":
        r = xi + zi
    case "-":
        r = xi - zi
    case "*":
        r = xi * zi
    case "/":
        r = xi / zi

print(f"{r:.1f}")
