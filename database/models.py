from sqlalchemy import Column, Integer, String, BigInteger, Boolean, DateTime, ForeignKey, Float, Date
from sqlalchemy.orm import relationship, declarative_base
from database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    phone_number = Column(String, nullable=False, unique=True)
    password = Column(String)
    reg_date = Column(String)

class UserTask(Base):
    __tablename__ = 'user_posts'
    id = Column(Integer, autoincrement=True, primary_key=True)
    main_text = Column(String, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    reg_date = Column(DateTime)
    user_fk = relationship(User, lazy="subquery")
class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, autoincrement=True, primary_key=True)
    post_id = Column(Integer, ForeignKey("user_posts.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    text = Column(String, nullable=False)
    reg_date = Column(DateTime)
    user_fk = relationship(User, lazy="subquery")
    post_fk = relationship(UserTask, lazy="subquery")