from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/playercount")
def player_count():
    try:
        response = requests.get(
            "https://servers-frontend.fivem.net/api/servers/single/3q74by",
            headers={"User-Agent": "Mozilla/5.0"}
        )
        data = response.json()
        return jsonify({
            "clients": data["Data"]["clients"],
            "max_clients": data["Data"]["sv_maxclients"]
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run()
