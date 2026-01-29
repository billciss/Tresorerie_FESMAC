from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/v1/tokens', methods=['POST'])
def create_token():
    # Logic to create a token
    return jsonify({'message': 'Token created'}), 201

@app.route('/api/v1/tokens/<token_id>', methods=['GET'])
def get_token(token_id):
    # Logic to get a token
    return jsonify({'token_id': token_id, 'status': 'active'})

if __name__ == '__main__':
    app.run(debug=True)