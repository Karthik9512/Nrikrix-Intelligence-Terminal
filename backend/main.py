from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Bloomberg Terminal API running"}

@app.get("/crypto/{coin}")
def get_crypto(coin: str):

    url = "https://api.coingecko.com/api/v3/simple/price"

    params = {
        "ids": coin,
        "vs_currencies": "usd"
    }

    response = requests.get(url, params=params)

    return response.json()

@app.get("/market/global")
def global_market():

    url = "https://api.coingecko.com/api/v3/simple/price"

    coins = ["bitcoin", "ethereum", "solana"]

    params = {
        "ids": ",".join(coins),
        "vs_currencies": "usd"
    }

    response = requests.get(url, params=params)

    data = response.json()

    result = []

    for coin in coins:
        result.append({
            "coin": coin,
            "price": data.get(coin, {}).get("usd")
        })

    return result