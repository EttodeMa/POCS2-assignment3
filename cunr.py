def fact2(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact2(n-2)


def b_n(n):
    return fact2(2 * n - 5) % 1000000


with open("C:/Users/ettod/Downloads/rosalind_cunr.txt", "r") as x:
    leaves = int(x.readline().strip())

res = b_n(leaves)
print(res)
