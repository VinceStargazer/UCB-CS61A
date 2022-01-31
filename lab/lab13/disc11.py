from doctest import testmod, run_docstring_examples
from operator import add, mul
from tree import *


def merge(s1, s2):
    """ Merges two sorted lists
    >>> merge([1, 3], [2, 4])
    [1, 2, 3, 4]
    >>> merge([1, 2], [])
    [1, 2]
    """
    if not s1:
        return s2
    elif not s2:
        return s1
    elif s1[0] < s2[0]:
        return [s1[0]] + merge(s1[1:], s2)
    else:
        return [s2[0]] + merge(s1, s2[1:])


def subset_sum(seq, k):
    """
    >>> subset_sum([2, 4, 7, 3], 5) # 2 + 3 = 5
    True
    >>> subset_sum([1, 9, 5, 7, 3], 2)
    False
    >>> subset_sum([2, 7, 5, 9], 2)
    True
    >>> subset_sum([], 1)
    False
    >>> subset_sum([1, 2, 3, 4, 5], 10)
    True
    """
    if not seq:
        return False
    elif k == seq[0]:
        return True
    else:
        return subset_sum(seq[1:], k - seq[0]) if k > seq[0] else subset_sum(seq[1:], k)


def average(t):
    """
    Returns the average value of all the nodes in t.
    >>> t0 = Tree(0, [Tree(1), Tree(2, [Tree(3)])])
    >>> average(t0)
    1.5
    >>> t1 = Tree(8, [t0, Tree(4)])
    >>> average(t1)
    3.0
    """
    def sum_helper(t):
        total, count = t.label, 1
        for b in t.branches:
            sub_total, sub_count = sum_helper(b)
            total += sub_total
            count += sub_count
        return total, count
    total, count = sum_helper(t)
    return total / count


def accumulate(iterable, f):
    """
    >>> list(accumulate([1, 2, 3, 4, 5], add))
    [1, 3, 6, 10, 15]
    >>> list(accumulate([1, 2, 3, 4, 5], mul))
    [1, 2, 6, 24, 120]
    """
    it = iter(iterable)
    rec = next(it)
    for _ in range(len(iterable)):
        yield rec
        try: rec = f(rec, next(it))
        except StopIteration: return


def hailstone_sequence(n):
    """
    >>> hs_gen = hailstone_sequence(10)
    >>> next(hs_gen)
    10
    >>> next(hs_gen)
    5
    >>> for i in hs_gen:
    ...     print(i)
    16
    8
    4
    2
    1
    """
    yield n
    while n != 1:
        if n % 2 == 0:
            yield n // 2
            n //= 2
        else:
            yield 3 * n + 1
            n = 3 * n + 1


def tree_sequence(t):
    """
    >>> t = Tree(1, [Tree(2, [Tree(5)]), Tree(3, [Tree(4)])])
    >>> print(list(tree_sequence(t)))
    [1, 2, 5, 3, 4]
    """
    yield t.label
    for b in t.branches:
        yield from tree_sequence(b)


def repeated(f):
    """
    >>> double = lambda x: 2 * x
    >>> funcs = repeated(double)
    >>> identity = next(funcs)
    >>> identity(1)
    1
    >>> double = next(funcs)
    >>> double(1)
    2
    >>> quad = next(funcs)
    >>> oct = next(funcs)
    >>> quad(1)
    4
    >>> oct(1)
    8
    >>> [g(1) for _, g in
    ... zip(range(5), repeated(lambda x: 2 * x))]
    [1, 2, 4, 8, 16]
    """
    g = lambda x: x
    while True:
        yield g
        g = lambda x: f(g(x))


def all_paths(t):
    """
    >>> t = Tree(1, [Tree(2, [Tree(5)]), Tree(3, [Tree(4)])])
    >>> print(list(all_paths(t)))
    [[1, 2, 5], [1, 3, 4]]
    """
    if t.is_leaf():
        yield [t.label]
    for b in t.branches:
        for path in all_paths(b):
            yield [t.label] + path


class FlatMapper:
    """
    A FlatMapper takes a function fn that returns an iterable
    value. The flat_map method takes an iterable s and
    returns a generator over all values in the iterables
    returned by calling fn on each element of s.
    >>> stutter = lambda x: [x, x]
    >>> m = FlatMapper(stutter)
    >>> g = m.flat_map((2, 3, 4, 5))
    >>> type(g)
    <class 'generator'>
    >>> list(g)
    [2, 2, 3, 3, 4, 4, 5, 5]
    """
    def __init__(self, fn):
        self.fn = fn

    def flat_map(self, s):
        lst = map(self.fn, s)
        for i in lst:
            yield from i


def amplify(f, x):
    """Yield the longest sequence x, f(x), f(f(x)), ... that
    are all true values.
    >>> list(amplify(lambda s: s[1:], 'boxes'))
    ['boxes', 'oxes', 'xes', 'es', 's']
    >>> list(amplify(lambda x: x//2-1, 14))
    [14, 6, 2]
    """
    while x:
        yield x
        x = f(x)


run_docstring_examples(amplify, globals(), True)
