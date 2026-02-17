from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

locations = {}

@app.route("/")
def home():
    return "GPS Server Running"

@app.route("/map")
def map_page():
    return render_template("map.html")

@app.route("/update", methods=["POST"])
def update():
    data = request.json

    device = data.get("device")
    lat = data.get("lat")
    lon = data.get("lon")

    if device:
        locations[device] = {"lat": lat, "lon": lon}

    return {"status": "ok"}

@app.route("/location")
def location():
    return jsonify(locations)


if __name__ == "__main__":
    app.run()

