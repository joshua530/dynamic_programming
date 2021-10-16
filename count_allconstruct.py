from typing import List


def count_allconstruct(target: str, prefixes: List[str]):
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
            results = count_allconstruct(target[len_prefix:], prefixes)

            if len(results) != 0:  # remaining substring matched
                for i in range(len(results)):
                    results[i] = [prefix] + results[i]
                combinations += results

    return combinations


def count_allconstruct_improved(target: str, prefixes: List[str], memo: dict):
    # base case
    if target in memo.keys():
        return memo[target]
    if target == "":
        return [[]]

    combinations = []

    for prefix in prefixes:
        if target.startswith(prefix):
            prefix_len = len(prefix)
            results = count_allconstruct_improved(target[prefix_len:], prefixes, memo)
            if len(results) != 0:
                for i in range(len(results)):
                    results[i] = [prefix] + results[i]
                combinations += results
    memo[target] = combinations
    return combinations


print(count_allconstruct("purple", ["purp", "p", "ur", "le", "purpl"]))
print(count_allconstruct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
print(count_allconstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(count_allconstruct("asdfasdf", ["a", "b"]))
print(
    count_allconstruct_improved(
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaad",
        ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaaaaa"],
        {},
    )
)

# Time = O(n^m)
# space = O(m)
# -> for both the improved and non-improved
