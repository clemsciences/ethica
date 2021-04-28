"""

"""

from flask_cors import CORS

from ethica_server import create_app
from ethica_server.routes import ethica


app = create_app(ethica)
cors = CORS()
cors.init_app(app)

if __name__ == "__main__":
    app.run(debug=True, port=5010)
