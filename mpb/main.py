import matplotlib.pyplot as plt
import math

tXfailureRate = list(map(lambda i: i / 100, range(0, 200)))

k = 2


def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

# t: tXfailureRate


def series(t):
    return math.exp(-1 * 3 * t)


def parallel(t):
    init = 1
    for _ in range(1, 4):
        init = init * (1 - math.exp(-1 * t))
    return 1 - init


def koutofn(t):
    init = 0
    for i in range(k, 4):
        init = init + comb(3, i) * math.pow(math.exp(-1 * t),
                                            i) * math.pow(1 - math.exp(-1 * t), 3 - i)
    return init


def standby_redundancy(t):
    init = 0
    for i in range(0, 4):
        init = init + math.pow(t, i) / \
            math.factorial(i) * math.exp(-1 * t)
    return init


plt.title("3")

plt.xlabel("time")
plt.ylabel("system reliability")

plt.plot(tXfailureRate, list(map(series, tXfailureRate)), label="series")
plt.plot(tXfailureRate, list(map(parallel, tXfailureRate)), label="parallel")
plt.plot(tXfailureRate, list(map(koutofn, tXfailureRate)), label="k out of n")
plt.plot(tXfailureRate, list(map(standby_redundancy, tXfailureRate)),
         label="standby redundancy")

plt.legend()

plt.show()
