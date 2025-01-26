import requests

# URL вашего Google Apps Script
url = "https://script.google.com/macros/s/AKfycbynvcsGmjGBGaUCe1V1bfrGaqUbm_IyVmZKx6WmI5s3uUwHZ4DIgAg-iMSVBrW_i1v3/exec"

# Локальный путь к файлу CSV
csv_file_path = "data.csv"

try:
    # Запрос данных с вашей ссылки
    response = requests.get(url)
    response.raise_for_status()  # Проверяем успешность запроса

    # Проверяем, что ответ содержит данные в формате CSV
    if "text/csv" in response.headers.get("Content-Type", ""):
        # Сохраняем CSV данные в локальный файл
        with open(csv_file_path, "w", encoding="utf-8") as file:
            file.write(response.text)
        print(f"CSV файл обновлен: {csv_file_path}")
    else:
        print("Ошибка: URL возвращает не CSV-данные.")

except requests.RequestException as e:
    print(f"Ошибка при запросе данных: {e}")
