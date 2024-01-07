import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

file_ext = sys.argv[1].split(".")
if len(file_ext) != 2 or file_ext[1] != "py":
    sys.exit("Not a Python file")

file = sys.argv[1]
try:
    with open(file, mode="r") as f:
        lines = f.readlines()
except FileNotFoundError:
    sys.exit("File does not exist")

count = 0
for line in lines:
    line = line.lstrip().rstrip("\n")
    if not (line.startswith("#") or line == ""):
        count += 1

print(count)
