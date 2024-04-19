from flask import Blueprint, request, jsonify, make_response
import json
from src import db


customers = Blueprint('customers', __name__)

# Get all customers from the DB
@customers.route('/getCustomers', methods=['GET'])
def get_customers():
    cursor = db.get_db().cursor()
    cursor.execute('select first_name, last_name,\
        date_of_birth, customer_id from customers')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get all customers' first names from the DB ordered alphabetically
@customers.route('/getFirst_Name', methods=['GET'])
def get_customers():
    cursor = db.get_db().cursor()
    cursor.execute('select first_name, customer_id from customers ORDER BY first_name DESC')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


# Get all customers' last names from the DB ordered alphabetically
@customers.route('/getLast_Name', methods=['GET'])
def get_customers():
    cursor = db.get_db().cursor()
    cursor.execute('select last_name, customer_id from customers ORDER BY last_name DESC')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


# Get all customers' DOB from the DB from oldest to youngest
@customers.route('/getDate_Of_Birth', methods=['GET'])
def get_customers():
    cursor = db.get_db().cursor()
    cursor.execute('select date_of_birth, customer_id from customers ORDER BY date_of_birth DESC')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response




customer_email = Blueprint('customer_email', __name__)

# Get all customers' email address from the DB
@customer_email.route('/emails', methods=['GET'])
def get_customer_email():
    cursor = db.get_db().cursor()
    cursor.execute('select email_address, customer_id from customer_email ORDER BY email_address DESC')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


customer_phones = Blueprint('customer_phones', __name__)

# Get all customers' phone number from the DB
@customer_phones.route('/phone_numbers', methods=['GET'])
def get_customer_phones():
    cursor = db.get_db().cursor()
    cursor.execute('select phone_num, customer_id from customer_phones ORDER BY phone_num DESC')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


# Add customers
@customers.route('/customers', methods=['POST']) 
def add_customers():
    # Retrieve data from the request
    data = request.json

    # Ensure required fields are present in the request data
    required_fields = ['customer_id', 'first_name', 'last_name', 'date_of_birth']
    if not all(field in data for field in required_fields):
        return jsonify({"Error": "Missing required fields."})

    # Insert the new customer into the database
    cursor = db.get_db().cursor()
    try:
        cursor.execute('''
            INSERT INTO customers ('first_name', 'last_name', 'date_of_birth', 'customer_id')
            VALUES (%s, %s, %s, %s, %s)
    ''', (data['first_name'], data['last_name'], data['date_of_birth'], data['customer_id'])) 
        db.get_db().commit()
    except Exception as e:
        return jsonify({"Error": str(e)})

    return jsonify({"Message": "Customer added successfully."})


# Update customer
@customers.route('/customesr/<int:customer_id>', methods=['PUT'])
def update_customer(customer_id):
    # Retrieve data from the request
    data = request.json

    # Ensure required fields are present in the request data
    required_fields = ['customer_id', 'first_name', 'last_name', 'date_of_birth']
    if not all(field in data for field in required_fields):
        return jsonify({"Error": "Missing required fields."})

    # Update the customer in the database
    cursor = db.get_db().cursor()
    try:
        cursor.execute('''
            UPDATE customers
            SET first_name = %s, last_name = %s, date_of_birth = %s
            WHERE customer_id = %s
        ''', (data['customer_id'], data['first_name'], data['last_name'], data['date_of_birth']))
        db.get_db().commit()
    except Exception as e:
        return jsonify({"Error": str(e)})

    return jsonify({"Message": f"Customer {customer_id} updated successfully."})


# Delete customer
@customers.route('/customers/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    # Delete the customer from the database
    cursor = db.get_db().cursor()
    try:
        cursor.execute('''
            DELETE FROM customers
            WHERE customer_id = %s
        ''', (customer_id,))
        db.get_db().commit()
    except Exception as e:
        return jsonify({"Error": str(e)})

    return jsonify({"Message": f"Customer {customer_id} deleted successfully"})




