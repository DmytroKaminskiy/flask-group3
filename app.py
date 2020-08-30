from flask import Flask, request
import requests

from utils import generate_random_password, exec_query

app = Flask(__name__)


@app.route('/generate-password/')
def generate_password():
    password_len = request.args.get('password-len', '10')

    if not password_len.isdigit():
        return 'Error, password-len should be integer'

    password_len = int(password_len)

    if password_len > 100:
        return 'Password should be less than 100'

    return generate_random_password(password_len)

@app.route('/space/')
def space():
    response = requests.get('http://api.open-notify.org/astros.json')
    number = response.json()['number']
    return f'In space: {number}'

@app.route('/customers/')
def customers():
    country = request.args['country']
    query = f"Select * from customers WHERE Country = '{country}';"
    # Select * from customers WHERE Country = 'Germany';
    return str(exec_query(query))


@app.route('/invoices/')
def invoices():
    query = 'Select * from invoices;'
    return str(exec_query(query))

# http://127.0.0.1:8000/gen-pass/?password-len=10

if __name__ == "__main__":
    '''
    http://127.0.0.1:5000/customers/?country=USA&ordering=Country,-State
Select * from customers WHERE Country = 'Germany' ORDER BY Country, State DESC
Select * from customers WHERE Country = 'Germany' ORDER BY Country ASC, State DESC
    '''
    app.run(port=5000, debug=True)
