
from util import *

puzz1 = [[0],
         [0, 0],
         [3, 2, 1]]

puzz2 = [[3],
         [2, 0],
         [1, 0, 0]]

non_unique1 = [[1],
               [1, 1],
               [1, 1, 1]]

def num_check_soln(puzzle, soln):
    paths = get_paths(soln)
    for index in range(0, len(soln)):
        height = len(paths[index]) + 1
        if sum(follow_path(puzzle, index, paths[index])) != height:
            # print("Should be height " + str(height) + ", instead height " + str(follow_path(puzzle, index, paths[index])))
            return(False)
    return(True)
