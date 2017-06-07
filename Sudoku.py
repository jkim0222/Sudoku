# Sudoku by Python
# 6/6/17
# Jungju Kim

sudokus = [[[1, 0, 4, 9, 0, 2, 0, 0, 6],    # Easiest
            [9, 0, 0, 1, 0, 4, 5, 2, 0],
            [2, 8, 0, 0, 3, 0, 9, 0, 1],
            [3, 0, 6, 4, 7, 0, 8, 0, 0],
            [0, 4, 0, 8, 2, 5, 0, 3, 0],
            [5, 0, 8, 0, 0, 0, 1, 7, 4],
            [0, 5, 2, 7, 0, 0, 4, 9, 0],
            [0, 1, 0, 0, 9, 3, 0, 6, 8],
            [0, 3, 9, 0, 4, 8, 0, 0, 5]],
           [[0, 3, 5, 0, 7, 0, 1, 0, 4],    # Medium 1
            [4, 0, 9, 0, 3, 8, 0, 0, 5],
            [8, 1, 0, 0, 0, 0, 9, 0, 0],
            [0, 0, 0, 0, 8, 3, 0, 0, 0],
            [0, 9, 0, 0, 0, 0, 0, 5, 0],
            [0, 0, 0, 0, 6, 2, 0, 0, 0],
            [0, 0, 4, 0, 0, 0, 0, 1, 7],
            [9, 0, 0, 8, 5, 0, 3, 0, 6],
            [1, 0, 6, 0, 4, 0, 8, 2, 0]],
           [[0, 2, 0, 6, 0, 8, 0, 0, 0],    # Medium 2
            [5, 8, 0, 0, 0, 9, 7, 0, 0],
            [0, 0, 0, 0, 4, 0, 0, 0, 0],
            [3, 7, 0, 0, 0, 0, 5, 0, 0],
            [6, 0, 0, 0, 0, 0, 0, 0, 4],
            [0, 0, 8, 0, 0, 0, 0, 1, 3],
            [0, 0, 0, 0, 2, 0, 0, 0, 0],
            [0, 0, 9, 8, 0, 0, 0, 3, 6],
            [0, 0, 0, 3, 0, 6, 0, 9, 0]]]

ey = []
ex = []
ei = []
cand = []

def show_sudoku(s):
    fixed = 0
    print('-----------------------------')
    for y in range(9):
        for x in range(9):
            if s[y][x]:
                print(' ' + str(s[y][x]), end = ' ')
                fixed += 1
            else:
                print('  ', end = ' ')
            if x % 3 == 2:
                if x != 8:
                    print('|', end = '')
                else:
                    print()
        if y % 3 == 2:
            print('-----------------------------')
    print('(' + str(fixed) + '/81)')
    return fixed

def make_e_cand():
    for y in range(9):
        ey.append([])
    for x in range(9):
        ex.append([])
    for i in range(9):
        ei.append([])
    for y in range(9):
        cand.append([])
        for x in range(9):
            cand[y].append([1, 2, 3, 4, 5, 6, 7, 8, 9])

def update_e_cand(s):
    for y in range(9):
        for x in range(9):
            if s[y][x]:
                if not (s[y][x] in ey[y]):
                    ey[y].append(s[y][x])
                if not (s[y][x] in ex[x]):
                    ex[x].append(s[y][x])
                i = (y // 3) * 3 + x // 3
                if not (s[y][x] in ei[i]):
                    ei[i].append(s[y][x])
    for y in range(9):
        for x in range(9):
            for i in range(len(ey[y])):
                if ey[y][i] in cand[y][x]:
                    cand[y][x].remove(ey[y][i])
            for i in range(len(ex[x])):
                if ex[x][i] in cand[y][x]:
                    cand[y][x].remove(ex[x][i])
            i = (y // 3) * 3 + x // 3
            for j in range(len(ei[i])):
                if ei[i][j] in cand[y][x]:
                    cand[y][x].remove(ei[i][j])

def show_e():
    for y in range(9):
        print('ey'+str(y)+':', ey[y])
    for x in range(9):
        print('ex'+str(x)+':', ex[x])
    for i in range(9):
        print('ei'+str(i)+':', ei[i])

def show_cand(s):
    for y in range(9):
        for x in range(9):
            if s[y][x] == 0:
                print("Candidates for", y, "x", x, "=", cand[y][x])

def find_naked_singles(s, debug):
    found = 0
    for y in range(9):
        for x in range(9):
            if s[y][x] == 0 and len(cand[y][x]) == 1:
                s[y][x] = cand[y][x][0]
                if debug > 1:
                    print("Naked single", cand[y][x][0], "on", y, "x", x)
                found += 1
    if debug:
        print("Found", found, "naked single(s).")
    return found

def find_hidden_singles(s, debug):
    found = 0
    for y in range(9):
        n_cands = [0] * 10      # 10 for readability
        hidden_in = [0] * 10
        for x in range(9):
            if s[y][x] == 0:
                for i in range(len(cand[y][x])):
                    n_cands[cand[y][x][i]] += 1
                    hidden_in[cand[y][x][i]] = x
        for i in range(1, 10):
            if n_cands[i] == 1:
                s[y][hidden_in[i]] = i
                if debug > 1:
                    print("Hidden single", i, "on row", y, "x = ", hidden_in[i])
                found += 1
    for x in range(9):
        n_cands = [0] * 10      # 10 for readability
        hidden_in = [0] * 10
        for y in range(9):
            if s[y][x] == 0:
                for i in range(len(cand[y][x])):
                    n_cands[cand[y][x][i]] += 1
                    hidden_in[cand[y][x][i]] = y
        for i in range(1, 10):
            if n_cands[i] == 1:
                s[hidden_in[i]][x] = i
                if debug > 1:
                    print("Hidden single", i, "on column", x, "y = ", hidden_in[i])
                found += 1
    for i in range(9):
        n_cands = [0] * 10      # 10 for readability
        hidden_in_y = [0] * 10
        hidden_in_x = [0] * 10
        for y in range((i // 3) * 3, (i // 3) * 3 + 3):
            for x in range((i % 3) * 3, (i % 3) * 3 + 3):
                if s[y][x] == 0:
                    for j in range(len(cand[y][x])):
                        n_cands[cand[y][x][j]] += 1
                        hidden_in_y[cand[y][x][j]] = y
                        hidden_in_x[cand[y][x][j]] = x
        for j in range(1, 10):
            if n_cands[j] == 1:
                s[hidden_in_y[j]][hidden_in_x[j]] = j
                if debug > 1:
                    print("Hidden single", j, "in block", i, "on", hidden_in_y[j], "x", hidden_in_x[j])
                found += 1
    if debug:
        print("Found", found, "hidden single(s).")
    return found

def main(n, debug):
    s = sudokus[n]
    f = show_sudoku(s)
    make_e_cand()
    while (f < 81):
        update_e_cand(s)
        found = 0
        if debug > 1:
            show_cand(s)
        found += find_naked_singles(s, debug)
        found += find_hidden_singles(s, debug)
        if found == 0:
            break;
        f += found
        if debug:
            print(str(81-f), "more to go.")
    show_sudoku(s)

main(1, 2)