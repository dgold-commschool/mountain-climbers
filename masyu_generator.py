from random import *
from masyu_solver import *

def mas_build_random_instance(n, mode):
    puzzle = [["." for i in range(0, row_len)] for row_len in range(1, n + 1)]
    coords = [(row_len - 1, i) for row_len in range(1, n+1) for i in range(0, row_len)]
    while len(mas_find_all_soln(puzzle,mode)) > 1:
        coord = choice(coords)
        if random() < .5:
            if puzzle[coord[0]][coord[1]] == ".": puzzle[coord[0]][coord[1]] = "b"
            elif mode == "count": puzzle[coord[0]][coord[1]] += "b"
            else: puzzle[coord[0]][coord[1]] = "b"
        else:
            puzzle[coord[0]][coord[1]] = "w"
    if mas_is_good(puzzle, mode): return(puzzle)
    return(mas_build_random_instance(n,mode))

def seeded_mas_build_random_instance(n, seed,mode):
    puzzle = [[seed[row_len - 1][i] for i in range(0, row_len)] for row_len in range(1, n + 1)]
    coords = [(row_len - 1, i) for row_len in range(1, n+1) for i in range(0, row_len) if seed[row_len - 1][i] == "."]
    while len(mas_find_all_soln(puzzle,mode)) > 1:
        coord = choice(coords)
        if random() < .5:
            if puzzle[coord[0]][coord[1]] == ".": puzzle[coord[0]][coord[1]] = "b"
            elif mode == "count": puzzle[coord[0]][coord[1]] += "b"
            else: puzzle[coord[0]][coord[1]] = "b"
        else:
            puzzle[coord[0]][coord[1]] = "w"
    if mas_is_good(puzzle, mode): return(puzzle)
    return(seeded_mas_build_random_instance(n, seed,mode))

pretty_print(mas_build_random_instance(4, "count"))
# pretty_print(seeded_mas_build_random_instance(6, [".", "00", "000", "0000", "00000", "......"], "count"))
pretty_print(seeded_mas_build_random_instance(6, ["0", "..", "000", "0000", ".....", "000000"], "count"))
