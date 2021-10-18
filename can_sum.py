from typing import List


def can_sum(target: int, nums: List[int]) -> bool:
    if target == 0:
        return True
    if target < 0:
        return False

    for num in nums:
        if can_sum(target - num, nums):
            return True
    return False


def can_sum_memoization(target: int, nums: List[int], calculated: dict = {}) -> bool:
    """
    Checks whether a number can be obtained by adding together numbers in a list
    Assumption: a number can be used more than once
    """
    # base cases
    if target in calculated.keys():
        return calculated[target]
    if target == 0:
        return True
    if target < 0:
        return False

    for num in nums:
        if can_sum_memoization(target - num, nums, calculated):
            calculated[target] = True
            return True
    calculated[target] = False
    return False


# print(can_sum_memoization(7, [3, 1], {}))
# print(can_sum_memoization(300, [7, 21], {}))
# print(can_sum_memoization(300, [7, 14], {}))


def can_sum_tabulation(target: int, nums: List[int]) -> bool:
    """Time=O(mn); space=O(m) where m=target, n=len(nums)"""
    # first fill in with data related to the one that'll be returned
    table = [False for i in range(target + 1)]
    # zero will always return true since no element needs to be picked from
    # the list
    table[0] = True

    for i in range(len(table)):
        for j in range(len(nums)):
            current = nums[j]
            if i + current < len(table) and table[i] == True:
                table[i + current] = True
    print(table)
    return table[target]


print(can_sum_tabulation(7, [5, 3, 4]))
print(can_sum_tabulation(7, [2, 4]))
print(can_sum_tabulation(100, [7]))
