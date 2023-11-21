@bp.route("/")
def index():
    # get all posts
    db = get_db()
    posts = db.query(Post).order_by(Post.created_at.desc()).all()

    return render_template(
        "homepage.html", posts=posts, loggedIn=session.get("loggedIn")
    )


@bp.route("/login")
def login():
    # not logged in yet
    if session.get("loggedIn") is None:
        return render_template("login.html")
    return redirect("/dashboard")


@bp.route("/post/<id>")
def single(id):
    # get single post by id
    db = get_db()
    post = db.query(Post).filter(Post.id == id).one()

    # render single post template
    return render_template(
        "single-post.html", post=post, loggedIn=session.get("loggedIn")
    )
