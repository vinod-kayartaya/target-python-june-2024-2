from socket import socket, AF_INET, SOCK_STREAM
import json


def main1():
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_address = ('192.168.158.156', 2345)
    server_socket.connect(server_address)

    name = input('Enter name: ')
    city = input('Enter city: ')
    email = input('Enter email: ')

    req = {}
    req['method_name'] = 'add_customer'
    req['method_args'] = (name, city, email)

    server_socket.send(json.dumps(req).encode('utf-8'))
    resp = server_socket.recv(1024)
    resp = json.loads(resp.decode('utf-8'))

    print(resp)

def main():
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_address = ('192.168.158.156', 2345)
    server_socket.connect(server_address)

    customer_id = int(input('Enter customer id: '))

    req = {}
    req['method_name'] = 'get_customer'
    req['method_args'] = (customer_id, )

    server_socket.send(json.dumps(req).encode('utf-8'))
    resp = server_socket.recv(1024)
    resp = json.loads(resp.decode('utf-8'))

    print(resp)

if __name__ == '__main__':
    main()
