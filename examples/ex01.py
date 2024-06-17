"""
This is our first module.

In here we are learning the following:
1. docstring
2. hash-bang notation
3. input output from the user
"""
#! ./.venv/bin/python

print('value of __name__ is', __name__)


def future_function_1():
    ...


def future_function_2():
    pass


def say_hello(name='friend', city='your city'):
    print(f'Hello {name}, how is weather in {city}')


def say_hello(name='friend', city='your city'):
    print(f'Namaskara {name}, how is weather in {city}')


def main():
    say_hello()
    say_hello('Vinod')
    say_hello('Shyam', 'Shivamogga')
    say_hello(city='Bengaluru')

    my_name = 'Vinod'
    my_email = 'vinod@vinod.co'
    my_phone = '9731424784'
    my_age = 50

    print(f'{my_name = }')
    print(f'{my_email = }')
    print(f'{my_phone = }')
    print(f'{my_age = }')

    print(f'{my_name}')
    print(f'{my_email}')
    print(f'{my_phone}')


# the following section is ignored by the interpreter when this module is imported in
# another module; will be executed when you run this module.
if __name__ == '__main__':
    main()
