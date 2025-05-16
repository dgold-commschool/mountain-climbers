from random import *
from numeric_solver import *


def build_random_instance(n):
    puzzle = [[0 for i in range(0, row_len)] for row_len in range(1, n + 1)]
    coords = [(row_len - 1, i) for row_len in range(1, n+1) for i in range(0, row_len)]
    tot = 0
    while tot < n * (n + 1) // 2:
        coord = choice(coords)
        while puzzle[coord[0]][coord[1]] < n and tot < n * (n + 1) // 2:
            puzzle[coord[0]][coord[1]] += 1
            tot += 1
            if random() < .5: break
    if num_is_good(puzzle): return(puzzle)
    return(build_random_instance(n))

def build_from_seed(n, seed, max_iters):
    while max_iters != 0:
        
        puzzle = [[int(e) if e != "." else 0 for e in row ] for row in seed]
        coords = [(row_len - 1, i) for row_len in range(1, n+1) for i in range(0, row_len) if seed[row_len - 1][i] == "."]
        tot = sum([sum(row) for row in puzzle])
        while tot < n * (n + 1) // 2:
            coord = choice(coords)
            while puzzle[coord[0]][coord[1]] < n and tot < n * (n + 1) // 2:
                puzzle[coord[0]][coord[1]] += 1
                tot += 1
                if random() < .5: break
        if num_is_good(puzzle): return(puzzle)
        max_iters -= 1
    return(None)

pretty_print(build_random_instance(4))

pretty_print(build_from_seed(4, [".", "..", "...", "1312"], 5000))

pretty_print(build_from_seed(5, [".", "..", "...", "....", "....."], 1000))
