def main():
    keys = ('id', 'fname', 'lname', 'city', 'email')
    vals = (1, 'Vinod', 'Kumar', 'Bengaluru', 'vinod@vinod.co')
    
    p1 = dict(zip(keys, vals))
    print(p1)

    p2 = dict.fromkeys(keys)
    print(p2)


if __name__ == '__main__':
    main()

