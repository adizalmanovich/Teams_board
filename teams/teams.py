from flask import Flask, jsonify, request, json
import requests

app = Flask(__name__)

Teams = [
    {
        'firstname': 'Michal',
        'lastname': 'Zborovsky',
        "id": 1,
        "mission": []
    },

    {
        'firstname': 'Ben',
        'lastname': 'Goldenberg',
        "id": 2,
        "mission": []

    },

    {
        'firstname': 'Avigail',
        'lastname': 'Spektor',
        "id": 3,
        "mission": [1,2]
    },

    {
        'firstname': 'Gal',
        'lastname': 'Shmilovich',
        "id": 4,
        "mission": []

    },

    {
        'firstname': 'Adi',
        'lastname': 'Zalmanovich',
        "id": 5,
        "mission": []

    }
]


# get all teams
@app.route('/api/teams', methods=['GET'])
def get_teams():
    return jsonify(Teams)


@app.route('/api/teams', methods=['POST'])
def add_member():
    a = request.json
    Teams.insert(len(Teams), a)
    print(jsonify(Teams))
    return jsonify(Teams)


@app.route('/api/teams/<id_name>', methods=['GET'])
def id_finder(id_name):
    for member in Teams:
        if member["id"] == int(id_name):
            return jsonify(member)


@app.route('/api/teams/<int:id>', methods=['PUT'])
def id_change(id):
    new_member = {}
    for i, member in enumerate(Teams):
        if member["id"] == id:
            member["mission"].append(request.json["mission"])
            new_member = member
            Teams[i] = member
    if new_member == {}:
         return jsonify({"error": "not found id"}), 404
    return jsonify(Teams)


@app.route('/api/teams/<int:id>', methods=['DELETE'])
def id_delete(id):
    for member in Teams:
        if member["id"] == id:
            Teams.remove(member)
    return jsonify(Teams)


@app.route('/api/teams/<int:member_id>/<int:mission_id>', methods=['DELETE'])
def mission_delete(mission_id, member_id):
    for member in Teams:
        if member["id"] == member_id:
            if mission_id in member["mission"]:
                member["mission"].remove(mission_id)
            else:
                return jsonify({"error": "not found id"}), 404

    return jsonify(Teams)

if __name__ == '__main__':
    app.run(debug=True, port=80, host="0.0.0.0")

