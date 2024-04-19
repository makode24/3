from flask import Blueprint, request, jsonify, make_response
import json
from src import db


flights = Blueprint('flights', __name__)

# Get all the flights from the database
@flights.route('/flights', methods=['GET'])
def get_flights():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    cursor.execute('SELECT flight_id, class, layover, arrival_time, departure_time, price FROM flights')

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

# Get all the flights from the database ordering by lowest price
@flights.route('/leastExpensive')
def get_flights_lowest_price():
    cursor = db.get_db().cursor()
    query = '''
        SELECT flight_id, class, layover, arrival_time, departure_time, price
        FROM flights
        ORDER BY price DESC
    '''
    cursor.execute(query)
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

# Get the menu for the flight
@flights.route('/getFlightMenu')
def get_flight_menu():
    cursor = db.get_db().cursor()
    query = '''
        SELECT drinks, dessert, main_course, flight_id
        FROM flight_menu 
        JOIN flights ON flight_menu.flight_id = flights.flight_id;
    '''
    cursor.execute(query)
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

# Get the airlines and orders them by rating (from highest to lowest)
@flights.route('/getAirlineRatings')
def get_airline_ratings():
    cursor = db.get_db().cursor()
    query = '''
        SELECT name, rating
        FROM airlines
        WHERE airline_id IN (SELECT DISTINCT airline_id FROM flights) 
        ORDER BY rating DESC;
    '''
    cursor.execute(query)
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

# Get the airlines and orders them by number of accidents (from lowest to highest)
@flights.route('/getAirlineAccidents')
def get_airline_accidents():
    cursor = db.get_db().cursor()
    query = '''
        SELECT name, rating
        FROM airlines
        WHERE airline_id IN (SELECT DISTINCT airline_id FROM flights) 
        ORDER BY rating DESC;
    '''
    cursor.execute(query)
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

# Get the airports that offer any type of lounge
@flights.route('/getAirportLounges')
def get_airport_lounges():
    cursor = db.get_db().cursor()
    query = '''
        SELECT DISTINCT a.code, a.city, al.lounge_type
        FROM airports a
        JOIN airport_lounges al ON a.code = al.code;
    '''
    cursor.execute(query)
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