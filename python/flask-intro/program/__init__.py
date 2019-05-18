from flask import Flask


app = Flask(__name__)

# This has to happen after the Flask app is created
from program import routes
