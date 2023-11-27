import itertools as itt
import math as mh


def permutations(k):
    res = []
    l = []
    for ele in range(1, int(k) + 1):
        l.append(ele)
    perm = itt.permutations(l)
    perm_list = list(perm)
    for x in perm_list:
        res.append(x)
    return res


with open("C:/Users/ettod/Downloads/rosalind_perm.txt") as x:
    k = x.read()
print(mh.factorial(int(k)))
s = permutations(k)
for b in s:
    print(" ".join(map(str, b)))
