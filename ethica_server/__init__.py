from flask import Flask, Blueprint


__author__ = ["Clément Besnier <clem@clementbesnier.fr>", ]


ethica = Blueprint("ethica", __name__, )


def create_app(blueprint):
    app = Flask(__name__)
    app.secret_key = "ethica"

    app.register_blueprint(blueprint)

    return app


def create_prod_app(blueprint):
    app = Flask(__name__)
    app.secret_key = "ethica"

    app.register_blueprint(blueprint)

    return app
