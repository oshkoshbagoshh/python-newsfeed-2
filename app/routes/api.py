# @Author: AJ Javadi
# @Email: amirjavadi25@gmail.com
# @Date: 2023-11-28 14:15:51
# @Last Modified by:   undefined
# @Last Modified time: 2023-11-28 14:15:51
# @Description: file:///Users/aj/python-newsfeed-2/app/routes/api.py
# ====================================================================================================
# imports 
from flask import Blueprint, request, jsonify, session
from app.models import User, Post, Comment, Vote
from app.db import get_db
# from app.utils.auth import login_required
import sys
import traceback
from sqlalchemy.orm.exc import NoResultFound

# ====================================================================================================
# Blueprint Configuration
bp = Blueprint('api', __name__, url_prefix='/api')


# signup route
# /api/users
@bp.route('/users', methods=['POST'])
def signup():
    data = request.get_json()
    # print(data)
    db = get_db()
    
    # error handling
    try :
        # attempt to create a new user
        newUser = User(
            username = data['username'],
            email = data['email'],
            password = data['password']
        )

        # save in database
        db.add(newUser)
        # print success
        print('success!')
        # commit to database
        db.commit()
    except:
        # print error
        print(sys.exc_info()[0])
        # insert failed , so send message to front end 
        db.rollback() # rollback to previous state
        return jsonify(message = 'Signup failed'), 500
        
    
    # user's session info 
    # this clears the existing session data and creates a new session for the user
    session.clear()
    session['user_id'] = newUser.id # create a session for user
    session['loggedIn'] = True # set loggedIn to true
    return jsonify(id=newUser.id)




# logout route 
# /api/auth/logout
@bp.route('/users/logout', methods=['POST'])
def logout():
    # remove session variables
    session.clear()
    return '', 204  # HTTP status code 204 means the server successfully processed the request, but is not returning any content.


# login route
# /api/auth/login
# login route
@bp.route('/users/login', methods=['POST'])
def login():
    data = request.get_json()
    db = get_db()

    user = None  # Initialize user variable
    try:
        user = db.query(User).filter(User.email == data['email']).one()
        if user.verify_password(data['password']) == False:
                return jsonify(message = 'Incorrect credentials'), 400
        session.clear()
        session['user_id'] = user.id
        session['loggedIn'] = True
        return jsonify(id = user.id)
    except NoResultFound:
        return jsonify(message='Incorrect credentials'), 400
    except Exception as e:
        traceback.print_exc()
        return jsonify(message='An error occurred'), 500   
    
    

