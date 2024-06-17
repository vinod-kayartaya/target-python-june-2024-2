filename = '/Users/vinod/Desktop/trainings/target-python-june-2024-2/examples/ex09.py'


def file_read_method1():
    global filename
    f = None
    try:
        f = open(filename)
        content = f.read()
        print(content)
    except OSError as err:
        print(f'Something went wrong! - {err}')
    finally:
        if f is not None: 
            f.close()


def file_read_method2():
    global filename
    # context manager closes the open resource before exiting
    with open(filename) as f:
        # while exiting this block, f.close() is called automatically
        for each_line in f:
            print(each_line, end='')


def file_read_method3():
    global filename
    # context manager closes the open resource before exiting
    with open(filename) as f:
        while True:
            each_line = f.readline()
            if each_line == '':
                break
            print(each_line, end='')


def main():
    # file_read_method1()
    file_read_method2()


if __name__ == '__main__':
    main()

