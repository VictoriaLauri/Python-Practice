import sys
import requests

if len(sys.argv) != 2:
    sys.exit("Incorrect amount of arguments")

try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    file = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except requests.RequestException:
    sys.exit("Could not load API")

info = file.json()
rate = info["bpi"]["USD"]["rate_float"]
result = rate * n

print(f"${result:,.4f}")
