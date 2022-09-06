import re
from flask import Flask, jsonify, request, Response, make_response
import json

app = Flask(__name__)

USERS = {'ljames': {'name': 'Lebron James'}}

@app.route('/')
def index():
    return 'Index Page' 

@app.route("/users/<username>", methods=['GET', 'PUT', 'DELETE'])
def access_or_update_user(username):
    if request.method == 'GET':
        user_details = USERS.get(username)
        if user_details:
            return jsonify(user_details), 200
        else:
            return Response(status=404)

    elif request.method == 'PUT':
        user_details = json.loads(request.data)
        uname = list(user_details.keys())[0] 
        name = list(user_details.values())[0]
        if user_details and uname == username:
            USERS.update({username : {'name': name}})
            return Response(status=200)

    else:
        deleted_user = USERS.pop(username)
        if deleted_user:
            return jsonify(deleted_user), 200


@app.route("/users/", methods=['GET', 'POST'])
def all_users_or_add_new_user():
    if request.method == 'GET':
        return jsonify(USERS)
    else:
        user_details = json.loads(request.data)
        username = list(user_details.keys())[0]
        if username not in USERS and username:
            USERS.update(user_details)   
            return Response(status=201, headers={"location": f"/users/{username}"}) 
        else:
            return Response(status=409)



if __name__ == "__main__":
    app.run()
