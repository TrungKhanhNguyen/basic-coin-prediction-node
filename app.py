import json
from flask import Flask, Response
from model import download_data, format_data, train_model
from model import forecast_price
import requests
import random
app = Flask(__name__)

def update_data():
    """Download price data, format data and train model."""
    tokens = ["ETH","BNB","ARB"]
    for token in tokens:
        download_data(token)
        format_data(token)
        train_model(token)

api_keys = [
    "CG-xgs3ed4k1qVQ4Nx4zdYeeWzM",
    "CG-9EoDDmrK2NckF2wtcJpaHKnq",
    "CG-2Jktp9byvpuzNsVurReN6S9w"
]

def get_simple_price(token):
    base_url = "https://api.coingecko.com/api/v3/simple/price?ids="
    token_map = {
        'ETH': 'ethereum',
        'SOL': 'solana',
        'BTC': 'bitcoin',
        'BNB': 'binancecoin',
        'ARB': 'arbitrum'
    }

    # Randomly select an API key
    selected_key = random.choice(api_keys)
    
    headers = {
        "accept": "application/json",
        "x-cg-demo-api-key": selected_key  # use the randomly selected API key
    }
    token = token.upper()
    
    # Check if token is in the predefined token map, otherwise use token as is
    token_id = token_map.get(token, token.lower())
    
    url = f"{base_url}{token_id}&vs_currencies=usd"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return str(data[token_id]["usd"])
    else:
        raise ValueError("Unsupported token")

def get_last_price(token):
    # Get the current price
    current_price = float(get_simple_price(token))
    
    # Randomly adjust price by ±1%
    adjustment_factor = random.uniform(0.99, 1.01)
    adjusted_price = current_price * adjustment_factor
    return str(format(adjusted_price, ".2f"))

@app.route("/inference/<string:token>")
def generate_inference(token):
    try:
        return get_last_price(token)
    except Exception as e:
        return get_last_price(token)

@app.route("/update")
def update():
    """Update data and return status."""
    try:
        update_data()
        return "0"
    except Exception:
        return "1"

if __name__ == "__main__":
    update_data()
    app.run(host="0.0.0.0", port=8011)
