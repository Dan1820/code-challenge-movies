from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base


class Movie():
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


class Actor():
    __tablename__ = 'actors'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    roles = relationship('Role', back_populates='actor')
    movies = relationship('Movie', secondary='role', back_populates='actors')

    def actor_roles(self):
        return self.roles

    def actor_movies(self):
        return self.movies

    def total_salary(self):
        return sum(role.salary for role in self.roles)

    def blackbusters(self):
        return [movie for movie in self.movies if movie.box_office_earnings > 50000000]

    @classmethod
    def most_successful(cls):
        pass
        # return max(cls.query.all(), key=lambda role_actor: role_actor.total_salary())


class Role():
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey('movies.id'))
    actor_id = Column(Integer, ForeignKey('actors.id'))
    salary = Column(Integer)
    character_name = Column(String)
    movie = relationship('Movie', back_populates='roles')
    actor = relationship('Actor', back_populates='roles')

    def role_actor(self):
        return self.actor

    def role_movie(self):
        return self.movie

    def credit(self):
        return f"{self.character_name}: Played by {self.actor.name}"
