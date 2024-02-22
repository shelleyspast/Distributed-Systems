import requests

# Search for available rooms
search_params = {
    'location': 'New York',
    'dates': '2024-03-01',
    'guests': 2
}
response = requests.get('http://localhost:5000/search', params=search_params)
print("Available Rooms:")
print(response.json())

# Book a room
booking_data = {
    'hotel': 'hotel1',
    'room_type': 'single',
    'guest_name': 'John Doe',
    'payment_details': {
        'card_number': '1234567812345678',
        'expiry_date': '03/26',
        'cvv': '123'
    }
}
booking_response = requests.post('http://localhost:5000/book', json=booking_data)
print("Booking Response:")
print(booking_response.json())

# Submit a review
review_data = {
    'hotel': 'hotel1',
    'rating': 5,
    'comment': 'Great experience!'
}
review_response = requests.post('http://localhost:5000/review', json=review_data)
print("Review Response:")
print(review_response.json())