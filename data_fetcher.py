import os
import requests
from time import sleep

app_base_path = os.getenv("APP_BASE_PATH", default=os.getcwd())
data_base_path = os.path.join(app_base_path, "inference-data")
tokens = ['BTC', 'ETH', 'SOL', 'ARB', 'BNB']

def download_data_from_middle_vps(token):
    url = f"http://37.27.31.69:5000/price/{token}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        os.makedirs(data_base_path, exist_ok=True)
        file_name = os.path.join(data_base_path, f'{token}.txt')
        with open(file_name, 'w') as file:
            file.write(str(data))
        print(f'Data for {token} saved to {file_name}')
    else:
        raise ValueError("Failed to fetch data from middle VPS")

def schedule_download():
    while True:
        for token in tokens:
            sleep(10)
            download_data_from_middle_vps(token)
        sleep(300)  # 5 minutes

if __name__ == '__main__':
    schedule_download()

