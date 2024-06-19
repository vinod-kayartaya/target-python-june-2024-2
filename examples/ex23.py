from flask import Flask, render_template, Response, request
from sqlite3 import connect, DatabaseError
import json

app = Flask(__name__)
db_filename = 'customersdb.sqlite'


def create_response(data, status=200, mimetype='application/json'):
    return Response(json.dumps(data), status=status, mimetype=mimetype)


@app.get('/api/customers/<int:customer_id>')
def handle_get_one_customer(customer_id):
    try:
        with connect(db_filename) as conn:
            cur = conn.cursor()
            cur.execute('select * from customers where id = ?', (customer_id, ))
            data = cur.fetchone()
            if data is None:
                err = dict()
                err['message'] = f'No data found for id {customer_id}'
                return create_response(err, status=404)
            keys = ('id', 'name', 'email', 'city')
            customer = dict(zip(keys, data))
            return create_response(customer)
    except DatabaseError as e:
        return f'{e}'
    

@app.get('/api/customers')
def handle_get_all_customers():
    try:
        with connect(db_filename) as conn:
            cur = conn.cursor()
            cur.execute('select * from customers')
            data = cur.fetchall()
            keys = ('id', 'name', 'email', 'city')
            customers = [dict(zip(keys, row)) for row in data]
            return create_response(customers)
    except DatabaseError as e:
        return f'{e}'
    

@app.post('/api/customers')
def handle_post():
    try:
        req_body = request.json
        data = (req_body['name'], req_body['email'], req_body['city'])
        sql = 'insert into customers(name, email, city) values (?, ?, ?)'
        with connect(db_filename) as conn:
            cur = conn.cursor()
            cur.execute(sql, data)
            req_body['id'] = cur.lastrowid
            conn.commit()
            return create_response(req_body, status=201)
    except Exception as e:
        err = {}
        err['message'] = f'{e}'
        return create_response(err, status=400)



@app.route('/')
def index():
    name = 'Vinod Kumar Kayartaya'
    library = 'Flask'
    return render_template('home.html', context=dict(name=name, library=library))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1234, debug=True)