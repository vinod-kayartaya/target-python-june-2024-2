#! .venv/bin/python
import sys
from myutils import to_float

def main():
    args = sys.argv[1:]
    print(f'{args = }')
    args = [to_float(arg) for arg in args]
    print(f'{args = }')
    print(f'{sum(args) = }')



if __name__ == '__main__':
    main()

