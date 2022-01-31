from doctest import testmod
from lab05 import *


def all_primes(nums):
    """Write a function that takes in a list nums and returns a new list with only the primes
    from nums. Assume that is_prime(n) is defined. You may use a while loop, a for loop, or a
    list comprehension"""
    return [n for n in nums if is_prime(n)]


def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return True
    return False


def list_of_lists(lst):
    """
    Write a function that takes in a list of positive integers and outputs
    a list of lists where the i-th list contains the integers from 0 up to,
    but not including, the i-th element of the input list.
    >>> list_of_lists([1, 2, 3])
    [[0], [0, 1], [0, 1, 2]]
    >>> list_of_lists([1])
    [[0]]
    >>> list_of_lists([])
    []
    """
    result = []
    for n in lst:
        seq = []
        for i in range(n):
            seq.append(i)
        result.append(seq)
    return result


def sum_of_nodes(t):
    """
    >>> t = tree(9,
    ...         [tree(2),
    ...         tree(4,
    ...             [tree(1)]),
    ...         tree(4,
    ...             [tree(7),
    ...             tree(3)])])
    >>> sum_of_nodes(t) # 9 + 2 + 4 + 4 + 1 + 7 + 3 = 30
    30
    """
    if is_leaf(t):
        return label(t)
    return label(t) + sum([sum_of_nodes(b) for b in branches(t)])


def sum_range(t):
    """Returns the range of the sums of t, that is, the
    difference between the largest and the smallest
    sums of t.
    >>> t = tree(9,
    ...         [tree(2),
    ...         tree(4,
    ...             [tree(1)]),
    ...         tree(4,
    ...             [tree(7),
    ...             tree(3)])])
    >>> sum_range(t) # (9 + 4 + 7) - (9 + 2) = 9
    9
    """
    def helper(t):
        if is_leaf(t):
            return [label(t), label(t)]
        else:
            a = min([helper(b)[1] for b in branches(t)])
            b = max([helper(b)[0] for b in branches(t)])
            x = label(t)
            return [b + x, a + x]
    x, y = helper(t)
    return x - y


def no_eleven(n):
    """Return a list of lists of 1's and 6's that do not
    contain 1 after 1.
    >>> no_eleven(2)
    [[6, 6], [6, 1], [1, 6]]
    >>> no_eleven(3)
    [[6, 6, 6], [6, 6, 1], [6, 1, 6], [1, 6, 6], [1, 6, 1]]
    >>> no_eleven(4)[:4] # first half
    [[6, 6, 6, 6], [6, 6, 6, 1], [6, 6, 1, 6], [6, 1, 6, 6]]
    >>> no_eleven(4)[4:] # second half
    [[6, 1, 6, 1], [1, 6, 6, 6], [1, 6, 6, 1], [1, 6, 1, 6]]
    """
    if n == 0:
        return [[]]
    elif n == 1:
        return [[6], [1]]
    else:
        a, b = no_eleven(n - 1), no_eleven(n - 2)
        return [[6] + s for s in a] + [[1, 6] + s for s in b]


def eval_with_add(t):
    """Evaluate an expression tree of * and + using only
    addition.
    >>> plus = tree('+', [tree(2), tree(3)])
    >>> eval_with_add(plus)
    5
    >>> times = tree('*', [tree(2), tree(3)])
    >>> eval_with_add(times)
    6
    >>> eval_with_add(tree('*'))
    1
    """
    if label(t) == '+':
        return sum(label(b) for b in branches(t))
    elif label(t) == '*':
        total = 1
        for b in branches(t):
            total, term = 0, total
            for i in range(label(b)):
                total = total + term
        return total
    else:
        return label(t)


testmod()
