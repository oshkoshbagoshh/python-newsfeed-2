# @Author: AJ Javadi
# @Email: amirjavadi25@gmail.com
# @Date: 2023-11-28 11:41:08
# @Last Modified by:   undefined
# @Last Modified time: 2023-11-28 11:41:08
# @Description: file:///Users/aj/python-newsfeed-2/app/models/Vote.py
# Path: app/models/Vote.py

# imports
from app.db import Base
from sqlalchemy import Column, Integer, ForeignKey

# create a vote class
class Vote(Base):
    __tablename__ = 'votes'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('posts.id'))
    