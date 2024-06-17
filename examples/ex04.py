#! .venv/bin/python
from myutils import line


def main():
    nums = [19, 38, 49, 29, 20, 84, 22, 81, 28, 11]
    print(f'{nums = }')
    print(f'{len(nums) = }')
    print(f'{nums[0] = }')
    print(f'{nums[len(nums)-1] = }')
    print(f'{nums[-1] = }')
    print(f'{nums[-len(nums)] = }')

    # slice operations
    print(f'{nums[3:8] = }')
    print(f'{nums[3:] = }')
    print(f'{nums[:8] = }')
    print(f'{nums[3:-1] = }')
    # print(f'{nums[-1:-5]}')
    print(f'{nums[0:5]}')
    print(f'{nums[0:5:2]}')
    print(f'{nums[-1:-5:-1]}')
    print(f'{nums[::-1]}')
    my_name = 'vinod kumar'
    print(f'{my_name[::-1] = }')

if __name__ == '__main__':
    main()

