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


# print(can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"], {}))
# print(can_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"], {}))
# print(
#     can_construct(
#         "eeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
#         ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"],
#         {},
#     )
# )


def can_construct_tabulation(target: str, substrings: List[str]) -> bool:
    """
    eg target=abcdef
    (uses a clever tabulation implementation)
    0 1 2 3 4 5 6
    a b c d e f
    T F F F F F F

    - the assumption is that an index indicates whether the character before the
    character at that index is reachable(ie can we go up to but not including the
    character at the index?)
    - 0 is True because we can generate an empty substring by selecting nothing

    Here's how it technically looks like in the beginning just after seeding
    (look at the character reachability diagonally starting with '' is True, a is False...)
       0 1 2 3 4 5 6
    '' a b c d e f
       T F F F F F F

    and in the end...
       0 1 2 3 4 5 6
    '' a b c d e f
       T F T T T F T

    Time=O(m^2n)
    Space=O(m)
    """

    table = [False for i in range(len(target) + 1)]
    table[0] = True

    for i in range(len(target) + 1):
        if table[i]:  # current character is reachable
            for substring in substrings:
                index = i + len(substring)
                if target[i : i + len(substring)].startswith(substring):
                    table[index] = True  # mark last substring character as reachable
                    if index == len(target):
                        return True
    return table[len(target)]


print(
    can_construct_tabulation(
        "skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]
    )
)
print(can_construct_tabulation("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(
    can_construct_tabulation(
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
        ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"],
    )
)
