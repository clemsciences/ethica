
from flask_cors import CORS

from ethica_server import create_prod_app
from ethica_server.routes import ethica

app = create_prod_app(ethica)
cors = CORS()
cors.init_app(app)
