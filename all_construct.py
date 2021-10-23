from typing import List
from copy import deepcopy
import random


def all_construct(target: str, prefixes: List[str]):
    """
    Finds all possible substring combinations to
    construct the target string
    """
    # base case
    if target == "":
        return [[]]

    combinations = []

    for prefix in prefixes:
        if target.startswith(prefix):
            len_prefix = len(prefix)
            results = all_construct(target[len_prefix:], prefixes)

            if len(results) != 0:  # remaining substring matched
                for i in range(len(results)):
                    results[i] = [prefix] + results[i]
                combinations += results

    return combinations


def all_construct_memoization(target: str, prefixes: List[str], memo: dict):
    # base case
    if target in memo.keys():
        return memo[target]
    if target == "":
        return [[]]

    combinations = []

    for prefix in prefixes:
        if target.startswith(prefix):
            prefix_len = len(prefix)
            results = all_construct_memoization(target[prefix_len:], prefixes, memo)
            if len(results) != 0:
                for i in range(len(results)):
                    results[i] = [prefix] + results[i]
                combinations += results
    memo[target] = combinations
    return combinations


# print(all_construct("purple", ["purp", "p", "ur", "le", "purpl"]))
# print(all_construct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
# print(all_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
# print(all_construct("asdfasdf", ["a", "b"]))
# print(
#     all_construct_memoization(
#         "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaad",
#         ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaaaaa"],
#         {},
#     )
# )

# Time = O(n^m)
# space = O(m)
# -> for both the improved and non-improved


def all_construct_tabulation(target: str, substrings: List[str]):
    """
    Time = ~O(n^m)
    Space = ~O(n^m)
    """
    table = [[] for i in range(len(target) + 1)]
    table[0] = [[]]

    for i in range(len(target) + 1):
        if len(table[i]) != 0:
            for substring in substrings:
                if target[i : i + len(substring)].startswith(substring):
                    modified = deepcopy(table[i])
                    for j in range(len(modified)):
                        modified[j] += [substring]
                    table[i + len(substring)] += modified
    return table[len(target)]


# print(all_construct_tabulation("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
# print(all_construct_tabulation("purple", ["purp", "p", "ur", "le", "purpl"]))
# print(all_construct_tabulation("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
# print(
#     all_construct_tabulation(
#         "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaad",
#         ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaaaaa"],
#     )
# )
print(
    all_construct_tabulation(
        "skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]
    )
)
# print(all_construct_tabulation("cat", ["dog", "bird"]))
