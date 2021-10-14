def traverse_grid(n_rows: int, n_cols: int) -> int:
    """
    Finds the number of ways an n*n grid can be traversed till one
    gets to the bottom right most square
    """
    # base case = 0,x x,0 1,1(1,1 means we have reached)
    # the bottom right most square
    if n_rows == 0 or n_cols == 0:
        return 0
    elif n_rows == 1 and n_cols == 1:
        return 1

    # traverse down and right
    num_ways = traverse_grid(n_rows - 1, n_cols) + traverse_grid(n_rows, n_cols - 1)
    return num_ways


# print(traverse_grid(2, 3))
# print(traverse_grid(3, 3))
# print(traverse_grid(13, 13))
# print(traverse_grid(18, 18)) runs forever


def traverse_grid_improved(n_rows: int, n_cols: int, calculated_paths: dict = {}):
    path = "{}-{}".format(n_rows, n_cols)
    inverted_path = "{}-{}".format(n_cols, n_rows)

    # path already traversed ?
    if path in calculated_paths.keys():
        return calculated_paths[path]
    elif inverted_path in calculated_paths.keys():
        return calculated_paths[inverted_path]

    if n_rows == 0 or n_cols == 0:
        calculated_paths[path] = 0
        return calculated_paths[path]
    elif n_rows == 1 and n_cols == 1:
        calculated_paths[path] = 1
        return calculated_paths[path]

    # move down and right respectively
    calculated_paths[path] = (
        traverse_grid_improved(n_rows - 1, n_cols, calculated_paths)
        + traverse_grid_improved(n_rows, n_cols - 1, calculated_paths)
    )
    return calculated_paths[path]


print(traverse_grid_improved(2, 3))
# print(traverse_grid_improved(3, 2))
# print(traverse_grid_improved(18, 18))

# 40398

def traverse_grid_space_complexity(n_rows: int, n_cols: int, calculated_paths: dict = {}):
    path = "{}-{}".format(n_rows, n_cols)
    inverted_path = "{}-{}".format(n_cols, n_rows)

    # path already traversed ?
    if path in calculated_paths.keys():
        return
    # elif inverted_path in calculated_paths.keys():
    #     return

    if n_rows == 0 or n_cols == 0:
        calculated_paths[path] = 0
        return
    elif n_rows == 1 and n_cols == 1:
        calculated_paths[path] = 1
        return

    # move down and right respectively
    calculated_paths[path] = (
        traverse_grid_improved(n_rows - 1, n_cols, calculated_paths)
        + traverse_grid_improved(n_rows, n_cols - 1, calculated_paths)
    )
    return calculated_paths


print(len(traverse_grid_space_complexity(21,18)))
