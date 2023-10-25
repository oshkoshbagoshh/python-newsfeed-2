from flask import Blueprint, render_template

bp = Blueprint('home', __name__, url_prefix='/')

# use the decorator pattern to turn the index() function into a route
@bp.route('/')
def index():
    return render_template('homepage.html')

# use the decorator pattern to turn the login() function into a route
@bp.route('/login')
def login():
    return render_template('login.html')

# URL paramemeter for the post id 
@bp.route('/post/<id>')
def single(id):
    return render_template('single.html')

