from typing import List


def count_construct(target: str, prefixes: List[str]) -> int:
    """
    Counts the number of different combinations that the
    prefixes can be put together to form the target string
    Time = O(n^m*m)
    Space = O(m^2)
    """
    # base case
    if target == "":
        return 1

    num_matches = 0

    for prefix in prefixes:
        if target.startswith(prefix):
            len_prefix = len(prefix)
            result = count_construct(target[len_prefix:], prefixes)
            num_matches += result

    return num_matches


print(count_construct("purple", ["purp", "p", "ur", "le", "purpl"]))
print(count_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))


def count_construct_improved(target: str, prefixes: List[str], memo: dict) -> int:
    """
    Memoized can_count
    Time=O(n*m^2)
    Space=O(m^2)
    """
    # base case
    if target in memo.keys():
        return memo[target]
    if target == "":
        return 1

    num_matches = 0
    for prefix in prefixes:
        if target.startswith(prefix):
            len_prefix = len(prefix)
            result = count_construct_improved(target[len_prefix:], prefixes, memo)
            num_matches += result

    memo[target] = num_matches
    return num_matches


print(count_construct_improved("purple", ["purp", "p", "ur", "le", "purpl"], {}))
print(count_construct_improved("abcdef", ["ab", "abc", "cd", "def", "abcd"], {}))
print(
    count_construct_improved(
        "enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"], {}
    )
)
print(
    count_construct_improved(
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
        ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"],
        {},
    )
)
