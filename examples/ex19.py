from sqlite3 import connect, DatabaseError


db_filename = 'customersdb.sqlite'


def menu() -> int:
    print("""
*** Main Menu ***
0. Exit
1. Create customers table
2. Add new customer data
3. Search customer by id
4. Display all customers""")
    return int(input("Enter your choice: "))

def main():
    while True:
        choice = menu()

        if choice == 0:
            break

        if choice < 0 or choice > 4:
            print('Invalid choice. Please retry.')
            continue

        if choice == 1:
            create_customer_table()
        elif choice == 2:
            add_new_customer()
        elif choice == 3:
            search_customer()
        else:
            display_all_customers()


def create_customer_table():
    global db_filename
    sql = """create table customers (
    id INTEGER primary key autoincrement,
    name varchar(50) not null,
    email varchar(100) unique,
    city varchar(50) default 'Bengaluru'
    )
"""
    try:
        with connect(db_filename) as conn:
            cur = conn.cursor()
            cur.execute(sql)
            print('Table created successfully')
    except DatabaseError as e:
        print(e)

if __name__ == '__main__':
    main()
