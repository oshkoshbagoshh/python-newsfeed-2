from flask import Blueprint, render_template 
from app.models import Post
from app.db import get_db

bp = Blueprint("home", __name__, url_prefix="/")


# This is the homepage route
@bp.route("/")
def index():
  # get all posts from database
  db = get_db()
  posts = (
    db
      .query(Post)
      .order_by(Post.created_at.desc())
      .all()
  )
  return render_template(
    "homepage.html",
    posts=posts
    )



# login route
@bp.route("/login")
def login():
  return render_template("login.html")


# post id route
@bp.route("/post/<int:id>")
def single(id):
  # get single post from database
  db = get_db()
  post = db.query(Post).filter(Post.id == id).one()
  
  # render single post template
  return render_template(
    "single-post.html",
    post=post
    )
  
  

