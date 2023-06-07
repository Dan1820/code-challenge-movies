

# class Actor():
#     __tablename__ = 'actors'
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     roles = relationship('Role', back_populates='actor')
#     movies = relationship('Movie', secondary='role', back_populates='actors')

#     def roles(self):
#         return self.roles

#     def movies(self):
#         return self.movies
