#from flask import Flask, request, jsonify
from flask import Flask, request, jsonify, render_template

#app = Flask(__name__, template_folder="templates")  # відносний шлях (краще, ніж абсолютний)
app = Flask(__name__, template_folder="../templates")

users = {}

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user_id = data.get('id')
    users[user_id] = data
    return jsonify({"message": "User created", "user": users[user_id]}), 201

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user), 200
    return jsonify({"message": "User not found"}), 404

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"message": "User not found"}), 404
    data = request.get_json()
    users[user_id].update(data)
    return jsonify({"message": "User updated", "user": users[user_id]}), 200

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        return jsonify({"message": "User deleted"}), 200
    return jsonify({"message": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=8000)