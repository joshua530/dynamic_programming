"""
Contains various implementations for computing dynamic programming problems
for the fibonacci series
"""


def fib_memoization(n, computed_fibs: dict = {}) -> int:
    if n < 0:
        raise ValueError("Invalid argument '{}'".format(n))
    if n == 0:
        return 0
    if n <= 2:
        return 1
    if n in computed_fibs.keys():
        return computed_fibs[n]
    computed_fibs[n] = fib_memoization(n - 1, computed_fibs) + fib_memoization(
        n - 2, computed_fibs
    )
    return computed_fibs[n]


# print(fib_memoization(1))
# print(fib_memoization(2))
# print(fib_memoization(3))
print(fib_memoization(20))
# print(fib_memoization(40))
# print(fib_memoization(400))
print(fib_memoization(1000))


def fib_tabulation(n: int):
    """
    Uses a sliding window to form the table used for calculating the
    fibonacci numbers
    """
    if n < 0:
        raise ValueError(f"{n} is out of bounds")

    fibs_table = [0 for i in range(n + 1)]
    if len(fibs_table) > 1:
        fibs_table[1] = 1

    for i in range(n + 1):
        start = i  # beginning of sliding window
        mid = i + 1  # middle of sliding window
        end = i + 2  # end of sliding window

        # ensure sliding window positions are not out of bounds
        if mid <= n:
            fibs_table[mid] += fibs_table[start]
        if end <= n:
            fibs_table[end] += fibs_table[start]
    return fibs_table[n]


print(fib_tabulation(00))
