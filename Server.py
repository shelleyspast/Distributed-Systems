from flask import Flask, request, jsonify

app = Flask(__name__)

available_rooms = {
    "hotel1": {
        "room_type": "single",
        "price": 100,
        "available": 5
    },
    "hotel2": {
        "room_type": "double",
        "price": 150,
        "available": 10
    }
}

@app.route('/search', methods=['GET'])
def search_rooms():
    location = request.args.get('location')
    dates = request.args.get('dates')
    guests = request.args.get('guests')
    available_rooms_data = []
    for hotel, room_info in available_rooms.items():
        available_rooms_data.append({
            "hotel": hotel,
            "room_type": room_info["room_type"],
            "price": room_info["price"],
            "available": room_info["available"]
        })

    return jsonify({"available_rooms": available_rooms_data})

@app.route('/book', methods=['POST'])
def book_room():
    data = request.json
    hotel = data.get('hotel')
    room_type = data.get('room_type')
    return jsonify({"message": "Booking confirmed!"})

@app.route('/review', methods=['POST'])
def submit_review():
    data = request.json
    return jsonify({"message": "Review submitted successfully!"})

if __name__ == '__main__':
    app.run(debug=True)