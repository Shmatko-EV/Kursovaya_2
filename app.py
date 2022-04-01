from flask import Flask

from routes import mane_blueprint
from api.routes_api import api_bp

def create_app():

    app = Flask(__name__)

    app.register_blueprint(mane_blueprint)

    app.register_blueprint(api_bp, url_prefix='/api')

    return app


app = create_app()

if __name__ == "__main__":
    app.run()
