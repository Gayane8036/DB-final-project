from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import crud, schemas
from database import SessionLocal, engine

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

@app.post("/creators/", response_model=scheme.CreatorResponse)
def create_creator(creator: scheme.CreatorCreate, db: Session = Depends(get_db)):
    return crud.create_creator(db=db, creator=creator)

@app.post("/artworks/", response_model=scheme.ArtworkResponse)
def create_artwork(artwork: scheme.ArtworkCreate, db: Session = Depends(get_db)): 
    return crud.create_artwork(db=db, artwork=artwork)

@app.post("/storage_places/", response_model=scheme.StorageResponse)
def create_storage_place(storage_place: scheme.StorageCreate, db: Session = Depends(get_db)):
    return crud.create_storage_place(db=db, storage_place=storage_place)

@app.post("/creators/bulk/", response_model=List[scheme.CreatorResponse])
def create_creators(creators: List[scheme.CreatorCreate], db: Session = Depends(get_db)):
    return [crud.create_creator(db=db, creator=creator) for creator in creators]

@app.post("/artworks/bulk/", response_model=List[scheme.ArtworkResponse])
def create_artworks(artworks: List[scheme.ArtworkCreate], db: Session = Depends(get_db)):
    return [crud.create_artwork(db=db, artwork=artwork) for artwork in artworks]

@app.post("/storage_places/bulk/", response_model=List[scheme.StorageResponse])
def create_storage_places(storage_places: List[scheme.StorageCreate], db: Session = Depends(get_db)):
    return [crud.create_storage_place(db=db, storage_place=storage_place) for storage_place in storage_places]
