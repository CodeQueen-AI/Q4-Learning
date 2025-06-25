import requests

class CryptoDataAgent:
    def __init__(self):
        self.base_url = "https://api.binance.com/api/v3/ticker/price"

    def get_price(self, symbol: str):
        symbol = symbol.upper()
        if not symbol.endswith("USDT"):
            symbol += "USDT"
        url = f"{self.base_url}?symbol={symbol}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data["price"]
        else:
            return None
