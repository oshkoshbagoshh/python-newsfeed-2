# @Author: AJ Javadi
# @Email: amirjavadi25@gmail.com
# @Date: 2023-11-28 11:01:42
# @Last Modified by:   undefined
# @Last Modified time: 2023-11-28 11:01:42
# @Description: file:///Users/aj/python-newsfeed-2/app/models/Post.py
# Path: app/models/Post.py

# imports 
from datetime import datetime
from app.db import Base
from .Vote import Vote
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, select, func
from sqlalchemy.orm import relationship, column_property


# Post model
class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    post_url = Column(String(100), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    # relationship
    user = relationship('User')
    comments = relationship('Comment', cascade='all,delete')
    votes = relationship('Vote', cascade='all,delete')
    
    # votes relationship    
    vote_count = column_property(
        select(func.count(Vote.id)).where(Vote.post_id == id).as_scalar()
    )