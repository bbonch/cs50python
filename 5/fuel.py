def main():
    while True:
        text = input("Fraction: ")

        try:
            percentage = convert(text)
            gauge = gauge(percentage)

            print(gauge)
        except (ValueError, ZeroDivisionError):
            pass


def convert(fraction):
    try:
        x, y = fraction.split("/")
        fuel = int(x) / int(y) * 100

        if fuel > 100 or fuel < 0:
            raise ValueError
        else:
            return fuel
    except (ValueError, ZeroDivisionError):
        raise


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{round(percentage)}%"


if __name__ == "__main__":
    main()
