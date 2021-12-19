import matplotlib.pyplot as plt
from matplotlib import colors
import matplotlib.cm as cm
import numpy as np
import sys
import time
import os
import glob

s1 = ''
s2 = ''
match = 0
mismatch = 0
gap = 0

def get_alignment():
    if len(s1) <= 1 or len(s2) <= 1:
        return
    res = [None] * (len(s2) + 1)
    res[0] = 0
    res[-1] = len(s1)
    cur = [(0, 0, len(s1), len(s2))]
    n = 0
    while cur:
        next_round = []
        for i in cur:
            if i[3] - i[1] <= 1:
                continue
            r1, r2, r3 = Hirschberg(*i)
            res[r1[0]] = r1[1]
            next_round.append(r2)
            next_round.append(r3)
        cur = next_round
        if cur:
            n += 1
            draw(res, n)

    z = np.ones((len(s1) + 1, len(s2) + 1))
    t1, t2 = '-' + s1, '-' + s2
    for i in range(len(res) - 1):
        if res[i] == res[i + 1]:
            z[res[i], i] = 0
            z[res[i + 1], i + 1] = 0
            continue
        r = final_round(t1[res[i]: res[i + 1] + 1], t2[i: i + 2])
        z[res[i]: res[i + 1] + 1, i: i + 2] = r
    draw(z, n + 1, True)

def final_round(a, b):
    m = np.zeros((len(a), 2))
    for i in range(1, len(m)):
        m[i, 0] = m[i - 1, 0] + gap
    m[0, 1] = gap
    for i in range(1, len(m)):
        m[i, 1] = max(m[i, 0] + gap, m[i - 1, 1] + gap, m[i - 1, 0] + (match if a[i] == b[1] else mismatch))
    r = np.ones((len(a), 2))
    i, j = len(r) - 1, 1
    while i != 0 or j != 0:
        r[i, j] = 0
        if i * j > 0 and m[i - 1, j - 1] + (match if a[i] == b[j] else mismatch) == m[i, j]:
            i -= 1
            j -= 1
        elif i > 0 and m[i - 1, j] + gap == m[i, j]:
            i -= 1
        else:
            j -= 1
    r[0, 0] = 0
    return r


def Hirschberg(i, j, i1, j1):
    if j1 - j <= 1:
        return
    
    mid = (j + j1) // 2
    l = list(range(0, i1 - i + 1))
    for x in range(len(l)):
        l[x] *= gap
    for y in range(j + 1, mid + 1):
        next_l = []
        for x in range(i, i1 + 1):
            score = float('-inf')
            if x > i:
                score = max(score, next_l[-1] + gap)
                score = max(score, l[x - i - 1] + (match if s1[x - 1] == s2[y - 1] else mismatch))
            score = max(score, l[x - i] + gap)
            next_l.append(score)
        l = next_l
    # print(l)

    l1 = list(range(0, i1 - i + 1))[::-1]
    for x in range(len(l1)):
        l1[x] *= gap
    for y in range(j1 - 1, mid - 1, -1):
        next_l = [float('-inf')] * len(l1)
        for x in range(i1, i - 1, -1):
            score = float('-inf')
            if x < i1:
                score = max(score, next_l[x - i + 1] + gap)
                score = max(score, l1[x - i + 1] + (match if s1[x] == s2[y] else mismatch))
            score = max(score, l1[x - i] + gap)
            next_l[x - i] = score
        l1 = next_l
    # print(l1)

    i_star = 0
    tmp = float('-inf')
    for x in range(len(l)):
        if l[x] + l1[x] > tmp:
            tmp = l[x] + l1[x]
            i_star = i + x

    return (mid, i_star), (i, j, i_star, mid), (i_star, mid, i1, j1)


def draw(ref, n, flag=False):
    if flag:
        z = ref
    else:
        z = np.ones((len(s1) + 1, len(s2) + 1))
        l = []
        for i in range(len(ref)):
            if ref[i] is not None:
                l.append((ref[i], i))
        for i in range(len(l) - 1):
            if l[i + 1][0] - l[i][0] <= 1 and l[i + 1][1] - l[i][1] <= 1:
                continue
            for a in range(l[i][0], l[i + 1][0] + 1):
                for b in range(l[i][1], l[i + 1][1] + 1):
                    z[a, b] = 0.5
        for i in range(len(ref)):
            if ref[i] is not None:
                z[ref[i], i] = 0

    z = z[::-1]
    x = np.arange(-0.5, z.shape[1], 1)
    y = np.arange(-0.5, z.shape[0], 1)

    fig, ax = plt.subplots()
    if len(s1) <= 20 and len(s2) <= 20:
        ax.pcolormesh(x, y, z, cmap=cm.gray, edgecolors='black')
    else:
        ax.pcolormesh(x, y, z, cmap=cm.gray)
    ax.set_aspect(1)

    if len(s1) <= 20 and len(s2) <= 20:
        ax.set_xticklabels(list('-' + s2))
        ax.set_xticks(np.arange(len(x) - 1))
        ax.set_yticklabels(list('-' + s1)[::-1])
        ax.set_yticks(np.arange(len(y) - 1))
        ax.xaxis.set_tick_params(labeltop=True)
        ax.xaxis.set_tick_params(labelbottom=False)
    else:
        ax.axes.xaxis.set_visible(False)
        ax.axes.yaxis.set_visible(False)

    # plt.show()
    plt.savefig('my-app/src/assets/{}.png'.format(n))


if __name__ == "__main__":
    print(sys.argv[1:])

    files = glob.glob('my-app/src/assets/*')
    print(files)
    for f in files:
        print(f)
        os.remove(f)

    s1, s2, match, mismatch, gap = sys.argv[1:]
    match = int(match)
    mismatch = int(mismatch)
    gap = int(gap)
    get_alignment()