##import dependenciess
from flask import Flask 
## create a new Flask instance call app
app = Flask(__name__)
## Create a Flask Routes
@app.route('/')
def hello_world():
    return 'Hello world, Flask is fun'

