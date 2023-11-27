def counting_subsets(n):

    r = pow(2, int(n), 1000000)
    return r


with open("C:/Users/ettod/Downloads/rosalind_sset.txt", "r") as c:
    n = c.read().strip()

ddf = counting_subsets(n)
print(ddf)
