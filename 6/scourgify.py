import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

file = sys.argv[1]
rows = []
try:
    with open(file, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            last, first = row["name"].split(",")
            rows.append({"first": first.strip(), "last": last, "house": row["house"]})
except FileNotFoundError:
    sys.exit(f"Could not read {file}")

with open(sys.argv[2],"w") as f:
    field_names = ["first","last","house"]
    writer = csv.DictWriter(f,fieldnames=field_names)

    writer.writeheader()
    for row in rows:
        writer.writerow(row)
