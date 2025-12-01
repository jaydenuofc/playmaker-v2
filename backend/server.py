import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
# Allow your frontend (different URL) to call this API
CORS(app, resources={r"/api/*": {"origins": "*"}})

SLEEPER_PLAYERS_URL = "https://api.sleeper.app/v1/players/nfl"

def map_injury_to_color(status: str | None) -> str:
    """
    Convert Sleeper injury_status to traffic-light colors.
    Examples from Sleeper: 'Out', 'Questionable', 'Doubtful', 'IR', 'Healthy', etc.
    """
    if not status or status.lower() in ["healthy", ""]:
        return "green"

    status = status.lower()

    if status in ["questionable", "probable"]:
        return "yellow"

    # Everything else (out, ir, suspended, pup, doubtful, etc.) is red
    return "red"


@app.route("/")
def home():
    return "Sleeper NFL Injury API Running"


@app.route("/api/player-status", methods=["GET"])
def player_status():
    """
    Example:
    GET /api/player-status?names=Jalen%20Hurts,Puka%20Nacua

    Returns JSON like:
    [
      {
        "name": "Jalen Hurts",
        "team": "PHI",
        "position": "QB",
        "injury_status": "Questionable",
        "color": "yellow"
      },
      ...
    ]
    """
    names_param = request.args.get("names")
    if not names_param:
        return jsonify({"error": "Missing 'names' query parameter"}), 400

    requested_names = [n.strip().lower() for n in names_param.split(",") if n.strip()]

    resp = requests.get(SLEEPER_PLAYERS_URL)
    if not resp.ok:
        return jsonify({"error": "Failed to fetch from Sleeper", "status": resp.status_code}), 502

    data = resp.json()  # big dict: {player_id: {...fields...}}

    results = []

    for player_id, p in data.items():
        full_name = p.get("full_name", "")
        if not full_name:
            continue

        full_name_lower = full_name.lower()

        if any(target in full_name_lower for target in requested_names):
            injury = p.get("injury_status")  # e.g. "Questionable", "Out", "IR", "Healthy"
            color = map_injury_to_color(injury)

            results.append({
                "name": full_name,
                "team": p.get("team", ""),
                "position": p.get("position", ""),
                "injury_status": injury,
                "color": color,
            })

    return jsonify(results)


if __name__ == "__main__":
    # Local dev
    app.run(host="0.0.0.0", port=5000, debug=True)
