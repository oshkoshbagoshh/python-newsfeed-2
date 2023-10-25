from app.db import Base
from sqlalchemy import Column, Integer, String 
from sqlalchemy.orm import validates
import bcrypt

#  create a salt 
salt = bcrypt.gensalt()


# Create a User class that inherits from Base
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), primary_key=True)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    
    
    # Add a validator to the email field
    @validates('email')
    def validate_email(self, key, email):
        # Make sure email address contains @ character
        assert '@' in email

        return email
    
    # add a validator to the password field
    @validates('password')
    def validate_password(self, key, password):
        assert len(password) >= 4
        
        # encrpyt the password
        return bcrypt.hashpw(password.encode('utf-8'), salt)
        
        return password