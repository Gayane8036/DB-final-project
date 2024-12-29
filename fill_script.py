import requests
from faker import Faker
import random

fake = Faker()

def generate_creators(n):
    creators = []
    for _ in range(n):
        creators.append({
            "name": fake.name(),
            "birth_year": random.randint(1800, 2000),
            "death_year": random.randint(1800, 2000) if random.choice([True, False]) else None,
            "country": fake.country(),
            "main_focus": fake.word()
        })
    return creators

def generate_artworks(n, creator_ids, storage_ids):
    artworks = []
    for _ in range(n):
        artworks.append({
            "type": random.choice(["Painting", "Sculpture", "Drawing"]),
            "cost": round(random.uniform(1000, 1000000), 2),
            "title": fake.sentence(),
            "dimensions": f"{random.randint(20, 100)} cm x {random.randint(20, 100)} cm",
            "material": fake.word(),
            "creator_id": random.choice(creator_ids),
            "storage_id": random.choice(storage_ids)
        })
    return artworks

def generate_storages(n):
    storages = []
    for _ in range(n):
        storages.append({
            "name": fake.company(),
            "type": random.choice(["Museum", "Gallery"]),
            "country": fake.country(),
            "opening_date": fake.date_this_century()
        })
    return storages

def bulk_create_data():
    creators = generate_creators(100)
    artworks = generate_artworks(200, range(1, 101), range(1, 51))
    storages = generate_storages(50)

    requests.post("http://127.0.0.1:8000/creators/bulk/", json=creators)
    requests.post("http://127.0.0.1:8000/artworks/bulk/", json=artworks)
    requests.post("http://127.0.0.1:8000/storage_places/bulk/", json=storages)

bulk_create_data()
