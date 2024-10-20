import requests
import os
import random
from time import sleep
api_keys = [
   "CG-fn5Dnv5ujTE8SoQvQP5APwDu",
   "CG-1EU1cAnJdfWCsvCWKPeyjxNS",
   "CG-HXp3Hpa2FJ3pvzHsr3MC28Gn",
   "CG-DoU2GvVr9cr5XDiqVRvmVsN6",
   "CG-ti78Sdc2ixAm9sThFefiRMNx",
   "CG-3MisueQuvysQ364rWc9xW59w",
   "CG-xgs3ed4k1qVQ4Nx4zdYeeWzM",
   "CG-9EoDDmrK2NckF2wtcJpaHKnq",
   "CG-2Jktp9byvpuzNsVurReN6S9w",
   "CG-Lk9W6hsBoN47nBNdpQbdpEZr",
   "CG-JEobnGPeQ9RB1Dgq7UZHJWiP"
]
app_base_path = os.getenv("APP_BASE_PATH", default=os.getcwd())
data_base_path = os.path.join(app_base_path, "inference-data")
def download_data(token):
        
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
        os.makedirs(data_base_path, exist_ok=True)
        file_name = os.path.join(data_base_path, f'{token}.txt')
        with open(file_name, 'w') as file:
            file.write(str(data[token_id]["usd"]))
        print(f'Data for {token} saved to {file_name}')
        #return str(data[token_id]["usd"])
    else:
        raise ValueError("Failed to fetch data")

if __name__ == '__main__':
    tokens = ['BTC', 'ETH', 'SOL']
    for token in tokens:
        download_data(token)
        sleep(5)
