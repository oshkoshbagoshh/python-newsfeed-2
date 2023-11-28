# @Author: AJ Javadi
# @Email: amirjavadi25@gmail.com
# @Date: 2023-11-28 11:22:48
# @Last Modified by:   undefined
# @Last Modified time: 2023-11-28 11:22:48
# @Description: file:///Users/aj/python-newsfeed-2/app/models/Comment.py
# Path: app/models/Comment.py

from datetime import datetime
from app.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship


# Comment model
class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(255), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    post_id = Column(Integer, ForeignKey("posts.id"))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    
    user = relationship('User')
    