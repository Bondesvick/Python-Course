def gcd(a, b):
    assert a == int(a) and b == int(b), 'Number must be a valid integer'
    if a < 0:
        a = a * -1
    if b < 0:
        b = b * -1
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


print(gcd(48, 18))
