months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

while True:
    try:
        text = input("Date: ")

        parts = text.split("/")
        year = 0
        month = 0
        day = 0
        if len(parts) == 3:
            year = int(parts[2])
            month = int(parts[0])
            day = int(parts[1])
        else:
            parts = text.split(", ")
            year = int(parts[1])
            parts = parts[0].split(" ")
            if parts[0] in months:
                month = months.index(parts[0]) + 1
                day = int(parts[1])
            else:
                continue

        if day > 31 or month > 12:
            continue
        print(f"{year}-{month:02}-{day:02}")
        break
    except (ValueError, IndexError):
        pass
