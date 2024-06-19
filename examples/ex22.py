import os
from concurrent.futures import ThreadPoolExecutor

def wc(filename: str) -> dict:
    print(f'got this file for processing - {filename}')
    with open(filename, encoding='utf-8') as file:
        cc = len(file.read())
        file.seek(0)
        lc = len(file.readlines())
        return dict(filename=filename, cc=cc, lc=lc)


def main():
    loc = '.'
    future_tasks = []
    with ThreadPoolExecutor(max_workers=5) as executor:
        with os.scandir(loc) as entries:
            for each_entry in entries:
                if each_entry.is_file():
                    if not each_entry.name.endswith('.py'):
                        continue
                    future_task = executor.submit(wc, each_entry.path)
                    future_tasks.append(future_task)
        
        
        for future_task in future_tasks:
            print(future_task.result())
        
    print('end of main()')



if __name__ == '__main__':
    main()
