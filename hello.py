 # An instance of the Flask class will be our WSGI application.
from flask import Flask
# We create an instance of the Flask class
# Since we are creating a single module, we use __name__
	# this is the name of the application's module or package
app = Flask(__name__)

# Tells Flask what URL should trigger our function
@app.route('/')

# Function is given a name which is also used to generate URLs for this function
def hello_world():
    return 'Hello, World!'