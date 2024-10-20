# import os
import logging

# from tracing import setupTracingForFlask, setupTracingForRequests, setupTracing 
from flask import Flask, jsonify

logging.basicConfig(level=logging.DEBUG)


#initiate the flask api 
app = Flask(__name__)
# setupTracing(os.environ["APPNAM"], os.environ["APPSUBLVLNAM"])
# setupTracingForFlask(app)
# setupTracingForRequests()

#define a route
@app.route('/api/greet', methods=['GET']) 

#define function greet
def greet(): 
    return jsonify({'message': 'Hello, World!'})

#boilerplate code to run the flask app
if __name__ == '__main__':
    app.run(port=8000)