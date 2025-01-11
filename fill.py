import requests
import random
from faker import Faker

fake = Faker()

BASE_URL = "http://127.0.0.1:8000"

def create_creator():
    creator_data = {
        "full_name": fake.name(),
        "country": fake.country(),
        "years_of_life": f"{random.randint(1800, 1900)} - {random.randint(1900, 2000)}",
        "main_direction": fake.job()
    }
    response = requests.post(f"{BASE_URL}/creators/", json=creator_data)
    return response.json()

def create_storage_place():
    storage_place_data = {
        "name": fake.company(),
        "type": random.choice(["Museum", "Gallery", "Private Collection"]),
        "country": fake.country(),
        "opening_date": f"{random.randint(1900, 2025)}-01-01"
    }
    response = requests.post(f"{BASE_URL}/storage_places/", json=storage_place_data)
    return response.json()

def create_artwork(creator_id, storage_place_id):
    artwork_data = {
        "title": fake.word(),
        "type": random.choice(["Painting", "Sculpture", "Drawing"]),
        "dimensions": f"{random.randint(10, 200)} x {random.randint(10, 200)}",
        "material": random.choice(["Oil on Canvas", "Marble", "Wood", "Clay"]),
        "price": round(random.uniform(100, 10000), 2),
        "creator_id": creator_id,
        "storage_place_id": storage_place_id
    }
    response = requests.post(f"{BASE_URL}/artworks/", json=artwork_data)
    return response.json()

def generate_data(num_creators=10, num_storage_places=5, num_artworks=20):
    storage_places = [create_storage_place() for _ in range(num_storage_places)]
    print("Storage places created")

    creators = [create_creator() for _ in range(num_creators)]
    print("Creators created")

    for artwork in range(num_artworks):
        creator = random.choice(creators)
        storage_place = random.choice(storage_places)
        create_artwork(creator["id"], storage_place["id"])
        print(f"Artwork {artwork + 1} created")

if __name__ == "__main__":
    generate_data()
