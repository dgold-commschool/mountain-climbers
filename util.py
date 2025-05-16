def pretty_print(puzzle):
    if puzzle == None: return()
    print()
    indent = len(puzzle[-1]) - 1
    for row in puzzle:
        print((2 * indent + 1) * " " + "   ".join([str(i) for i in row]))
        print()
        indent -= 1
    return()

def follow_path(puzzle, index, path):
    row = len(puzzle) - 1
    l = [puzzle[row][index]]
    for move in path:
        row -= 1
        if move == "R":
            l.append(puzzle[row][index])
        else:
            index = index - 1
            l.append(puzzle[row][index])
            
    return(l)

def get_paths(soln):
    if len(soln) == 1:
        return([""])
    index_of_one = soln.index(1)
    paths = ["R"] * index_of_one + [""] + ["L"] * (len(soln) - index_of_one - 1)
    next_up = [i - 1 for i in soln if i != 1]
    after = get_paths(next_up)

    after = after[:index_of_one] + [""] + after[index_of_one:]
    return([paths[i] + after[i] for i in range(len(soln))])
