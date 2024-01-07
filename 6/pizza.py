import csv
import tabulate
import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

file_ext = sys.argv[1].split(".")
if len(file_ext) != 2 or file_ext[1] != "csv":
    sys.exit("Not a CSV file")

file = sys.argv[1]

try:
    with open(file, "r") as f:
        reader = csv.reader(f)
        print(tabulate.tabulate(reader, headers="firstrow", tablefmt="grid"))
except FileNotFoundError:
    sys.exit("File does not exist")
