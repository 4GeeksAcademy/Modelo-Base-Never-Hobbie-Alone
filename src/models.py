import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

eventos = Table('eventos', Base.metadata,
    Column('evento_id', Integer, ForeignKey('evento.id'), primary_key=True),
    Column('user_id', Integer, ForeignKey('user.id'), primary_key=True)
)

hobbies = Table('hobbies', Base.metadata,
    Column('categoria_id', Integer, ForeignKey('categoria.id'), primary_key=True),
    Column('user_id', Integer, ForeignKey('user.id'), primary_key=True)
)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=True)
    email = Column(String(250), nullable=True)
    pwd = Column(String(250), nullable=True)
    eventos = relationship('Evento', secondary=eventos, backref= 'user', lazy=True)
    hobbies = relationship('Categoria', secondary=eventos, backref= 'user', lazy=True)
    creado = relationship('Evento', backref='user', lazy=True)

class Evento(Base):
    __tablename__ = 'evento'
    id = Column(Integer, primary_key=True)
    evento = Column(String(250), nullable=True)
    ciudad = Column(String(250), nullable=True)
    ubicación = Column(String(250), nullable=True)
    max_personas = Column(Integer, nullable=True)
    id_categoria = Column(Integer, ForeignKey('categoria.id'), nullable=False)
    user_creador = Column(Integer, ForeignKey('user.id'), nullable=False)

class Categoria(Base):
    __tablename__ = 'categoria'
    id = Column(Integer, primary_key=True)
    tipo = Column(String(250), nullable=True)
    categoria = Column(String(250), nullable=True)
    eventos = relationship('Evento', backref='categoria', lazy=True)

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
