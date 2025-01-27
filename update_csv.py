import requests
import csv

def fetch_and_create_csv():
    url = "https://api.geckoterminal.com/api/v2/networks/ton/pools/EQAf2LUJZMdxSAGhlp-A60AN9bqZeVM994vCOXH05JFo-7dc"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()["data"]["attributes"]

        token_name = data.get("name", "N/A")
        price_usd = round(float(data.get("base_token_price_usd", 0)), 2)
        price_change = round(float(data.get("price_change_percentage", {}).get("h24", 0)), 2)
        volume_usd = round(float(data.get("volume_usd", {}).get("h24", 0)), 2)
        reserve_usd = round(float(data.get("reserve_in_usd", 0)), 2)

        csv_data = [
            ["Token Name", "Price (USD)", "Price Change (24h %)", "Trading Volume (24h USD)", "Reserve (USD)"],
            [token_name, price_usd, price_change, volume_usd, reserve_usd]
        ]
        print(f"Данные для записи: {csv_data}")

        with open("data.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(csv_data)

        print("CSV файл обновлен.")

    except requests.RequestException as e:
        print(f"Ошибка при запросе данных: {e}")
    except KeyError as e:
        print(f"Ошибка доступа к данным: {e}")

fetch_and_create_csv()
