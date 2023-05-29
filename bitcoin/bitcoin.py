import requests
import sys

# Check if command-line argument is provided and can be converted to float
if len(sys.argv) < 2:
    sys.exit("Please provide the number of Bitcoins to buy as a command-line argument")
try:
    num_bitcoins = float(sys.argv[1])
except ValueError:
    sys.exit("Invalid argument. Please provide a number for the number of Bitcoins to buy")

# Query the API for the current price of Bitcoin in USD
try:
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = response.json()
    current_price = float(data['bpi']['USD']['rate_float'])
except (requests.RequestException, ValueError, KeyError):
    sys.exit("Error occurred while fetching Bitcoin price")

# Calculate the cost of the specified number of Bitcoins in USD
cost = num_bitcoins * current_price

# Output the cost in USD with four decimal places and a thousands separator
print(f"The cost of {num_bitcoins} Bitcoins is ${cost:,.4f}")