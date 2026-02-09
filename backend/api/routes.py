from flask import Flask, jsonify, request

app = Flask(__name__)

# API endpoint for beers
@app.route('/api/beers', methods=['GET', 'POST'])
def beers():
    if request.method == 'GET':
        return jsonify({'message': 'List of beers'})
    elif request.method == 'POST':
        data = request.get_json()
        return jsonify({'message': 'Beer added', 'data': data}), 201

# API endpoint for trades
@app.route('/api/trades', methods=['GET', 'POST'])
def trades():
    if request.method == 'GET':
        return jsonify({'message': 'List of trades'})
    elif request.method == 'POST':
        data = request.get_json()
        return jsonify({'message': 'Trade created', 'data': data}), 201

# API endpoint for user management
@app.route('/api/users', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        return jsonify({'message': 'List of users'})
    elif request.method == 'POST':
        data = request.get_json()
        return jsonify({'message': 'User created', 'data': data}), 201

if __name__ == '__main__':
    app.run(debug=True)