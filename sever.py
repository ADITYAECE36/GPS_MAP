from flask import Flask, request, jsonify

app = Flask(__name__)

gps_data = {
    "person1": {"lat": 0, "lon": 0},
    "person2": {"lat": 0, "lon": 0}
}

@app.route('/')
def home():
    return "GPS Server Running"

@app.route('/update', methods=['POST'])
def update():
    data = request.json
    person = data["person"]
    gps_data[person] = {
        "lat": data["lat"],
        "lon": data["lon"]
    }
    return "Updated"

@app.route('/gps', methods=['GET'])
def get_gps():
    return jsonify(gps_data)

if __name__ == "__main__":
    app.run()
