from flask import Flask, Blueprint


__author__ = ["Clément Besnier <clem@clementbesnier.fr>", ]


ethica = Blueprint("ethica", __name__, )


def create_app():
    app = Flask(__name__)
    # app.config.from_object(Config)
    app.secret_key = "ethica"

    app.register_blueprint(ethica, url_prefix="/ethica")

    return app
