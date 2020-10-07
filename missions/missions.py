from flask import Flask, jsonify, request, json
import requests, os

app = Flask(__name__)
Teams_api = os.environ.get("Teams_api")

missions = [
    {
        "id":1,
        "Task": "Storage Vmotion",
        "members-ids": [2]
    },

    {
         "id":2,
        "Task": "Deploy new cluster",
        "members-ids": []
    },

    {
        "id": 3,
        "Task": "Create new WFA Workflows",
        "members-ids": []
    }
]

@app.route('/api/missions', methods = ['GET'])
def get_missions():
    return jsonify(missions)

@app.route('/api/missions', methods = ['POST'])
def add_order ():
    mission = request.json
    missions.append(mission)
    ids = mission["members-ids"]
    for member_id in ids:
        body = {
            "mission": request.json["id"]
        }

        req = requests.put(url="""http://{teams_api}/api/teams/{member_id}""", data=json.dumps(body), headers={'Content-type': 'application/json'}) 
        if req.status_code == 404:
            return jsonify({"error": """worker not fount {teams_api}"""})
    response = {
        "msg": "success",
        "mission":missions
    }
    return jsonify(response)

@app.route('/api/missions/<int:id>', methods=['DELETE'])
def del_finished_missions (id):
    finished_mission = {}
    for mission in missions:
        if mission["id"] == id:
            finished_mission = mission
            missions.remove(mission)
    if finished_mission == {}:
        return jsonify({"error" : "not found id" }), 404
    response = {
        "deleted":id,
        "missions": missions
    }
    return jsonify(response)

@app.route('/api/missions/<int:id>', methods = ['GET'])
def get_mission(id):
    get_mission = {}
    for mission in missions:
        if mission["id"] == id:
            get_mission = mission
    if get_mission == {}:
        return jsonify({"error" : "not found id" }), 404
    response = {

        "mission": get_mission
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, port=4000, host="0.0.0.0")

