import requests
import pandas as pd
import schedule
import time
from datetime import datetime

coins = ["bitcoin", "ethereum", "solana"]

def fetch_prices():

    url = "https://api.coingecko.com/api/v3/simple/price"

    params = {
        "ids": ",".join(coins),
        "vs_currencies": "usd"
    }

    response = requests.get(url, params=params)
    data = response.json()

    rows = []

    for coin in coins:

        if coin not in data:
            continue

        rows.append({
            "coin": coin,
            "price": data[coin]["usd"],
            "time": datetime.now()
        })

    if rows:
        df = pd.DataFrame(rows)
        df.to_csv("market_data.csv", mode="a", header=False, index=False)
        print(df)


schedule.every(30).seconds.do(fetch_prices)

print("Market collector running...")

while True:
    schedule.run_pending()
    time.sleep(1)