from doctest import testmod


def memory(n):
    """
    Write a function that takes in a value x and updates
    and prints the result based on input functions.
    >>> f = memory(10)
    >>> f = f(lambda x: x * 2)
    20
    >>> f = f(lambda x: x - 7)
    13
    >>> f = f(lambda x: x > 5)
    True
    """
    def operation(f):
        print(f(n))
        return memory(f(n))
    return operation


def add_this_many(x, el, lst):
    """ Adds el to the end of lst the number of times x occurs
    in lst.
    >>> lst = [1, 2, 4, 2, 1]
    >>> add_this_many(1, 5, lst)
    >>> lst
    [1, 2, 4, 2, 1, 5, 5]
    >>> add_this_many(2, 2, lst)
    >>> lst
    [1, 2, 4, 2, 1, 5, 5, 2, 2]
    """
    total = 0
    for i in lst:
        if i == x:
            total += 1
    for i in range(total):
        lst.append(el)


def reverse(lst):
    """ Reverses lst in place.
    >>> x = [3, 2, 4, 5, 1]
    >>> reverse(x)
    >>> x
    [1, 5, 4, 2, 3]
    """
    for i in range(len(lst) // 2):
        lst[i], lst[len(lst)-i-1] = lst[len(lst)-i-1], lst[i]


def group_by(s, fn):
    """
    The values of the dictionary are lists of elements from s. Each element e in
    a list should be constructed such that fn(e) is the same for all elements in
    that list. Finally, the key for each value should be fn(e).
    >>> group_by([12, 23, 14, 45], lambda p: p // 10)
    {1: [12, 14], 2: [23], 4: [45]}
    >>> group_by(range(-3, 4), lambda x: x * x)
    {0: [0], 1: [-1, 1], 4: [-2, 2], 9: [-3, 3]}
    """
    dict, dict_s = {}, {}
    for i in s:
        if fn(i) not in dict:
            dict[fn(i)] = [i]
        else:
            dict[fn(i)] += [i]
    for k in sorted(dict):
        dict_s[k] = dict[k]
    return dict_s


def replace_all_deep(d, x, y):
    """
    Write a function that takes in a deep dictionary d and replace
    all occurences of x as a value (not a key) with y.
    >>> d = {1: {2: 'x', 'x': 4}, 2: {4: 4, 5: 'x'}}
    >>> replace_all_deep(d, 'x', 'y')
    >>> d
    {1: {2: 'y', 'x': 4}, 2: {4: 4, 5: 'y'}}
    """
    for key, value in d.items():
        if value == x:
            d[key] = y

    for value in d.values():
        if type(value) == dict:
            replace_all_deep(value, x, y)


testmod()
