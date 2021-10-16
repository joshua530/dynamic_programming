from typing import List


def can_construct(target: str, substrings: List[str], memo: dict):
    """
    Checks whether a string can be constructed by concatenating a
    number of provided substrings where one is allowed to use each of
    the substrings more than once
    Brute force:
    time -> O(n^m*m)
    space -> O(m^2)
    Memoized:
    time -> O(n*m^2)
    space -> O(m^2)
    """
    # base case
    if target in memo.keys():
        return memo[target]
    if target == "":
        return True

    for substring in substrings:
        len_substr = len(substring)
        # check whether substring is a prefix to the target
        if target.startswith(substring):
            # trim the prefix and compare the rest of the
            # substring
            result = can_construct(target[len_substr:], substrings, memo)
            if result:
                memo[target] = True
                return True
    memo[target] = False
    return False


print(can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"], {}))
print(can_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"], {}))
print(
    can_construct(
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
        ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"],
        {},
    )
)
