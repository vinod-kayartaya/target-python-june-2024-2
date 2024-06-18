import requests
from myutils import line
import csv


def download_picture(url):
    filename = url.split('/')[-1]
    resp = requests.get(url)
    if resp.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(resp.content)
            print(f'saved {filename}')


def flatten(row):
    rating = row['rating']
    del row['rating']
    row['rating'] = rating['rate']
    row['count'] = rating['count']
    return row


def main():
    line()
    url = 'https://fakestoreapi.com/products'
    resp = requests.get(url)
    
    if resp.status_code == 200:
        filename = 'products.csv'
        data = resp.json()
        data = [flatten(row) for row in data]
        with open(filename, 'wt') as file:
            keys = data[0].keys()
            print(keys)
            writer = csv.DictWriter(file, keys)
            writer.writeheader()
            writer.writerows(data)
            print(f'{filename} created')

        for each_prod in data:
            download_picture(each_prod['image'])

    line()


if __name__ == '__main__':
    main()
