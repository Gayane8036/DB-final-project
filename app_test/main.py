from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import SessionLocal, engine
from models import Base
from schemas import CreatorCreate, ArtworkCreate, StorageCreate, CreatorResponse, ArtworkResponse, StorageResponse
import crud

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Маршруты для Creator
@app.post("/creators/", response_model=CreatorResponse)
def create_creator(creator: CreatorCreate, db: Session = Depends(get_db)):
    return crud.create_creator(db=db, creator=creator)


@app.get("/creators/", response_model=List[CreatorResponse])
def get_creators(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_creators(db=db, skip=skip, limit=limit)


@app.get("/creators/{creator_id}", response_model=CreatorResponse)
def get_creator(creator_id: int, db: Session = Depends(get_db)):
    creator = crud.get_creator(db=db, creator_id=creator_id)
    if not creator:
        raise HTTPException(status_code=404, detail="Creator not found")
    return creator


# Маршруты для Artwork
@app.post("/artworks/", response_model=ArtworkResponse)
def create_artwork(artwork: ArtworkCreate, db: Session = Depends(get_db)):
    return crud.create_artwork(db=db, artwork=artwork)


@app.get("/artworks/", response_model=List[ArtworkResponse])
def get_artworks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_artworks(db=db, skip=skip, limit=limit)


@app.get("/artworks/{artwork_id}", response_model=ArtworkResponse)
def get_artwork(artwork_id: int, db: Session = Depends(get_db)):
    artwork = crud.get_artwork(db=db, artwork_id=artwork_id)
    if not artwork:
        raise HTTPException(status_code=404, detail="Artwork not found")
    return artwork


# Маршруты для StoragePlace
@app.post("/storage_places/", response_model=StorageResponse)
def create_storage_place(storage_place: StorageCreate, db: Session = Depends(get_db)):
    return crud.create_storage_place(db=db, storage_place=storage_place)


@app.get("/storage_places/", response_model=List[StorageResponse])
def get_storage_places(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_storage_places(db=db, skip=skip, limit=limit)


@app.get("/storage_places/{storage_place_id}", response_model=StorageResponse)
def get_storage_place(storage_place_id: int, db: Session = Depends(get_db)):
    storage_place = crud.get_storage_place(db=db, storage_place_id=storage_place_id)
    if not storage_place:
        raise HTTPException(status_code=404, detail="Storage place not found")
    return storage_place

@app.get("/creators/filter", response_model=List[CreatorResponse])
def filter_creators(name: str = "", min_age: int = 0, db: Session = Depends(get_db)):
    return crud.filter_creators(db=db, name=name, min_age=min_age)
    
@app.get("/artworks_by_creator/{creator_id}", response_model=List[ArtworkResponse])
def get_artworks_by_creator(creator_id: int, db: Session = Depends(get_db)):
    return crud.get_artworks_by_creator(db=db, creator_id=creator_id)

@app.put("/artworks/{artwork_id}", response_model=ArtworkResponse)
def update_artwork(artwork_id: int, artwork: ArtworkCreate, db: Session = Depends(get_db)):
    return crud.update_artwork(db=db, artwork_id=artwork_id, artwork=artwork)

@app.get("/creators/artworks_count", response_model=List[CreatorResponse])
def get_creators_with_artworks_count(db: Session = Depends(get_db)):
    return crud.get_creators_with_artworks_count(db=db)
    
@app.get("/creators/sorted", response_model=List[CreatorResponse])
def get_sorted_creators(sort_by: str = "name", db: Session = Depends(get_db)):
    return crud.get_sorted_creators(db=db, sort_by=sort_by)

