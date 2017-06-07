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

def fix(s, debug):
    fixed = 0
    for y in range(9):
        for x in range(9):
            if s[y][x] == 0 and len(cand[y][x]) == 1:
                s[y][x] = cand[y][x][0]
                if debug > 1:
                    print("Fixing", y, "x", x, "with", cand[y][x][0])
                fixed += 1
    if debug:
        print("Fixed", fixed, "sudoku(s).")
    return fixed

def hidden_single(s, y, x, k):
    y_hidden = False
    x_hidden = False
    if ((y % 3 == 0 and (s[y + 1][x] or k in ey[y + 1]) and (s[y + 2][x] or k in ey[y + 2])) or
        (y % 3 == 1 and (s[y - 1][x] or k in ey[y - 1]) and (s[y + 1][x] or k in ey[y + 1])) or
        (y % 3 == 2 and (s[y - 2][x] or k in ey[y - 2]) and (s[y - 1][x] or k in ey[y - 1]))):
        y_hidden = True
    if ((x % 3 == 0 and (s[y][x + 1] or k in ex[x + 1]) and (s[y][x + 2] or k in ex[x + 2])) or
        (x % 3 == 1 and (s[y][x - 1] or k in ex[x - 1]) and (s[y][x + 1] or k in ex[x + 1])) or
        (x % 3 == 2 and (s[y][x - 2] or k in ex[x - 2]) and (s[y][x - 1] or k in ex[x - 1]))):
        x_hidden = True
    return y_hidden and x_hidden

def find_hidden_singles(s, debug):
    fixed = 0
    for y in range(9):
        for x in range(9):
            if s[y][x] == 0 and len(cand[y][x]) > 0:
                for i in range(len(cand[y][x])):
                    if hidden_single(s, y, x, cand[y][x][i]):
                        s[y][x] = cand[y][x][i]
                        if debug > 1:
                            print("Hidden single", cand[y][x][i], "on", y, "x", x)
                        fixed += 1
    if debug:
        print("Found", fixed, "hidden single(s).")
    return fixed

def naked_single(s, y, x, k):
    y_naked = False
    x_naked = False
    if ((y % 3 == 0 and k in ey[y + 1] and k in ey[y + 2]) or
        (y % 3 == 1 and k in ey[y - 1] and k in ey[y + 1]) or
        (y % 3 == 2 and k in ey[y - 2] and k in ey[y - 1])):
        y_naked = True
    if ((x % 3 == 0 and k in ex[x + 1] and k in ex[x + 2]) or
        (x % 3 == 1 and k in ex[x - 1] and k in ex[x + 1]) or
        (x % 3 == 2 and k in ex[x - 2] and k in ex[x - 1])):
        x_naked = True
    return y_naked and x_naked

def find_naked_singles(s, debug):
    fixed = 0
    for y in range(9):
        for x in range(9):
            if s[y][x] == 0 and len(cand[y][x]) > 0:
                for i in range(len(cand[y][x])):
                    if naked_single(s, y, x, cand[y][x][i]):
                        s[y][x] = cand[y][x][i]
                        if debug > 1:
                            print("Naked single", cand[y][x], "on", y, "x", x)
                        fixed += 1
    if debug:
        print("Found", fixed, "naked single(s).")
    return fixed

def main(n, debug):
    s = sudokus[n]
    f = show_sudoku(s)
    make_e_cand()
    while (f < 81):
        update_e_cand(s)
        if debug > 1:
            show_cand(s)
        fixed = fix(s, debug)
        found_naked_single = find_naked_singles(s, debug)
        found_hidden_single = find_hidden_singles(s, debug)
        if fixed + found_naked_single + found_hidden_single == 0:
            break;
        f += fixed + found_naked_single + found_hidden_single
        if debug:
            print(str(81-f), "more to go.")
    show_sudoku(s)

main(2, 2)