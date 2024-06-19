# from sqlite3 import connect, DatabaseError
from mysql.connector import connect, DatabaseError
# pip install mysql-connector-python
import csv


db_filename = 'customersdb.sqlite'
db_info = dict(host="localhost",
  user="root",
  password="Welcome#123",
  port = 3306,
  database='targetdb')


def menu() -> int:
    print("""
*** Main Menu ***
0. Exit
1. Create customers table
2. Add new customer data
3. Search customer by id
4. Display all customers
5. Load data from CSV file
""")
    return int(input("Enter your choice: "))

def main():
    while True:
        choice = menu()

        if choice == 0:
            break

        if choice < 0 or choice > 5:
            print('Invalid choice. Please retry.')
            continue

        if choice == 1:
            create_customer_table()
        elif choice == 2:
            add_new_customer()
        elif choice == 3:
            search_customer()
        elif choice == 4:
            display_all_customers()
        elif choice == 5:
            load_from_csv_file()


def create_customer_table():
    global db_filename
    sql = """create table customers (
    id INTEGER primary key auto_increment,
    name varchar(50) not null,
    email varchar(100) unique,
    city varchar(50) default 'Bengaluru'
    )
"""
    try:
        # with connect(db_filename) as conn:  # for sqlite
        with connect(**db_info) as conn:
            cur = conn.cursor()
            cur.execute(sql)
            print('Table created successfully')
    except DatabaseError as e:
        print(e)


def add_new_customer():
    global db_filename
    print("Enter new customer data: ")
    name = input("Name  : ")
    email = input("Email : ")
    city = input("City  : ")
    # sql = "insert into customers (name, city, email) values (?, ?, ?)"  # for sqlite
    sql = "insert into customers (name, city, email) values (%s, %s, %s)"
    try:
        # with connect(db_filename) as conn:  # for sqlite
        with connect(**db_info) as conn:
            cur = conn.cursor()
            cur.execute(sql, (name, city, email))
            conn.commit()
            print(f'Data inserted. ID generated is {cur.lastrowid}.')
    except DatabaseError as e:
        print(e)


def search_customer():
    global db_filename
    try:
        customer_id = int(input('Enter customer id to search: '))
        # sql = 'select name, city, email from customers where id = ?'  # for sqlite
        sql = 'select name, city, email from customers where id = %s'
        # with connect(db_filename) as conn:  # for sqlite
        with connect(**db_info) as conn:
            cur = conn.cursor()
            cur.execute(sql, (customer_id,))
            data = cur.fetchone()
            if data is None:
                print(f'No customer found for id {customer_id}')
            else:
                print(f'Name   : {data[0]}')
                print(f'City   : {data[1]}')
                print(f'Email  : {data[2]}')
    except ValueError as e:
        print('Customer ID must be an integer')
    except DatabaseError as e:
        print(e)


def display_all_customers():
    global db_filename
    try:
        sql = 'select * from customers'
        # with connect(db_filename) as conn:  # for sqlite
        with connect(**db_info) as conn:
            cur = conn.cursor()
            cur.execute(sql)
            data = cur.fetchall()
            if len(data) == 0:
                print('No customer data')
                return
            print('-'*89)
            print(f'|{'ID':4}|{'Name':20}|{'Email':40}|{'City':20}|')
            print('-'*89)
            for cid, name, email, city in data:
                print(f'|{cid:>4}|{name:20}|{email:40}|{city:20}|')
            print('-'*89)
    except ValueError as e:
        print(e)
    except DatabaseError as e:
        print(e)


def load_from_csv_file():
    try:
        csv_file_name = input('Enter CSV filename containing customer data: ')
        with open(csv_file_name, encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            if not set(('name', 'email', 'city')).issubset(set(reader.fieldnames)):
                print('One or more of the required fields missing the file [name, email, city]')
                return
            # with connect(db_filename) as conn:  # for sqlite
            with connect(**db_info) as conn:
                cur = conn.cursor()
                sql = "insert into customers (name, city, email) values (%s, %s, %s)"
                for row in reader:
                    print((row['name'], row['city'], row['email']))
                    cur.execute(sql, (row['name'], row['city'], row['email']))
                conn.commit()
                print('All data from CSV file added to database table.')
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
