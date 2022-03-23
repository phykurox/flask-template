from flask_cors import CORS
import flask, os, logging
from app import app, api, app_blueprint, VERSION, \
    PORT, APP_NAME, FLASK_DEBUG, ENV_NAME
from app.movies.film_api import film_ns


# Add flaskx namespaces here
api.add_namespace(film_ns)
app.register_blueprint(app_blueprint, url_prefix=f"/api/{VERSION}")

CORS(app)  # enable CORS on Flask app


if __name__ == "__main__":  # pragma: no cover
    app.run(host='0.0.0.0', port=PORT, debug=FLASK_DEBUG)
