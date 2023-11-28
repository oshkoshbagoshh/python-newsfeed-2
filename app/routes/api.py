# @Author: AJ Javadi
# @Email: amirjavadi25@gmail.com
# @Date: 2023-11-28 14:15:51
# @Last Modified by:   undefined
# @Last Modified time: 2023-11-28 14:15:51
# @Description: file:///Users/aj/python-newsfeed-2/app/routes/api.py
# ====================================================================================================

from flask import Blueprint, request, jsonify
from app.models import User 
from app.db import get_db
import sys 

# Blueprint Configuration
bp = Blueprint('api', __name__, url_prefix='/api')


# signup route
# /api/users
@bp.route('/users', methods=['POST'])
def signup():
    data = request.get_json()
    db = get_db()
    # print(data)
    
    # error handling
    try :
        # create a new user
        newUser = User(
            username = data['username'],
            email = data['email'],
            password = data['password']
        )

        # save in database
        db.add(newUser)
        # commit to database
        db.commit()
    except:
        print(sys.exc_info()[0])
        # insert failed , so send message to front end 
        return jsonify(message = 'Signup failed'), 500
        
    return jsonify(id=newUser.id)




