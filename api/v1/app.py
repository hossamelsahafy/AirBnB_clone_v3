from flask import Flask, Blueprint, jsonify
from models import storage
from api.v1.views import app_views
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(app_views)

# Allow CORS for all domains on all routes
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, threaded=True)
