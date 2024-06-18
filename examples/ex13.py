class Book:
    def __init__(self, **kwargs) -> None:
        self.title = kwargs.get('title')
        self.price = kwargs.get('price', 0.0)

    def __str__(self):
        return f'Book with title={self.__title} and price=₹{self.__price}'
    
    def __setattr__(self, name, value):
        # print(f'Book.__setattr__() called with name {name}')
        if name not in ('_Book__title', '_Book__price', 'title', 'price'):
            raise AttributeError(f'{name} is not allowed as an attribbute')
        
        super().__setattr__(name, value)
    
    # getter property called 'title'
    @property
    def title(self):
        return self.__title.upper()
    
    @title.setter
    def title(self, value):
        if (value is not None) and not isinstance(value, str):
            raise TypeError(f'title must be a str, got {type(value)}')
        if (value is not None) and (len(value) < 3 or len(value) > 50):
            raise ValueError(f'title must be between 3 and 50 letters, but is {len(value)} letters')
        self.__title = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value is None:
            self.__price = None
            return
        
        if type(value) not in (int, float):
            raise TypeError('price must be a number')
        if value < 0:
            raise ValueError('price must be >= 0')
        
        self.__price = value

    def print(self):
        print(f'Title = {self.__title}')
        print(f'Price = ₹{self.__price}')
        print()

    def __iadd__(self, value):
        if value is None:
            return self
        
        if type(value) is str:
            self.title += value
        elif type(value) in (int, float):
            self.price += value
        else:
            raise TypeError('+= works only with text or numbers for Book object')
        
        return self


def main():
    b1 = Book(title='Python unleashed')
    b2 = Book(price = 279.0)

    b2.title = 'Let us C'  # setter is called
    b1.price = 299

    # b1.author = 'John Doe'  # b1.__setattr__('author', 'John Doe')

    print(b1)
    print(b2)
    print(f'{b1.title = }')  # getter is called
    print(f'{b1.price = }')  # getter is called
    print(f'{b2.title = }')  # getter is called
    print(f'{b2.price = }')  # getter is called

    b1.print()
    Book.print(b1)

    b1 += ' (2nd edition)'
    b1 += 250

    b1.print()


if __name__ == '__main__':
    main()

"""

+       __add__
-       __sub__
*       __mul__
/       __div__
%       __mod__

+=       __iadd__
-=       __isub__
*=       __imul__
/=       __idiv__
%=       __imod__

<       __lt__
<=      __le__
>       __gt__
>=      __ge__
==      __eq__
!=      __ne__

"""