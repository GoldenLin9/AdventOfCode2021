grid = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

flashes = 0
steps = 0
ngrid = [list(map(int, list(x))) for x in grid.splitlines()]

y = [-1, -1, 0, 1, 1, 1, 0, -1]
x = [0, 1, 1, 1, 0, -1, -1, -1]

def explode(r, c):
    global flashes
    for i in range(len(y)):
        nr = r + y[i]
        nc = c + x[i]
        if 0 <= nr <= len(ngrid)-1 and 0 <= nc <= len(ngrid[0])-1:
            ngrid[nr][nc] += 1
            if ngrid[nr][nc] == 10:
                ngrid[nr][nc] = float("inf")
                flashes += 1
                explode(nr, nc)

while True:
    ok = True
    for r in range(len(ngrid)):
        for c in range(len(ngrid[0])):
            ngrid[r][c] += 1
            if ngrid[r][c] == 10:
                ngrid[r][c] = float("inf")
                flashes += 1
                explode(r, c)

    for xr in range(len(ngrid)):
        for xc in range(len(ngrid[0])):
            if ngrid[xr][xc] == float("inf"):
                ngrid[xr][xc] = 0
            else:
                ok = False

    if ok:
        break
    else:
        steps += 1

print(steps)