"""

"""


from ethica_server import create_app
from ethica_server.routes import ethica


app = create_app(ethica)

if __name__ == "__main__":
    app.run(debug=True, port=5010)
