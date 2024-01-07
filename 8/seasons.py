from datetime import date
import sys
import inflect


def main():
    print(convert(input("Date of Birth: "), date.today()))


def convert(str, now):
    try:
        year, month, day = str.split("-")
        bd = date(int(year), int(month), int(day))
    except ValueError:
        sys.exit("Invalid date")

    delta = now - bd
    delta_minutes = round(delta.total_seconds() / 60)
    
    p = inflect.engine()
    converted = p.number_to_words(delta_minutes).capitalize().replace("and ", "")

    return f"{converted} minutes"


if __name__ == "__main__":
    main()
