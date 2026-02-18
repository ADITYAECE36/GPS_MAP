from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

latest_data = {"lat": 0, "lon": 0}


@app.route('/')
def home():
    return render_template("map.html")


@app.route('/update', methods=['POST'])
def update():
    global latest_data
    data = request.json
    print("Received:", data)

    latest_data["lat"] = data["lat"]
    latest_data["lon"] = data["lon"]

    return {"status": "success"}


@app.route('/location')
def location():
    return jsonify(latest_data)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)
