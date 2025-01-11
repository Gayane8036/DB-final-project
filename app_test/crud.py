from sqlalchemy.orm import Session
from models import Creator, Artwork, StoragePlace
from schemas import CreatorCreate, ArtworkCreate, StorageCreate
from sqlalchemy import select
from sqlalchemy.orm import joinedload
from sqlalchemy import func
from sqlalchemy import asc, desc

# CRUD операции для Creator
def create_creator(db: Session, creator: CreatorCreate):
    db_creator = Creator(
        full_name=creator.full_name,
        country=creator.country,
        years_of_life=creator.years_of_life,
        main_direction=creator.main_direction
    )
    db.add(db_creator)
    db.commit()
    db.refresh(db_creator)
    return db_creator


def get_creator(db: Session, creator_id: int):
    return db.query(Creator).filter(Creator.id == creator_id).first()


def get_creators(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Creator).offset(skip).limit(limit).all()


# CRUD операции для Artwork
def create_artwork(db: Session, artwork: ArtworkCreate):
    db_artwork = Artwork(
        title=artwork.title,
        type=artwork.type,
        dimensions=artwork.dimensions,
        material=artwork.material,
        price=artwork.price,
        creator_id=artwork.creator_id,
        storage_place_id=artwork.storage_place_id
    )
    db.add(db_artwork)
    db.commit()
    db.refresh(db_artwork)
    return db_artwork


def get_artwork(db: Session, artwork_id: int):
    return db.query(Artwork).filter(Artwork.id == artwork_id).first()


def get_artworks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Artwork).offset(skip).limit(limit).all()


# CRUD операции для StoragePlace
def create_storage_place(db: Session, storage_place: StorageCreate):
    db_storage_place = StoragePlace(
        name=storage_place.name,
        type=storage_place.type,
        country=storage_place.country,
        opening_date=storage_place.opening_date
    )
    db.add(db_storage_place)
    db.commit()
    db.refresh(db_storage_place)
    return db_storage_place


def get_storage_place(db: Session, storage_place_id: int):
    return db.query(StoragePlace).filter(StoragePlace.id == storage_place_id).first()


def get_storage_places(db: Session, skip: int = 0, limit: int = 100):
    return db.query(StoragePlace).offset(skip).limit(limit).all()


def filter_creators(db: Session, name: str, min_age: int):
    query = select(Creator).where(Creator.name.ilike(f"%{name}%"), Creator.age >= min_age)
    result = db.execute(query).scalars().all()
    return result


def get_artworks_by_creator(db: Session, creator_id: int):
    query = select(Artwork).join(Creator).filter(Creator.id == creator_id)
    result = db.execute(query).scalars().all()
    return result


def update_artwork(db: Session, artwork_id: int, artwork: ArtworkCreate):
    db_artwork = db.query(Artwork).filter(Artwork.id == artwork_id).first()
    if db_artwork:
        if artwork.year > 2000:
            db_artwork.title = artwork.title
            db_artwork.year = artwork.year
            db.commit()
            db.refresh(db_artwork)
            return db_artwork
    return None

def get_creators_with_artworks_count(db: Session):
    query = select(Creator.name, func.count(Artwork.id)).join(Artwork).group_by(Creator.id)
    result = db.execute(query).fetchall()
    return result


def get_sorted_creators(db: Session, sort_by: str):
    sort_column = getattr(Creator, sort_by)
    query = select(Creator).order_by(sort_column)
    result = db.execute(query).scalars().all()
    return result


