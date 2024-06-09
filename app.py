from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


# Hack 1
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify({"payload": "success"})


# Hack 2
@app.route("/user", methods=["POST"])
def post_users():
    return jsonify({"payload": "success"})


# Hack 3
@app.route("/user", methods=["DELETE"])
def delete_users():
    return jsonify({"payload": "success"})


# Hack 4
@app.route("/user", methods=["PUT"])
def put_users():
    return jsonify({"payload": "success", "error": False})


# Hack 5
@app.route("/api/v1/users", methods=["GET"])
def h5_users():
    return jsonify({"payload": []})


# Hack 6
@app.route("/api/v1/user", methods=["POST"])
def h6_user():
    email = "foo@foo.foo"
    name = "fooziman"
    return jsonify(
        {
            "payload": {
                "email": email,
                "name": name,
            }
        }
    )


# Hack 7
@app.route("/api/v1/user/add", methods=["POST"])
def h7_user_add():
    key = request.form.get("key")
    key = {"email": "foo@foo.foo", "name": "fooziman", "id": "123"}
    return jsonify({"payload": key})


# Hack 8
@app.route("/api/v1/user/create", methods=["POST"])
def h8_user_create():
    payload = {"payload": {"email": "foo@foo.foo", "name": "fooziman", "id": "123"}}
    request.get_json(payload)
    return payload


if __name__ == "__main__":
    app.run(debug=True)
