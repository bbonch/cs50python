import sys

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

valid_ext = ["png", "jpg", "jpeg"]
input_ext = sys.argv[1].split(".")
if len(input_ext) != 2 or input_ext[1] not in valid_ext:
    sys.exit("Invalid output")

output_ext = sys.argv[2].split(".")
if output_ext[1] != input_ext[1]:
    sys.exit("Input and output have different extensions")

input = sys.argv[1]
output = sys.argv[2]
try:
    from PIL import Image, ImageOps

    with Image.open(input) as im:
        with Image.open("shirt.png") as shirt:
            size = shirt.size
            im = ImageOps.fit(im, size)
            im.paste(shirt,shirt)
            im.save(output)

except FileNotFoundError:
    sys.exit("Input does not exist")
