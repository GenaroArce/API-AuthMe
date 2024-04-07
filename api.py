from flask import Flask, jsonify, request
import pymongo
import bcrypt

app = Flask(__name__)

client = pymongo.MongoClient("MONGO_DB_URL")
db = client["MONGO_DB_NAME"]
collection = db["MONGO_DB_COLLECTION"]

@app.route('/users', methods=["POST"])
def register():
    data = request.get_json()

    email = data.get("email")
    username = data.get("username")
    password = data.get("password")
    password_security = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    user = {
        "email": email,
        "username": username,
        "password": password_security
    }

    result = collection.insert_one(user)
    
    return jsonify({"message": "User registered successfully ✔", "user_id": str(result.inserted_id)}), 201

@app.route('/users', methods=["GET"])
def login():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    check = collection.find_one({"username": username})
    
    if check:
        password_db = check.get("password")
        if bcrypt.checkpw(password.encode('utf-8'), password_db):
            return jsonify({"message": "Welcome to system!"}), 200
        else:
            return jsonify({"message": "Invalid password"}), 401
    else:
        return jsonify({"message": "Username not found"}), 404

if __name__ == '__main__':
    app.run(host="127.0.0.1", port="5050", debug=False)