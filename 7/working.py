import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    r = re.search(
        r"(?P<hour1>\d{1,2})(?::(?P<minute1>\d{1,2}))? (?P<part1>[A|P]M) to (?P<hour2>\d{1,2})(?::(?P<minute2>\d{1,2}))? (?P<part2>[A|P]M)",
        s,
    )
    if r:
        hour1 = int(r.group("hour1"))
        if hour1 > 12:
            raise ValueError

        minute1 = r.group("minute1")
        if minute1 and int(minute1) > 59:
            raise ValueError

        part1 = r.group("part1")

        hour2 = int(r.group("hour2"))
        if hour2 > 12:
            raise ValueError

        minute2 = r.group("minute2")
        if minute2 and int(minute2) > 59:
            raise ValueError

        part2 = r.group("part2")

        return f"{time_24(hour1, part1, minute1)} to {time_24(hour2,part2,minute2)}"
    else:
        raise ValueError


def time_24(hour, part, minute=None):
    if hour == 12:
        hour = 0
    if part == "PM":
        hour += 12
    minute_str = minute if minute else "00"
    time = f"{hour:02}:{minute_str}"

    return time


if __name__ == "__main__":
    main()
