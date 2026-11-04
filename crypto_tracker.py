import urllib.request
import json

def get_bitcoin_price():
    try:
        url = "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            price = data['bpi']['USD']['rate']
            print(f"💰 Current Bitcoin Price: ${price} USD")
    except Exception as e:
        print(f"Error fetching price: {e}")

if __name__ == "__main__":
    print("=== Hermes Crypto Tracker ===")
    get_bitcoin_price()
