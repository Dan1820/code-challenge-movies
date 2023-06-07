from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import (create_engine, PrimaryKeyConstraint,
                        Column, String, Integer, ForeignKey)
import os
import sys

sys.path.append(os.getcwd)


Base = declarative_base()

engine = create_engine('sqlite:///db/movies.db', echo=True)

# class Role(Base):
#     pass


class Actor(Base):
    # __tablename__ = 'actors'

    # id = Column(Integer, primary_key=True)
    # name = Column(String())

    # movies = relationship("Movie", secondary="", back_populates="actor")
    __tablename__ = 'actors'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    roles = relationship('Role', back_populates='actor')
    movies = relationship('Movie', secondary='role', back_populates='actors')

    def actor_roles(self):
        return self.roles

    def movie_actor(self):
        return self.movies

    def __repr__(self):
        return f'Actor: {self.name}'


class Movie(Base):
    # __tablename__ = 'movies'

    # id = Column(Integer, primary_key=True)
    # title = Column(String())
    # box_office_earnings = Column(Integer())

    # actors = relationship("Role", back_populates="movie")

    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    box_office_earnings = Column(Integer)
    roles = relationship('Role', back_populated="movie")
    actors = relationship('Actor', secondary='roles', back_populates='movies')

    def movie_roles(self):
        return self.roles

    def movie_actors(self):
        return self.actors

    def cast_role(self, actor, character_name, salary):
        role = Role(actor=actor, movie=self,
                    character_name=character_name, salary=salary)
        self.roles.append(role)

    def all_credits(self):
        return [role.credit() for role in self.roles]

    def fire_actor(self, actor):
        role = next((r for r in self.roles if r.actor == actor), None)
        if role:
            self.roles.remove(role)

    def __repr__(self):
        return f'Movie: {self.title}'


class Role():
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey('movies.id'))
    actor_id = Column(Integer, ForeignKey('actors.id'))
    salary = Column(Integer)
    character_name = Column(String)
    movie = relationship('Movie', back_populates='roles')
    actor = relationship('Actor', back_populates='roles')

    def actors(self):
        return self.actor

    def movies(self):
        return self.movie
