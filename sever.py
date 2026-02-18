from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

latest_data = {}

@app.route('/')
def home():
    return render_template("map.html")


@app.route('/update', methods=['POST'])
def update():
    global latest_data
    latest_data = request.json
    print("Received:", latest_data)
    return {"status": "ok"}


@app.route('/location')
def location():
    return jsonify(latest_data)


if __name__ == '__main__':
    app.run()

