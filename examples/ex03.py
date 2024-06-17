from myutils import remove_duplicates, line

if __name__ == '__main__':
    line()
    data = [1, 2, 3, 4, 2, 3, 4, 2, 3, 4, 5, 6]
    new_data = remove_duplicates(data, 35)
    print(f'{data = }')
    print(f'{new_data = }')
    line()
