from datetime import datetime
from app.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

# Create a comment clase that inherits from Base
class Comment(Base):
    __tablename__= 'comments'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(255), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('posts.id'))
    created_at = Column(DateTime,default=datetime.now)
    upated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    
    user = relationship('User')
    
    