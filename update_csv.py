import requests
import csv

# URL JSON-данных
url = "https://api.geckoterminal.com/api/v2/networks/ton/pools/EQAf2LUJZMdxSAGhlp-A60AN9bqZeVM994vCOXH05JFo-7dc"

# Получаем данные
response = requests.get(url)
data = response.json()

# Извлекаем нужные данные
attributes = data['data']['attributes']
csv_data = [
    ["Token Name", "Price (USD)", "Price Change 24h (%)", "Volume (USD)", "Reserve (USD)"],
    [
        attributes['name'],
        attributes['base_token_price_usd'],
        attributes['price_change_percentage']['h24'],
        attributes['volume_usd']['h24'],
        attributes['reserve_in_usd']
    ]
]

# Записываем в CSV
with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(csv_data)
