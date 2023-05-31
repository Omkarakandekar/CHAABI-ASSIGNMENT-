from functools import reduce

A0 = dict(zip(('a', 'b', 'c', 'd', 'e'), (1, 2, 3, 4, 5)))
A1 = range(10)
A2 = sorted([i for i in A1 if i in A0])
A3 = sorted([A0[s] for s in A0])
A4 = [i for i in A1 if i in A3]
A5 = {i: i*i for i in A1}
A6 = [[i, i*i] for i in A1]
A7 = reduce(lambda x, y: x+y, [10, 23, -45, 33])
A8 = list(map(lambda x: x*2, [1, 2, 3, 4]))
A9 = list(filter(lambda x: len(x) > 3, ["I", "want", "to", "learn", "python"]))

print("A0 =", A0)
print("A1 =", list(A1))
print("A2 =", A2)
print("A3 =", A3)
print("A4 =", A4)
print("A5 =", A5)
print("A6 =", A6)
print("A7 =", A7)
print("A8 =", A8)
print("A9 =", A9)
