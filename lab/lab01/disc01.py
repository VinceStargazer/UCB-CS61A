from doctest import testmod, run_docstring_examples


def wears_jacket(temp, raining):
    """
    >>> wears_jacket(90, False)
    False
    >>> wears_jacket(40, False)
    True
    >>> wears_jacket(100, True)
    True
    """
    return temp < 60 or raining == True


def handle_overflow(s1, s2):
    """
    >>> handle_overflow(27, 15)
    No overflow
    >>> handle_overflow(35, 29)
    Move to Section 2: 1
    >>> handle_overflow(20, 32)
    Move to Section 1: 10
    >>> handle_overflow(35, 30)
    No space left in either section
    """
    if s1 < 30 and s2 < 30:
        print("No overflow")
    elif s1 >= 30 and s2 < 30:
        print(f"Move to Section 2: {30 - s2}")
    elif s1 < 30 and s2 >= 30:
        print(f"Move to Section 1: {30 - s1}")
    else:
        print("No space left in either section")


def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    return n % 2 != 0


def keep_ints(cond, n):
    """Print out all integers 1..i..n where cond(i) is true
    >>> def is_even(x):
    ...     # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> keep_ints(is_even, 5)
    2
    4
    """
    for i in range(1, n+1):
        if cond(i):
            print(i)


def keep_ints2(n):
    """Print out all integers 1..i..n where cond(i) is true
    >>> def is_even(x):
    ...     # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> keep_ints2(5)(is_even)
    2
    4
    """
    def exam(cond):
        for i in range(1, n+1):
            if cond(i):
                print(i)
    return exam


testmod()