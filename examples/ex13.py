class Book:
    def __init__(self, **kwargs) -> None:
        self.title = kwargs.get('title')
        self.price = kwargs.get('price', 0.0)

    def __str__(self) -> str:
        return f'Book with title={self.__title} and price=₹{self.__price}'
    
    # getter property called 'title'
    @property
    def title(self):
        return self.__title.upper()
    
    @title.setter
    def title(self, value):
        if (value is not None) and not isinstance(value, str):
            raise TypeError(f'title must be a str, got {type(value)}')
        if (value is not None) and (len(value) < 3 or len(value) > 25):
            raise ValueError(f'title must be between 3 and 25 letters, but is {len(value)} letters')
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


def main():
    b1 = Book(title='Python unleashed')
    b2 = Book(price = 279.0)

    b2.title = 'Let us C'  # setter is called
    b1.price = 299

    print(b1)
    print(b2)
    print(f'{b1.title = }')  # getter is called
    print(f'{b1.price = }')  # getter is called
    print(f'{b2.title = }')  # getter is called
    print(f'{b2.price = }')  # getter is called


if __name__ == '__main__':
    main()
