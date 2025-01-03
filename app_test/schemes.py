from pydantic import BaseModel
from typing import Optional, List


# Схемы для Creator
class CreatorBase(BaseModel):
    full_name: str
    country: str
    years_of_life: Optional[str] = None
    main_direction: Optional[str] = None


class CreatorCreate(CreatorBase):
    pass


class CreatorResponse(CreatorBase):
    id: int
    artworks: List["ArtworkResponse"] = []

    class Config:
        orm_mode = True


# Схемы для Artwork
class ArtworkBase(BaseModel):
    title: str
    type: str
    dimensions: Optional[str] = None
    material: Optional[str] = None
    price: Optional[float] = None
    creator_id: int
    storage_place_id: int


class ArtworkCreate(ArtworkBase):
    pass


class ArtworkResponse(ArtworkBase):
    id: int
    creator: CreatorResponse
    storage_place: "StorageResponse"

    class Config:
        orm_mode = True


# Схемы для StoragePlace
class StorageBase(BaseModel):
    name: str
    type: str
    country: str
    opening_date: Optional[str] = None


class StorageCreate(StorageBase):
    pass


class StorageResponse(StorageBase):
    id: int
    artworks: List[ArtworkResponse] = []

    class Config:
        orm_mode = True
