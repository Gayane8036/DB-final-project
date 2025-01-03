import requests

# Базовый URL вашего приложения FastAPI
BASE_URL = "http://127.0.0.1:8000"

# Данные для заполнения
creators_data = [
    {"full_name": "Leonardo da Vinci", "country": "Italy", "life_years": "1452-1519", "main_direction": "Renaissance"},
    {"full_name": "Vincent van Gogh", "country": "Netherlands", "life_years": "1853-1890", "main_direction": "Post-Impressionism"},
    {"full_name": "Pablo Picasso", "country": "Spain", "life_years": "1881-1973", "main_direction": "Cubism"},
]

artworks_data = [
    {"name": "Mona Lisa", "type": "Painting", "dimensions": "77 x 53 cm", "material": "Oil on poplar", "cost": 1000000, "creator_id": 1},
    {"name": "Starry Night", "type": "Painting", "dimensions": "73.7 x 92.1 cm", "material": "Oil on canvas", "cost": 900000, "creator_id": 2},
    {"name": "Guernica", "type": "Painting", "dimensions": "349 x 776 cm", "material": "Oil on canvas", "cost": 1200000, "creator_id": 3},
]

storage_places_data = [
    {"name": "Louvre Museum", "type": "Museum", "country": "France", "opening_date": "1793-08-10"},
    {"name": "Van Gogh Museum", "type": "Museum", "country": "Netherlands", "opening_date": "1973-06-02"},
    {"name": "Museo Reina Sofía", "type": "Museum", "country": "Spain", "opening_date": "1992-09-10"},
]

# Функция для отправки POST-запросов
def post_data(endpoint, data):
    url = f"{BASE_URL}/{endpoint}/"
    response = requests.post(url, json=data)
    if response.status_code == 200:
        print(f"Добавлено: {data}")
    else:
        print(f"Ошибка: {response.status_code}, {response.text}")

# Заполнение данных
print("Добавляем создателей...")
for creator in creators_data:
    post_data("creators", creator)

print("Добавляем произведения...")
for artwork in artworks_data:
    post_data("artworks", artwork)

print("Добавляем места хранения...")
for storage_place in storage_places_data:
    post_data("storage_places", storage_place)
