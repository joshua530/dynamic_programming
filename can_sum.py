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


def can_sum_improved(target: int, nums: List[int], calculated: dict = {}) -> bool:
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
        if can_sum_improved(target - num, nums, calculated):
            calculated[target] = True
            return True
    calculated[target] = False
    return False

print(can_sum_improved(7,[3,1]))
print(can_sum_improved(300, [7,21], {}))
print(can_sum_improved(300, [7, 14], {}))
