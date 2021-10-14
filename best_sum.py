from typing import List

def best_sum(target:int, nums:List[int])->List[int]:
    """
    Finds the shortest combination of numbers that add up to a certain sum
    Complexity:
    m = target sum
    n = len(nums)
    -> Time = O(n^m * m) time for iterating over all branches of tree + time for copying values
    between arrays
    -> Space = O(m*m)
    """

    # base cases
    if target == 0:
        return []
    if target < 0:
        return None

    shortest_combination = None
    for num in nums:
        tmp_combination = best_sum(target-num, nums)
        if tmp_combination is not None:
            tmp = [num]+tmp_combination
            if shortest_combination is None or len(tmp) < len(shortest_combination):
                shortest_combination = tmp
    return shortest_combination


def best_sum_improved(target:int, nums:List[int],memo:dict)->List[int]:
    """
    Finds the shortest combination of numbers that add up to a certain sum
    Complexity:
    m = target sum
    n = len(nums)
    -> Time = O(n*m^2) time for iterating over all branches of tree + time for copying values
    between arrays
    -> Space = O(m*m)?
    """

    # base cases
    if target in memo.keys():
        return memo[target]

    if target == 0:
        return []
    if target < 0:
        return None

    shortest_combination = None
    for num in nums:
        tmp_combination = best_sum_improved(target-num, nums,memo)
        if tmp_combination is not None:
            tmp = [num]+tmp_combination
            if shortest_combination is None or len(tmp) < len(shortest_combination):
                shortest_combination = tmp
    memo[target] = shortest_combination
    return shortest_combination

# print(best_sum(8,[2,3,5]))
# print(best_sum(7,[5,4,3,7]))
# print(best_sum(8,[1,4,5]))
# print(best_sum(100,[1,2,5,25]))
# print(best_sum(400,[7,14]))

print(best_sum_improved(8,[2,3,5],{}))
print(best_sum_improved(7,[5,4,3,7],{}))
print(best_sum_improved(8,[1,4,5],{}))
print(best_sum_improved(100,[1,2,5,25],{}))
print(best_sum_improved(300,[7,14],{}))
print(best_sum_improved(400,[7,14],{}))
