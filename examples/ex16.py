from abc import ABC, abstractmethod
import math


class GeometricShape(ABC):

    def __init__(self) -> None:
        super().__init__()
        print('GeometricShape.__init__() called')

    @abstractmethod
    def find_area(self):
        pass

    @property
    @abstractmethod
    def shape_name(self)->str:
        pass


class Circle(GeometricShape):
    def __init__(self, radius=1.0) -> None:
        super().__init__()
        self.radius = radius
        print('Circle.__init__() called')

    def find_area(self):
        return math.pi * self.radius * self.radius
    
    @property
    def shape_name(self):
        return 'Circle'


class Triangle(GeometricShape):
    def __init__(self, base=1.0, height=1.0) -> None:
        super().__init__()
        self.base = base
        self.height = height
        print('Triangle.__init__() called')

    def find_area(self):
        return 0.5 * self.base * self.height
    
    @property
    def shape_name(self):
        return 'Triangle'
    

# polymorphic function
def process_shape(shape: GeometricShape) -> None:
    if not isinstance(shape, GeometricShape):
        raise TypeError('not a GeometricShape object')
    
    print(f'area of the {shape.shape_name} is {shape.find_area()}')


def main():
    c1 = Circle(12.34)
    t1 = Triangle(12.34, 56.78)
    process_shape(c1)
    process_shape(t1)
    # process_shape(1234)
    


if __name__ == '__main__':
    main()

