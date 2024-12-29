from pydantic import BaseModel
from datetime import date
from typing import List, Optional

class CreatorCreate(BaseModel):
    name: str
    birth_year: int
    death_year: Optional[int] = None
    country: str
    main_focus: str 

class CreatorResponse(BaseModel):
    id: int
    name: str
    birth_year: int
    death_year: Optional[int]
    country: str
    main_focus: str 

    class Config:
        orm_mode = True

class ArtworkCreate(BaseModel):
    type: str
    cost: float
    title: str
    dimensions: str
    material: str
    creator_id: int
    storage_id: int  

class ArtworkResponse(BaseModel):
    id: int
    type: str
    cost: float
    title: str
    dimensions: str
    material: str
    creator_id: int
    storage_id: int

    class Config:
        orm_mode = True

class StorageCreate(BaseModel):
    name: str
    type: str
    country: str
    opening_date: date

class StorageResponse(BaseModel):
    id: int
    name: str
    type: str
    country: str
    opening_date: date

    class Config:
        orm_mode = True
