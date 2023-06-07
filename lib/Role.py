# from sqlalchemy import Column, Integer, String, ForeignKey
# from sqlalchemy.orm import relationship
# from sqlalchemy.ext.declarative import declarative_base
# Base = declarative_base


# class Role():
#     __tablename__ = 'roles'
#     id = Column(Integer, primary_key=True)
#     movie_id = Column(Integer, ForeignKey('movies.id'))
#     actor_id = Column(Integer, ForeignKey('actors.id'))
#     salary = Column(Integer)
#     character_name = Column(String)
#     movie = relationship('Movie', back_populates='roles')
#     actor = relationship('Actor', back_populates='roles')

#     def actor(self):
#         return self.actor

#     def movie(self):
#         return self.movie
