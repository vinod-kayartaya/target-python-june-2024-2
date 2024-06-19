import os
import threading
import time

def get_word_count(filename, file_info):
    with open(filename) as file:
        content = file.read()
        line_count = len(content.split('\n'))
        word_count = len(content.split(' '))
        letter_count = len(content)
        info =  dict(filename=filename, letter_count=letter_count, word_count=word_count, line_count=line_count)
        time.sleep(1)
        file_info.append(info)

def main():
    file_info = []
    threads = []
    files = os.listdir('.')
    for each_file in files:
        if not each_file.endswith('.py'):
            continue
        t = threading.Thread(target=get_word_count, args=(each_file, file_info))
        threads.append(t)
        t.start()

    [t.join() for t in threads]
    print(file_info)
    print(len(file_info))

if __name__ == '__main__':
    main()
