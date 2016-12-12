from random import shuffle, randrange
from time import sleep
import os

def make_maze(w = 16, h = 16):
    vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]

    ver = [["|  "] * w + ['|'] for _ in range(h)] + [[]]
    hor = [["+--"] * w + ['+'] for _ in range(h + 1)]

    def walk(x, y):
        s = ""
        for (a, b) in zip(hor, ver):
            s += ''.join(a + ['\n'] + b + ['\n'])

        os.system('clear')
        print s

        sleep(0.1)

        vis[y][x] = 1

        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        for (xx, yy) in d:
            if vis[yy][xx]: continue
            if xx == x: hor[max(y, yy)][x] = "+  "
            if yy == y: ver[y][max(x, xx)] = "   "
            walk(xx, yy)


    # walk(randrange(w), randrange(h))
    walk(0, 0)

    # s = ""
    # for (a, b) in zip(hor, ver):
    #     s += ''.join(a + ['\n'] + b + ['\n'])
    #
    # print s

make_maze()
