from flask import Blueprint, request, jsonify, make_response
import json
from src import db


carCompany = Blueprint('carCompany', __name__)

# Get all the products from the database
@carCompany.route('/carCompany', methods=['GET'])
def get_carCompany():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    cursor.execute('SELECT rating, company_name FROM rent_car_company')

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


# get the company name from the database
@carCompany.route('/Company')
def get_carCompany():
    cursor = db.get_db().cursor()
    query = '''
        SELECT rating, company_name
        FROM rent_car_company
        ORDER BY company_name DESC
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


# get the ratings of the companies from the database
@carCompany.route('/Rating')
def get_carCompany():
    cursor = db.get_db().cursor()
    query = '''
        SELECT rating, company_name
        FROM rent_car_company
        ORDER BY rating DESC
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


# get the company names from the database ordered alphabetically
@carCompany.route('/Company')
def get_carCompany():
    cursor = db.get_db().cursor()
    query = '''
        SELECT rating, company_name
        FROM rent_car_company
        ORDER BY company_name DESC
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






cars = Blueprint('car', __name__)

# Get all the products from the database
@cars.route('/car', methods=['GET'])
def get_car():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    cursor.execute('SELECT model, available, capacity, price, company_name, licence_plate FROM cars')

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


# get the cheapest cars from the database
@cars.route('/mostExpensive')
def get_car():
    cursor = db.get_db().cursor()
    query = '''
        SELECT available, model, LicencePlate, price, capacity
        FROM cars
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


# get the model of the cars from the database in ordered alphabetically
@cars.route('/Model')
def get_car():
    cursor = db.get_db().cursor()
    query = '''
        SELECT available, model, LicencePlate, price, capacity
        FROM cars
        ORDER BY model DESC
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


# get the capacity of each car from the database ordering from lowest to highest
@cars.route('/Capacity')
def get_car():
    cursor = db.get_db().cursor()
    query = '''
        SELECT available, model, LicencePlate, price, capacity
        FROM cars
        ORDER BY capacity DESC
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

# get only available cars from the database
@cars.route('/Availability')
def get_car():
    cursor = db.get_db().cursor()
    query = '''
        SELECT available, model, LicencePlate, price, capacity
        FROM cars
        WHERE available = true
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


# Add cars
@cars.route('/cars', methods=['POST']) 
def add_cars():
    # Retrieve data from the request
    data = request.json

    # Ensure required fields are present in the request data
    required_fields = ['model', 'available', 'capacity', 'price', 'company_name', 'license_plate']
    if not all(field in data for field in required_fields):
        return jsonify({"Error": "Missing required fields."})

    # Insert the new car into the database
    cursor = db.get_db().cursor()
    try:
        cursor.execute('''
            INSERT INTO cars ('model', 'available', 'capacity', 'price', 'company_name', 'license_plate')
            VALUES (%s, %s, %s, %s, %s)
    ''', (data['model'], data['available'], data['capacity'], data['price'], data['company_name'], data['license_plate'])) 
        db.get_db().commit()
    except Exception as e:
        return jsonify({"Error": str(e)})

    return jsonify({"Message": "Car added successfully."})

# Update car
@cars.route('/cars/<int:license_plate>', methods=['PUT'])
def update_car(license_plate):
    # Retrieve data from the request
    data = request.json

    # Ensure required fields are present in the request data
    required_fields = ['company_name', 'license_plate', 'model', 'available', 'capacity', 'price']
    if not all(field in data for field in required_fields):
        return jsonify({"Error": "Missing required fields."})

    # Update the car in the database
    cursor = db.get_db().cursor()
    try:
        cursor.execute('''
            UPDATE cars
            SET model = %s, available = %s, capacity = %s, price = %s
            WHERE license_plate = %s, company_name = %s
        ''', (data['company_name'], data['license_plate'], data['model'], data['available'], data['capacity'], data['price']))
        db.get_db().commit()
    except Exception as e:
        return jsonify({"Error": str(e)})

    return jsonify({"Message": f"Car {license_plate} updated successfully."})


# Delete car
@cars.route('/cars/<int:license_plate>', methods=['DELETE'])
def delete_car(license_plate):
    # Delete the car from the database
    cursor = db.get_db().cursor()
    try:
        cursor.execute('''
            DELETE FROM cars
            WHERE license_plate = %s
        ''', (license_plate,))
        db.get_db().commit()
    except Exception as e:
        return jsonify({"Error": str(e)})

    return jsonify({"Message": f"Car {license_plate} deleted successfully"})



