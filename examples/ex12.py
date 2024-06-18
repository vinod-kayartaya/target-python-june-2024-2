class Person(object):

    def __init__(self, name=None, city='Bengaluru'):
        self.name = name
        self.city = city

    def __str__(self):
        return f'Person with name={self.name} and city={self.city}'


def main():
    p1 = Person('Vinod', 'Bengaluru')
    p2 = Person('John', 'Dallas')
    p3 = Person()

    print(p1)
    print(p2)
    print(p3)

if __name__ == '__main__':
    main()

