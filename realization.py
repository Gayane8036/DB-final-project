from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import crud, scheme 
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
