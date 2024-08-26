from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/get-user/<user_id>')
def get_user(user_id):
    user_data = {
        'user_id': user_id,
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    }

    extra = request.args.get('extra')
    if extra:
        user_data['extra'] = extra

    return jsonify(user_data), 200

@app.route('/create-user', methods=['POST'])
def create_user():
    data = request.get_json()

    if not data:
        return jsonify({'error': 'No user data provided'}), 400

    user_id = data.get('user_id')
    name = data.get('name')
    email = data.get('email')

    if not user_id or not name or not email:
        return jsonify({'error': 'Invalid user data provided'}), 400

    data['status'] = 'created'
    return jsonify(data), 201


if __name__ == '__main__':
    app.run(debug=True)