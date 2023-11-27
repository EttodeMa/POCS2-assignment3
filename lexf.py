import itertools as it
with open("C:/Users/ettod/Downloads/rosalind_lexf.txt", "r") as d:
    all = d.readlines()
alphab = all[0].split()
m = int(all[1])
q = it.product(alphab, repeat=m)
res = ["".join(c) for c in q]
for g in res:
    print("".join(g))
