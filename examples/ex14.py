class Person(object):
    def __init__(self, **kwargs):
        print('Person.__init__() called')
        self.name = kwargs.get('name')
        self.email = kwargs.get('email')

    def print(self):
        print(f'Person::{id(self.print) = }')
        print(f'Name     : {self.name}')
        print(f'Email    : {self.email}')

class Employee(Person):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Person.__init__(self, **kwargs)
        self.id = kwargs.get('id')
        self.salary = kwargs.get('salary')

    def info(self):
        print(self.__dict__)

    def print(self):
        print(f'ID       : {self.id}')
        super().print()
        # Person.print(self)
        print(f'Salary   : {self.salary}')
        print(f'Employee::{id(self.print) = }')
        print(f'Person::{id(super().print) = }')

    def base(self):
        return super()

def main():
    e1 = Employee(name='John', email='john@xmpl.com', id=1234)
    print(isinstance(e1, Employee))
    print(isinstance(e1, Person))
    print(isinstance(e1, object))
    print(isinstance(e1, str))
    e1.info()
    e1.salary = 200000
    e1.info()
    e1.print()
    print(f'{id(e1.print) = }')
    e1.base().print()
    Person.print(e1)

if __name__ == '__main__':
    main()


