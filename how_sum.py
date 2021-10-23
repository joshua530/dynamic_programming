from typing import List


def how_sum_memoization(target: int, values: List[int], memo: dict) -> list:
    """
    Finds one combination of numbers whose sum totals to
    the target value
    Returns a list if a combination is found and None if no
    combination is found
    Worst case time = O(n^m*m); space = O(m+m) = O(m)(brute force[without the memo object])
    Memoized time=O(m*n*m)=O(n*m^2); space=O(m^2)
    """
    # base cases
    if target in memo.keys():
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None

    for val in values:
        diff = target - val
        result = how_sum_memoization(diff, values, memo)
        if result is not None:
            memo[target] = [val] + result
            return memo[target]

    memo[target] = None
    return None


# print(how_sum_memoization(8, [2, 3, 5], {}))
# print(how_sum_memoization(7, [5, 3, 4, 7], {}))
# print(how_sum_memoization(7, [2, 4], {}))
# print(how_sum_memoization(3000, [7, 14], {}))


def how_sum_tabulation(target: int, nums: List[int]) -> List[int]:
    table = [None for i in range(target + 1)]
    table[0] = []

    for i in range(target + 1):
        current = table[i]
        if current is not None:
            for num in nums:
                if i + num <= target:  # don't go out of bounds
                    table[i + num] = table[i] + [num]
                    print(table)
                    if (
                        i + num == target
                    ):  # we've found a combination that adds up to the target
                        return table[i + num]
    return []


# print(how_sum_tabulation(3000, [7, 14]))
print(how_sum_tabulation(8, [2, 3, 5]))
print(how_sum_tabulation(7, [5, 3, 4, 7]))
