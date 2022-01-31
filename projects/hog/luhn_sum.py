def digit_sum(n):
    if n < 10:
        return n
    else:
        return digit_sum(n // 10) + n % 10


def luhn_sum(n):
    if n < 10:
        return n
    else:
        return luhn_sum_double(n // 10) + n % 10


def luhn_sum_double(n):
    luhn_digit = digit_sum(2 * (n % 10))
    if n < 10:
        return luhn_digit
    else:
        return luhn_sum(n // 10) + luhn_digit
