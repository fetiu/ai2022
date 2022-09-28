from copy import deepcopy

grid = '''
{}│{}│{}
──┼──┼──
{}│{}│{}
──┼──┼──
{}│{}│{}
'''

EMPTY = '  '
SPACE = ' '

mark = [[EMPTY]*3 for i in range(3)]

def draw(mark):
    print(grid.format(mark[0][0], mark[0][1], mark[0][2],
                      mark[1][0], mark[1][1], mark[1][2],
                      mark[2][0], mark[2][1], mark[2][2]))

def out(x, y):
    return (x < 0 or x > 2 or y < 0 or y > 2)

def move(x, y, dx, dy):
    x += dx
    y += dy
    if not out(x, y) and (mark[y][x] != '  '):
        return move(x, y, dx, dy)
    return x,y

def rehome():
    for y in range(3):
        for x in range(3):
            if mark[y][x] == EMPTY:
                return x,y
    raise SystemError('Game Over')

turn = True
def place(x, y):
    global turn, mark
    if (turn):
        mark[y][x] = '⭕️'
        turn = False
    else:
        mark[y][x] = '❌'
        turn = True;
    draw(mark)

x,y = 0,0
def process(key):
    global x, y
    dmap = {
        'a': (-1, 0),
        's': (0, 1),
        'd': (1, 0),
        'w': (0, -1),
    }
    if (key == SPACE):
        place(x, y)
        x,y = rehome()
    tmp = deepcopy(mark)
    if (key in dmap.keys()):
        backup = x,y
        dx, dy = dmap[key]
        x,y = move(x, y, dx, dy)
        if out(x,y):
            x,y = backup
    tmp[y][x] = '🔻'
    draw(tmp)

place(1,1);
process('')
while True:
    process(input());
