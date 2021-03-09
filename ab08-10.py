def ggt(a: int, b: int) -> int:
    if a == 0:
        return b
    while b != 0:
        if a > b:
            a -= b
        else:
            b -= a
    return a

print(ggt(10, 15))
