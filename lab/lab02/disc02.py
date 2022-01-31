from doctest import testmod, run_docstring_examples


def inverse_cascade(n):
    grow(n)
    print(n)
    shrink(n)


def f_then_g(f, g, n):
    if n:
        f(n)
        g(n)


grow = lambda n: f_then_g(grow, print, n // 10)
shrink = lambda n: f_then_g(print, shrink, n // 10)


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)


def multiply(m, n):
    """
    >>> multiply(5, 3)
    15
    >>> multiply(4, 1)
    4
    >>> multiply(15, 10)
    150
    """
    if n == 1:
        return m
    return multiply(m, n - 1) + m


def countdown(n):
    if n == 1:
        print(n)
    else:
        print(n)
        countdown(n - 1)


def countup(n):
    if n == 1:
        print(n)
    else:
        countup(n - 1)
        print(n)


def sum_digits(n):
    """
    >>> sum_digits(7)
    7
    >>> sum_digits(30)
    3
    >>> sum_digits(228)
    12
    """
    if n < 10:
        return n
    return sum_digits(n // 10) + n % 10


def count_stair_ways(n):
    if n == 1 or n == 0:
        return 1
    return count_stair_ways(n - 1) + count_stair_ways(n - 2)


def count_k(n, k):
    """
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    if n == 1 or n == 0:
        return 1
    elif n < 0:
        return 0
    return_value = 0
    for i in range(1, k + 1):
        return_value += count_k(n - i, k)
    return return_value


countdown(5)
countup(5)
run_docstring_examples(count_k, globals(), True)
testmod()
