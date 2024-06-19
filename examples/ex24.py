# server app
# my ip = 192.168.158.156

from socket import socket, AF_INET, SOCK_STREAM
from sqlite3 import connect, DatabaseError
import json
import threading

db_filename = 'customersdb.sqlite'


def add_customer(name, city, email):
    try:
        data = (name, email, city)
        sql = 'insert into customers(name, email, city) values (?, ?, ?)'
        with connect(db_filename) as conn:
            cur = conn.cursor()
            cur.execute(sql, data)
            conn.commit()
            fields = ('name', 'email', 'city')
            c = dict(zip(fields, data))
            c['id'] = cur.lastrowid
            return c
    except Exception as e:
        err = {}
        err['message'] = f'{e}'
        err


def get_customer(customer_id):
    try:
        with connect(db_filename) as conn:
            cur = conn.cursor()
            cur.execute('select * from customers where id = ?', (customer_id, ))
            data = cur.fetchone()
            if data is None:
                err = dict()
                err['message'] = f'No data found for id {customer_id}'
                return err
            keys = ('id', 'name', 'email', 'city')
            customer = dict(zip(keys, data))
            return customer
    except DatabaseError as e:
        err = dict()
        err['message'] = f'{e}'
        return err

def main():
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_address = ('192.168.158.156', 2345)
    server_socket.bind(server_address)
    server_socket.listen()
    print(f'server listening at {server_address}')
    while True:
        print('waiting for clients to connect')
        cl_sock, cl_addr = server_socket.accept()
        threading.Thread(target=handle_client, args=(cl_sock, cl_addr)).start()

def handle_client(cl_sock, cl_addr):
    print(f'Got a client socket from {cl_addr}')
    req = cl_sock.recv(1024).decode('utf-8')
    req = json.loads(req)
    data = {}
    method_name = req['method_name']
    args = req['method_args']
    if method_name == 'get_customer':
        data = get_customer(*args)
    elif method_name == 'add_customer':
        data = add_customer(*args)

    cl_sock.send(json.dumps(data).encode('utf-8'))

if __name__ == '__main__':
    main()
