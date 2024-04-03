import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/v1/matches/live", methods=["GET"])
def live_matches():
    url = "https://api.cricbuzz.com/api/match/live"
    response = requests.get(url)
    data = response.json()
    matches = data["match"]
    live_matches = []
    for match in matches:
        if match["status"] == "In Progress":
            live_matches.append(match)
    return jsonify(live_matches)

if __name__ == "__main__":
    app.run()
