def fib(a: int, b: int) -> None:
    c = a + b
    print(c)
    if c < 100:
        fib(b, c)

fib(0, 1)
