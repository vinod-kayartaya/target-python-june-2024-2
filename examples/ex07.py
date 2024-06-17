from pprint import pprint


def main():
    p1 = {
        'name': 'vinod',
        'address': {
            'city': 'Bengaluru',
            'pincode': 560078
        },
        'phones': ['9731424784']
    }

    p1['address']['state'] = 'Karnataka'
    p1['phones'].append('9844083934')
    p1['email'] = 'vinod@vinod.co'

    print(f'{p1['email'] = }')
    # print(f'{p1['gender'] = }')
    print(f'{p1.get('country', 'India') = }')

    pprint(p1)

if __name__ == '__main__':
    main()

