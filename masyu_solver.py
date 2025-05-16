from masyu_checker import *
import itertools

def mas_find_all_soln(puzzle, mode):
    n = len(puzzle[-1])
    solns = []
    for soln in list(itertools.permutations(range(1, n+1))):
        if mode != "count" and mas_check_soln(puzzle, soln):
            solns.append(soln)
        if mode == "count" and mas_count_check_soln(puzzle, soln):
            solns.append(soln)

    return(solns)

def mas_is_good(puzzle, mode):
    n = len(puzzle[-1])
    found = False
    for soln in list(itertools.permutations(range(1, n+1))):
        if mode != "count" and mas_check_soln(puzzle, soln):
            if found: return(False)
            else: found = True
        if mode == "count" and mas_count_check_soln(puzzle, soln):
            if found: return(False)
            else: found = True

    return(found)

"""
print(mas_find_all_soln(puzz1))
print(mas_find_all_soln(puzz2))
print(mas_find_all_soln(impossible_puzzle1))"""

puzz3 = ["b", "..", "...", "....", ".....", ["w", "bb", "b", "b", "w", "w"]]

print(mas_find_all_soln(puzz3, "count"))