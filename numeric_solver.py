from numeric_checker import *
import itertools

def num_find_all_soln(puzzle):
    n = len(puzzle[-1])
    solns = []
    for soln in list(itertools.permutations(range(1, n+1))):
        if num_check_soln(puzzle, soln):
            solns.append(soln)

    return(solns)

def num_is_good(puzzle):
    n = len(puzzle[-1])
    found = False
    for soln in list(itertools.permutations(range(1, n+1))):
        if num_check_soln(puzzle, soln):
            if found: return(False)
            else: found = True

    return(found)
