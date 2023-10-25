from flask import Flask
from app.routes import home # import the home module
from app.routes import home, dashboard # import the dashboard module
from app.db import init_db



def create_app(test_config=None):
    # set up app config
    app = Flask(__name__, static_url_path="/")
    app.url_map.strict_slashes = False
    app.config.from_mapping(
        SECRET_KEY="super_secret_key",
        DATABASE_URL=""
    )

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    # register routes
    app.register_blueprint(home)
    app.register_blueprint(dashboard)
    
    
    
    # initialize the database
    init_db()

    # return the app
    return app


