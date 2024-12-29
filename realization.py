from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import CRUD, scheme
from database import SessionLocal, engine

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

@app.post("/creators/", response_model=schemas.Creator)
def create_creator(creator: schemas.Creator, db: Session = Depends(get_db)):
    return crud.create_creator(db=db, creator=creator)

@app.post("/artworks/", response_model=schemas.Artwork)
def create_artwork(artwork: schemas.Artwork, db: Session = Depends(get_db)):
    return crud.create_artwork(db=db, artwork=artwork)

@app.post("/storage_places/", response_model=schemas.StoragePlace)
def create_storage_place(storage_place: schemas.StoragePlace, db: Session = Depends(get_db)):
    return crud.create_storage_place(db=db, storage_place=storage_place)
