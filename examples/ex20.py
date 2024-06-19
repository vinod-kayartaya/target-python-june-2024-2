from threading import current_thread, Thread
import time


def play_bg_music():
    while True:
        print('playing music')
        time.sleep(0.001)


def print_table(n, upto=10):
    for i in range(1, upto+1):
        print(f'{current_thread().name} {n} X {i} = {n*i}')
        time.sleep(0.01)


def main():
    print(f'{current_thread().name} start of main()')
    t = Thread(target=print_table, name='print-table', args=(23, 20))
    t.start()
    Thread(target=print_table, args=(76, )).start()
    Thread(target=play_bg_music, daemon=True).start()
    t.join()
    print(f'{current_thread().name} end of main()')


if __name__ == '__main__':
    main()
