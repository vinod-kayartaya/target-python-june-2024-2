import time
import json
import csv


def main():
    filename = input('Enter CSV filename: ')
    with open(filename) as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
        
    # with open(filename) as file:
    #     keys = file.readline().strip().split(',')
    #     data = []
    #     for each_line in file:
    #         vals = each_line.strip().split(',')
    #         data.append(dict(zip(keys, vals)))

    out_filename = f'{filename[:-4]}_{time.time()}.json'
    with open(out_filename, 'w') as file:
        json.dump(data, file)
        print('data saved in JSON format')


if __name__ == '__main__':
    main()

