#! .venv/bin/python
from myutils import line
import math
from random import randint


def main():
    nums = [19, 38, 49, 29, 20, 84, 22, 81, 28, 11]

    even_nums = []
    for each_num in nums:
        if each_num % 2 == 0:
            even_nums.append(each_num)
    print(f'{even_nums = }')

    odd_nums = [ n for n in nums if n % 2 ]
    print(f'{odd_nums = }')

    squares = [n*n for n in nums]
    print(f'{squares = }')

    square_roots = [math.sqrt(n) for n in nums]
    print(f'{square_roots = }')

    random_nums = [randint(1, 100) for _ in range(10) ]
    print(f'{random_nums = }')

    random_nums = [randint(1, 100) for _ in range(15) ]
    print(f'{random_nums = }')

    random_nums = [randint(1, 100) for _ in range(5) ]
    print(f'{random_nums = }')

if __name__ == '__main__':
    main()

