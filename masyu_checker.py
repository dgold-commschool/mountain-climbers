from util import *

puzz1 = [".",
         "b.",
         "..."]

puzz2 = ["b",
         "w.",
         "..."]

impossible_puzzle1 = [".",
                      "bb",
                      "..."]

def mas_check_soln(puzzle, soln):
    paths = get_paths(soln)
    for index in range(0, len(soln)):
        steps = paths[index]
        squares = follow_path(puzzle, index, steps)
        if "w" in squares and ("LR" in steps or "RL" in steps):
            return(False)
        if "b" in squares and not ("LR" in steps or "RL" in steps):
            return(False)
        # if squares.count("w") > 1 or squares.count("b") > 1: 
        #    return(False)
    return(True)

def mas_count_check_soln(puzzle, soln):
    paths = get_paths(soln)
    for index in range(0, len(soln)):
        steps = "".join(paths[index])
        squares = "".join(follow_path(puzzle, index, steps))
        if "w" in squares and ("LR" in steps or "RL" in steps):
            return(False)
        if squares.count("w") > 1: 
            return(False)
        if (squares.count("b") > 0) and (squares.count("b") != steps.count("RL") + steps.count("LR")): 
            return(False)
    return(True)

impossible_puzzle2 = [".", "w.", "w.w", [".", "w", "bb", "."]]

