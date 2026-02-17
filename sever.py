from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

gps_data = {
    "device1": {"lat": 20.0, "lon": 85.0}
}

@app.route("/")
def home():
    return "GPS Server Running"

@app.route("/map")
def show_map():
    return render_template("map.html")

@app.route("/update", methods=["POST"])
def update():
    data = request.json
    device = data.get("device")

    gps_data[device] = {
        "lat": data.get("lat"),
        "lon": data.get("lon")
    }

    return jsonify({"status": "ok"})

@app.route("/get")
def get_data():
    return jsonify(gps_data)

if __name__ == "__main__":
    app.run()

