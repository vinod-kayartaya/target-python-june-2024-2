def subtotal(kind, *nums):
    """
    Calculates one of the following and returns the same based on the value of kind.
    kind == 1 -> sum
    kind == 2 -> count
    kind == 3 -> average
    kind == 4 -> min
    kind == 4 -> min
    kind == 5 -> max
    """

    if type(kind) is not int:
        raise TypeError('only int is allowed for `kind`')
    
    if kind < 1 or kind > 5:
        raise ValueError('`kind` must be between 1 and 5')
    
    if kind == 1:
        return sum(nums)
    if kind == 2:
        return len(nums)
    if kind == 3:
        return sum(nums) / len(nums)
    if kind == 4:
        return min(nums)
    
    return max(nums)


def dir2(obj):
    atrs = []
    for each_atr in dir(obj):
        if not each_atr.startswith('_'):
            atrs.append(each_atr)
    return atrs


def line(char='-', count=80):
    print(char*count)
    

def remove_duplicates(collection, value):
    new_collection = []
    for each_value in collection:
        if each_value != value:
            new_collection.append(each_value)
        elif value not in new_collection:
            new_collection.append(each_value)
    return new_collection


def to_float(s):
    try:
        return float(s)
    except ValueError:
        return 0.0
    