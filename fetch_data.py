import requests

def download_data(token):
    url = f'https://api.binance.com/api/v3/ticker/price?symbol={token}USDT'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        file_name = f'inference-data/{token}.txt'
        with open(file_name, 'w') as file:
            file.write(data['price'])
        print(f'Data for {token} saved to {file_name}')
    else:
        print(f'Failed to fetch data for {token}, status code: {response.status_code}')

if __name__ == '__main__':
    tokens = ['BTC', 'ETH', 'SOL', 'ARB', 'BNB']
    for token in tokens:
        download_data(token)
