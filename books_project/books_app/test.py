# from sqlalchemy import Table, Column, Integer, ForeignKey, String, create_engine, desc, Table
# from sqlalchemy.orm import relationship, sessionmaker
# from sqlalchemy.ext.declarative import declarative_base

# from marshmallow import Schema, fields

# from rest_framework import mixins, viewsets

# engine =  create_engine()

# session = sessionmaker()(bind=engine)

# Base = declarative_base()
# viewsets.ViewSet
# # one to one -----
# class User(Base):
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(100))
#     profile = relationship("Profile", backref="user", uselist=False, cascade="all, delete, save-update")

# class Profile(Base):
#     id = Column(Integer, primary_key=True)
#     fname = Column(String(100), nullable=False, unique=True)
#     lname = Column(String(30), nullable=False, unique=False)
#     user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE", onupdate="CASCADE"))

# #one to many
# class Person(Base):
#     __tablename__ = 'persons'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(30), nullable=True, unique=True)
#     posts = relationship("Post", back_populates="person", cascade="all, delete, save-update")


# class Post(Base):
#     __tablename__ = 'posts'
#     id = Column(Integer, primary_key=True)
#     desc = Column(String(200), nullable=False)
#     person_id = Column(ForeignKey("persons.id", ondelete="CASCADE", onupdate='CASCADE'))
#     person = relationship("Person",back_populates="posts")


# # many to many 

# man_group = Table(

#     "man_group",
#     Base.metadata,
#     Column('id', Integer, primary_key=True),
#     Column('man_id', Integer, ForeignKey("man.id")),
#     Column('group_id', Integer, ForeignKey('group.id'))
# )
# class Man(Base):
#     __tablename__ = 'man'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(100), nullable=False)
#     groups = relationship("Group", secondary=man_group, back_populates = "men")
    

# class Group(Base):
#     __tablename__ = 'group'

#     id = Column(Integer, primary_key=True)
#     title = Column(String(100), nullable=False)
#     men = relationship("Man", secondary=man_group, back_populates = 'groups')

# user_one = User(name = "ahmad")
# user_two = User(name = "israa")
# session.add(user_one)
# session.add_all([user_one, user_two])
# session.commit()

# user = session.query(User).filter(User.id == 1).first()
# user.name = "updated"
# session.commit()



# delete_user = session.query(User).filter(User.id == 2)
# session.delete(delete_user)
# session.commit()


# users = session.query(User).all()
# for user in users:
#     print(user.name)

# users_in = session.query(User).filter(User.id.in_([1,2,3])).all()

# users_more = session.query(User).filter(User.id > 3).all()

# last_user = session.query(User).order_by(User.id.asc()).first()

# last_user = session.query(User).order_by(desc(User.id)).all()

# like_user = session.query(User).filter(User.name.like('a%')).all()

# filter_and_order = session.query(User).filter(User.id.in_([1,2,3])).order_by(User.id.desc).all()




# user1 = session.query(User).filter(User.id == 1).first()
# user1.name = "updated"
# session.commit()

# profile1 = Profile(fname = "israa", lname = "osta", user = user1)
# session.add(profile1)

# deleted_user = session.query(User).filter(User.id == 2).first()
# session.delete(delete_user)