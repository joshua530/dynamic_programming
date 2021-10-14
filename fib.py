def fib(n, computed_fibs: dict = {}) -> int:
    "Computes fibonacci numbers"

    if n < 1:
        raise ValueError("Invalid argument '{}'".format(n))
    if n <= 2:
        return 1
    if n in computed_fibs.keys():
        return computed_fibs[n]
    computed_fibs[n] = fib(n - 1, computed_fibs) + fib(n - 2, computed_fibs)
    return computed_fibs[n]


print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(40))
print(fib(400))
print(fib(1000))
