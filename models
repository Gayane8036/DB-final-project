from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Creator(Base):
    __tablename__ = 'creators'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    birth_year = Column(Integer)
    death_year = Column(Integer, nullable=True)
    country = Column(String)
    main_focus = Column(String)

class Artwork(Base):
    __tablename__ = 'artworks'

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String)
    cost = Column(Float)
    title = Column(String)
    dimensions = Column(String)
    material = Column(String)
    creator_id = Column(Integer, ForeignKey('creators.id'))

    creator = relationship("Creator", back_populates="artworks")

class StoragePlace(Base):
    __tablename__ = 'storage_places'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    type = Column(String)
    country = Column(String)
    opening_date = Column(Date)

Creator.artworks = relationship("Artwork", back_populates="creator")


