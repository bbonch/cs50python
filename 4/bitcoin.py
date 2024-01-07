import sys

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument ")

try:
    count = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

import requests

try:
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    r_json = r.json()
    price = r_json["bpi"]["USD"]["rate_float"]

    print(f"${price * count:,.4f}")
except requests.RequestException:
    pass
