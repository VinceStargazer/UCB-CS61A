from doctest import testmod
from lab08 import Link
from lab08_extra import Tree


def skip(lst):
    """
    >>> a = Link(1, Link(2, Link(3, Link(4))))
    >>> a
    Link(1, Link(2, Link(3, Link(4))))
    >>> b = skip(a)
    >>> b
    Link(1, Link(3))
    >>> a
    Link(1, Link(2, Link(3, Link(4))))
    """
    if lst is Link.empty:
        return Link.empty
    elif lst.rest is Link.empty or lst.rest.rest is Link.empty:
        return Link(lst.first)
    return Link(lst.first, skip(lst.rest.rest))


def skip(lst):
    """
    >>> a = Link(1, Link(2, Link(3, Link(4, Link(5)))))
    >>> b = skip(a)
    >>> b
    >>> a
    Link(1, Link(3, Link(5)))
    """
    if lst.rest is not Link.empty:
        if lst.rest.rest is Link.empty:
            lst.rest = Link.empty
        else:
            lst.rest = lst.rest.rest
            skip(lst.rest)
    return None


def reverse(lnk):
    """
    >>> a = Link(1, Link(2, Link(3)))
    >>> b = reverse(a)
    >>> b
    Link(3, Link(2, Link(1)))
    >>> a
    Link(1, Link(2, Link(3)))
    """
    s = Link.empty
    for i in link_to_list(lnk):
        s = Link(i, s)
    return s


def link_to_list(lnk):
    if lnk.rest is Link.empty:
        return [lnk.first]
    return [lnk.first] + link_to_list(lnk.rest)


def contains(elem, n, t):
    """
    >>> t1 = Tree(1, [Tree(1, [Tree(2)])])
    >>> contains(1, 2, t1)
    True
    >>> contains(2, 2, t1)
    False
    >>> contains(2, 1, t1)
    True
    >>> t2 = Tree(1, [Tree(2), Tree(1, [Tree(1), Tree(2)])])
    >>> contains(1, 3, t2)
    True
    >>> contains(2, 2, t2) # Not on a path
    False
    """
    if n == 0:
        return True
    elif t.is_leaf():
        return t.label == elem and n <= 1
    elif t.label == elem:
        return any([contains(elem, n-1, b) for b in t.branches])
    else:
        return any([contains(elem, n, b) for b in t.branches])


def factor_tree(n):
    """
    >>> t = factor_tree(20)
    >>> print(t)
    20
      2
      10
        2
        5
    """
    for i in range(2, n // 2):
        if n % i == 0:
            return Tree(n, [Tree(i), factor_tree(n // i)])
    return Tree(n)


def slice_reverse(s, i, j):
    """
    >>> s = Link(1, Link(2, Link(3)))
    >>> slice_reverse(s, 1, 2)
    >>> s
    Link(1, Link(2, Link(3)))
    >>> s = Link(1, Link(2, Link(3, Link(4, Link(5)))))
    >>> slice_reverse(s, 2, 4)
    >>> s
    Link(1, Link(2, Link(4, Link(3, Link(5)))))
    """
    start = s
    for _ in range(i - 1):
        start = start.rest
    reverse = Link.empty
    current = start.rest
    for _ in range(j - i):
        rest = current.rest
        current.rest = reverse
        reverse = current
        current = rest
    start.rest.rest = current
    start.rest = reverse


testmod()
