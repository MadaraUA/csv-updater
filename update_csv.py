def fetch_and_create_csv():
    # URL API
    url = "https://api.geckoterminal.com/api/v2/networks/ton/pools/EQAf2LUJZMdxSAGhlp-A60AN9bqZeVM994vCOXH05JFo-7dc"

    try:
        # Получение данных
        response = requests.get(url)
        response.raise_for_status()  # Проверка на ошибки

        # Вывод полного ответа для диагностики
        print("API Response:", response.json())

        data = response.json()["data"]["attributes"]

        # Форматирование данных
        token_name = data["name"]
        price_usd = round(float(data["base_token_price_usd"]), 2)
        price_change = round(float(data["price_change_percentage"]["h24"]), 2)
        volume_usd = round(float(data["volume_usd"]["h24"]), 2)
        reserve_usd = round(float(data["reserve_in_usd"]), 2)

        # Запись в CSV
        csv_data = [
            ["Token Name", "Price (USD)", "Price Change (24h %)", "Trading Volume (24h USD)", "Reserve (USD)"],
            [token_name, price_usd, price_change, volume_usd, reserve_usd]
        ]

        with open("data.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(csv_data)

        print("CSV файл обновлен.")

    except requests.RequestException as e:
        print(f"Ошибка при запросе данных: {e}")
