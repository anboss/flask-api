from flask import Flask, jsonify

#initiate the flask api 
app = Flask(__name__)          

#define a route
@app.route('/api/greet', methods=['GET']) 

#define function greet
def greet(): 
    return jsonify({'message': 'Hello, World!'})

#boilerplate code to run the flask app
if __name__ == '__main__':
    app.run(debug=True) 
    