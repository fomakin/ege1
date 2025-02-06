# 2 задание
from itertools import *


def f(x, y, w, z):
    return (x == (not y)) <= ((x and w) == z)


for a1, a2, a3, a4, a5 in product([0, 1], repeat=5):
    table = [(1, 1, a1, a2), (1, 1, a3, 1), (a4, 1, 1, a5)]
    if len(table) == len(set(table)):
        for p in permutations('xywz'):
            if [f(**dict(zip(p, r))) for r in table] == [0, 0, 0]:
                print(p)
############################
# 15(отрезки)
from itertools import *


def f(x):
    b = 10 <= x <= 15
    c = 18 <= x <= 40
    a = a1 <= x <= a2
    return  # логическое выражение


ox = [i / 4 for i in range(10 * 4, 40 * 4 + 1)]
m = []
for a1, a2 in combinations(ox, 2):
    if all(f(x) for x in ox):
        m.append(a2 - a1)
print(min(m))


# 15(обычное)
def f(x, y):
    return ((x - 3 * y) < a) or (y > 400) or (x > 56)


for a in range(0, 1000):
    if all(f(x, y) for x in range(1, 1000) for y in range(1, 1000)):
        print(a)
        break
############################
# 16 задание
from sys import *

setrecursionlimit(10000)


def f(n):
    if n <= 2:
        return 1
    if n > 2:
        return n * f(n - 2)


print(f(5000) / f(4994))
#############################
# 17 задание
a = [int(x) for x in open('17-243.txt')]

S = sum([int(i) for x in a if x % 49 == 0 for i in str(x)])
ans = []
for i in range(len(a) - 1):
    if (a[i] > S and (not a[i + 1] > S) and a[i + 1] % 10 == 7) or \
            (a[i + 1] > S and (not a[i] > S) and a[i] % 10 == 7):
        ans.append(a[i] + a[i + 1])
print(len(ans), min(ans))


############################
# 19-21 задание
def f(a, b, m):
    if a + b >= 231:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(a + 2, b, m - 1), f(a * 2, b, m - 1), f(a, b + 2, m - 1), f(a, b * 2, m - 1)]
    return any(h) if (m - 1) % 2 == 0 else all(h)


print('19)', [s for s in range(1, 214) if f(17, s, 2)])  # all->any
print('20)', [s for s in range(1, 214) if not f(17, s, 1) and f(17, s, 3)])
print('21)', [s for s in range(1, 214) if not f(17, s, 2) and f(17, s, 4)])
############################
# 23 задание
from functools import *


@lru_cache(None)
def f(c, e):
    if c > e:
        return 0
    if c == e:
        return 1
    if c < e:
        return f(c + 1, e) + f(2 * c, e) + f(2 * c + 1, e)


print(f(4, 218))


#############################
# 25(делители)
def f(x):
    d = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return sorted(d)


for x in range(244143, 367821 + 1):
    d = f(x)
    # эта часть кода меняется    if int(x**0.5)**2 == x:
    if len(d) == 5:
        print(d[3], d[4])

# 25(маски)
from fnmatch import *

# range меняется в зависимости от условия#шаг это делимость
for i in range(0, 10 ** 10, 1):
    if fnmatch(str(i), '12673788?*'):
        print(i)
#############################
# 27 задание
f = open('7584a.txt')
f.readline()
# если первая строчка x,y
data = [list(map(float, x.replace(',', '.').split())) for x in a]
print(len(data))


def dist(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def getCluster(p0):
    cluster = [p for p in data if dist(p0, p) < 1]
    if len(cluster) > 0:
        for p in cluster: 
            data.remove(p)
        next_cluster = [getCluster(p) for p in cluster]
        cluster = cluster + sum(next_cluster, [])
    return cluster


clusters = []
while len(data) > 0:
    p0 = data.pop()
    cluster = [p0] + getCluster(p0)
    print(len(cluster))
    clusters.append(cluster)

clusters = [kl for kl in clusters if len(kl) > 10]

K = len(clusters)


def center(kl):
    m = []
    for p in kl:
        sm = sum(dist(p, p1) * p1[2] for p1 in kl)
        m.append([sm, p])
    return min(m)[1]


centroid = [center(kl) for kl in clusters]
print(centroid)

px = sum(x for x, y in centroid) / K
py = sum(y for x, y in centroid) / K
print(int(px * 100000), int(py * 100000))
########################################################
# еще несколько вариантов

# 2
from itertools import *


def f(x, y, w, z):
    return  # в зависимости от условия


for a1, a2, a3, a4 in product([0, 1], repeat=4):
    # в зависимости от условия
    t = [(1, 1, 1, a1), (1, 1, 1, a2), (1, a3, a4, 1)]
    if len(t) == len(set(t)):
        for p in permutations('xywz'):
            if [f(**dict(zip(p, r))) for r in t] == [1, 1, 1]:
                print(*p, sep='')


# 19-21
def f(a, b, m):
    if a + b >= 231: 
        return m % 2 == 0
    if m == 0: 
        return 0
    h = [f(a + 2, b, m - 1), f(a * 2, b, m - 1), f(a, b + 2, m - 1), f(a, b * 2, m - 1)]
    return any(h) if (m - 1) % 2 == 0 else all(h)


print('19)', [s for s in range(1, 214) if
              f(17, s, 2)])  # all->anyprint('20)',[s for s in range(1,214) if not f(17,s,1) and f(17,s,3)])
print('21)', [s for s in range(1, 214) if not f(17, s, 2) and f(17, s, 4)])
