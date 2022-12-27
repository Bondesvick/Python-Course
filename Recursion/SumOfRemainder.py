def sum_of_digits(n):
    assert 0 <= n == int(n), 'The number has to be a positive integer only!'
    if n == 0:
        return 0
    else:
        return int(n % 10) + sum_of_digits(int(n / 10))


print(sum_of_digits(3))
