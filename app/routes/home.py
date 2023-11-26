from flask import Blueprint, render_template 

bp = Blueprint("home", __name__, url_prefix="/")


# This is the homepage route
@bp.route("/")
def index():
  return render_template("homepage.html")

# login route

@bp.route("/login")
def login():
  return render_template("login.html")


# post id route
@bp.route("/post/<int:id>")
def single(id):
  return render_template("single-post.html")

