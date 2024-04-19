from flask import Blueprint, request, jsonify, make_response
import json
from src import db


hotels = Blueprint('hotels', __name__)

# Get all the hotels from the database
@hotels.route('/hotels', methods=['GET'])
def get_hotels():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    cursor.execute('SELECT name, street, street_num, rating FROM hotels')

    # grab the column headers from the returned data
    column_headers = [x[0] for x in cursor.description]

    # create an empty dictionary object to use in 
    # putting column headers together with data
    json_data = []

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    # the column headers. 
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

# Get available rooms for the hotel
@hotels.route('/hotels/<string:name>/<string:street>/<int:street_num>/rooms/available', methods=['GET'])
def get_hotel_rooms_available():
    cursor = db.get_db().cursor()
    
    # Query the database for available rooms for the specified hotel
    cursor.execute('''
        SELECT room_num, price, type, capacity
        FROM rooms
        WHERE name = %s AND street = %s AND street_num = %s AND availability = True
    ''', (name, street, street_num))

       # grab the column headers from the returned data
    column_headers = [x[0] for x in cursor.description]

    # create an empty dictionary object to use in 
    # putting column headers together with data
    json_data = []

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    # the column headers. 
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

# Get the specific room capacity
@hotels.route('/hotels/<string:name>/<string:street>/<int:street_num>/rooms/<int:room_id>/capacity', methods=['GET'])
def get_hotel_rooms_available():
    cursor = db.get_db().cursor()
    
    # Query the database for available rooms for the specified hotel
    cursor.execute('''
        SELECT capacity
        FROM rooms
        WHERE name = %s AND street = %s AND street_num = %s AND room_id = %s
    ''', (name, street, street_num, room_id))

       # grab the column headers from the returned data
    column_headers = [x[0] for x in cursor.description]

    # create an empty dictionary object to use in 
    # putting column headers together with data
    json_data = []

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    # the column headers. 
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

# Get the near by attractions
@hotels.route('/hotels/<string:name>/<string:street>/<int:street_num>/attractions', methods=['GET'])
def get_hotel_rooms_available():
    cursor = db.get_db().cursor()
    
    # Query the database for available rooms for the specified hotel
    cursor.execute('''
        SELECT attraction_id, type, description, kid_friendly, needs_booking, price
        FROM attractions
        WHERE EXISTS (
            SELECT 1
            FROM attractionHotel ah
            WHERE ah.street_num = %s AND ah.street = %s AND ah.name = %s
            AND attractions.attraction_id = ah.attraction_id
        )
    ''', (street_num, street, name))

       # grab the column headers from the returned data
    column_headers = [x[0] for x in cursor.description]

    # create an empty dictionary object to use in 
    # putting column headers together with data
    json_data = []

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    # the column headers. 
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

# Adds a hotel to the database
@hotels.route('/hotels', methods=['POST'])
def add_hotel():
    # Retrieve data from the request
    data = request.json

    # Ensure required fields are present in the request data
    required_fields = ['name', 'street', 'street_num', 'ranking']
    if not all(field in data for field in required_fields):
        return jsonify({"Error": "Missing required fields."})
    
    # Insert the new flight into the database
    cursor = db.get_db().cursor()
    try:
        cursor.execute('''
            INSERT INTO hotels (name, street, street_num, ranking)
            VALUES (%s, %s, %s, %s, %s)
        ''', (data['name'], data['street'], data['street_num'], data['ranking']))
        db.get_db().commit()
    except Exception as e:
        return jsonify({"Error": str(e)})

    return jsonify({"Message": "Hotel added successfully."})

# Update hotel information
@hotels.route('/hotel/<string:name>/<string:street>/<int:street_num>', methods=['PUT'])
def update_hotel(name, street, street_num):
    # Retrieve data from the request
    data = request.json

    # Ensure required fields are present in the request data
    required_fields = ['NWname', 'NWstreet', 'NWstreet_num', 'NWranking']
    if not all(field in data for field in required_fields):
        return jsonify({"Error": "Missing required fields."})

    # Update the flight in the database
    cursor = db.get_db().cursor()
    try:
        cursor.execute('''
            UPDATE hotels
            SET name = %s, street = %s, street_num = %s, ranking = %s
            WHERE name = %s AND street = %s AND street_num = %s
        ''', (data['NWname'], data['NWstreet'], data['NWstreet_num'], data['NWranking'], name, street, street_num))
        db.get_db().commit()
    except Exception as e:
        return jsonify({"Error": str(e)})

    return jsonify({"Message": "Hotel information updated successfully."})

# Updates the room availability
@hotels.route('/hotels/<string:name>/<string:street>/<int:street_num>/rooms/<int:room_id>/availability', methods=['POST'])
def update_room_availability(name, street, street_num, room_id):
    # Retrieve data from the request
    data = request.json

    # Ensure required fields are present in the request data
    required_fields = ['availability']
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    # Update the room availability in the database
    cursor = db.get_db().cursor()
    try:
        cursor.execute('''
            UPDATE rooms
            SET availability = %s
            WHERE street_num = %s AND street = %s AND name = %s AND room_id = %s
        ''', (data['availability'], street_num, street, name, room_id))

        # Commit the transaction
        db.get_db().commit()
    except Exception as e:
        # Rollback the transaction if an error occurs
        db.get_db().rollback()
        return jsonify({"Error": str(e)})
    
    return jsonify({"Message": "Room information updated successfully." })

# Deletes the hotel from the database
@hotels.route('/hotels/<string:name>/<string:street>/<int:street_num>', methods=['DELETE'])
def delete_hotel(name, street, street_num):
    # Connect to the database
    cursor = db.get_db().cursor()

    try:
        # Delete the hotel from the database
        cursor.execute('''
            DELETE FROM hotels
            WHERE name = %s AND street = %s AND street_num = %s
        ''', (name, street, street_num))

        # Commit the transaction
        db.get_db().commit()
    except Exception as e:
        # Rollback the transaction if an error occurs
        db.get_db().rollback()
        return jsonify({"Error": str(e)}), 500
    
    return jsonify({"Message": "Hotel deleted successfully." })