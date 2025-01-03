from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Creator(Base):
    __tablename__ = "creators"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    country = Column(String, nullable=False)
    years_of_life = Column(String, nullable=True)
    main_direction = Column(String, nullable=True)

    artworks = relationship("Artwork", back_populates="creator")


class Artwork(Base):
    __tablename__ = "artworks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    type = Column(String, nullable=False)
    dimensions = Column(String, nullable=True)
    material = Column(String, nullable=True)
    price = Column(Float, nullable=True)
    creator_id = Column(Integer, ForeignKey("creators.id"), nullable=False)
    storage_place_id = Column(Integer, ForeignKey("storage_places.id"), nullable=False)

    creator = relationship("Creator", back_populates="artworks")
    storage_place = relationship("StoragePlace", back_populates="artworks")


class StoragePlace(Base):
    __tablename__ = "storage_places"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)
    country = Column(String, nullable=False)
    opening_date = Column(String, nullable=True)

    artworks = relationship("Artwork", back_populates="storage_place")
