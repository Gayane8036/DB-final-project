from sqlalchemy.orm import Session
from sqlalchemy import select
import models, schemas
from fastapi import HTTPException

def apply_sort(query, sort_by: str, asc: bool, valid_columns: dict):
    if sort_by not in valid_columns:
        raise ValueError(f"Invalid column name: {sort_by}")
    sort_by = valid_columns[sort_by]
    return query.order_by(sort_by.asc() if asc else sort_by.desc())

# Creator CRUD
def create_creator(db: Session, creator_data: schemas.CreatorCreate):
    db_creator = models.Creator(**creator_data.dict())
    db.add(db_creator)
    db.commit()
    db.refresh(db_creator)
    return db_creator

def read_creators(db: Session, sort_by: str = None, asc: bool = True):
    query = select(models.Creator)

    if sort_by:
        try:
            query = apply_sort(query, sort_by, asc, {
                "name": models.Creator.name,
                "birth_year": models.Creator.birth_year,
                "death_year": models.Creator.death_year,
                "country": models.Creator.country,
                "main_focus": models.Creator.main_focus
            })
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))

    return db.execute(query).scalars().all()

def update_creator(db: Session, creator_id: int, creator_data: schemas.CreatorCreate):
    db_creator = db.query(models.Creator).filter(models.Creator.id == creator_id).first()

    if not db_creator:
        return None

    for key, value in creator_data.dict(exclude_none=True).items():
        setattr(db_creator, key, value)

    db.commit()
    db.refresh(db_creator)
    return db_creator

def delete_creator(db: Session, creator_id: int):
    db_creator = db.query(models.Creator).filter(models.Creator.id == creator_id).first()

    if not db_creator:
        return False

    db.delete(db_creator)
    db.commit()
    return True

# Artwork CRUD
def create_artwork(db: Session, artwork_data: schemas.ArtworkCreate):
    db_artwork = models.Artwork(**artwork_data.dict())
    db.add(db_artwork)
    db.commit()
    db.refresh(db_artwork)
    return db_artwork

def read_artworks(db: Session, sort_by: str = None, asc: bool = True):
    query = select(models.Artwork)

    if sort_by:
        try:
            query = apply_sort(query, sort_by, asc, {
                "title": models.Artwork.title,
                "cost": models.Artwork.cost,
                "type": models.Artwork.type,
                "dimensions": models.Artwork.dimensions,
                "material": models.Artwork.material
            })
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))

    return db.execute(query).scalars().all()

def update_artwork(db: Session, artwork_id: int, artwork_data: schemas.ArtworkCreate):
    db_artwork = db.query(models.Artwork).filter(models.Artwork.id == artwork_id).first()

    if not db_artwork:
        return None

    for key, value in artwork_data.dict(exclude_none=True).items():
        setattr(db_artwork, key, value)

    db.commit()
    db.refresh(db_artwork)
    return db_artwork

def delete_artwork(db: Session, artwork_id: int):
    db_artwork = db.query(models.Artwork).filter(models.Artwork.id == artwork_id).first()

    if not db_artwork:
        return False

    db.delete(db_artwork)
    db.commit()
    return True

# Storage CRUD
def create_storage(db: Session, storage_data: schemas.StorageCreate):
    db_storage = models.Storage(**storage_data.dict())
    db.add(db_storage)
    db.commit()
    db.refresh(db_storage)
    return db_storage

def read_storages(db: Session, sort_by: str = None, asc: bool = True):
    query = select(models.Storage)

    if sort_by:
        try:
            query = apply_sort(query, sort_by, asc, {
                "name": models.Storage.name,
                "type": models.Storage.type,
                "country": models.Storage.country,
                "opening_date": models.Storage.opening_date
            })
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))

    return db.execute(query).scalars().all()

def update_storage(db: Session, storage_id: int, storage_data: schemas.StorageCreate):
    db_storage = db.query(models.Storage).filter(models.Storage.id == storage_id).first()

    if not db_storage:
        return None

    for key, value in storage_data.dict(exclude_none=True).items():
        setattr(db_storage, key, value)

    db.commit()
    db.refresh(db_storage)
    return db_storage

def delete_storage(db: Session, storage_id: int):
    db_storage = db.query(models.Storage).filter(models.Storage.id == storage_id).first()

    if not db_storage:
        return False

    db.delete(db_storage)
    db.commit()
    return True
