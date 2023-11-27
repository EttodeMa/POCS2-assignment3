from Bio import SeqIO
def failure_array(s):
    n = len(s)
    p = [0] * n

    j = 0
    for i in range(2, n + 1):
        while j > 0 and s[j] != s[i - 1]:
            j = p[j - 1]
        if s[j] == s[i - 1]:
            j += 1
        p[i - 1] = j

    return p


file = "C:/Users/ettod/Downloads/rosalind_kmp.txt"
bio_seq = list(SeqIO.parse(file, "fasta"))
for ID in bio_seq:
    seq = str(ID.seq)
result = failure_array(seq)
print(*result)
