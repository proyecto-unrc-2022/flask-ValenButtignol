from flask import Flask, jsonify, request, Response, make_response
import json

app = Flask(__name__)

USERS = {}

@app.route('/')
def index():
    return 'Index Page' 

@app.route("/users/<username>", methods=['GET'])
def access_users(username):
    if request.method == 'GET':
        user_details = USERS.get(username)
        if user_details:
            return jsonify(user_details)
        else:
            return Response(status=404)


@app.route("/users", methods=['GET', 'POST'])
def all_users():
    if request.method == 'GET':
        if USERS:   
            return jsonify(USERS)
    return Response(status=404)

        

if __name__ == "__main__":
    app.run()
