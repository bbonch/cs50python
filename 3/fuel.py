def main():
    fuel = get_fuel()

    if fuel <= 1:
        print("E")
    elif fuel >= 99:
        print("F")
    else:
        print(f"{round(fuel)}%")


def get_fuel():
    while True:
        text = input("Fraction: ")

        try:
            x, y = text.split("/")
            fuel = int(x) / int(y) * 100

            if fuel > 100 or fuel < 0:
                pass
            else:
                return fuel
        except (ValueError, ZeroDivisionError):
            pass


if __name__ == "__main__":
    main()
