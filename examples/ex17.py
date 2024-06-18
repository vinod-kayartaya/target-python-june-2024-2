#! .venv/bin/python
from myutils import profile


@profile
def do_something():
    print('started to do something...')
    for _ in range(100_000_000):
        pass
    print('done!!')


def main():
    do_something('vinod', 100)


if __name__ == '__main__':
    main()

