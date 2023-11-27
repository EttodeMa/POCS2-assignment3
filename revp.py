from Bio import SeqIO as SI
from Bio import Seq as S

def palindromes(seq):
    results = []

    for x in range(len(seq)):
        for y in range(4, 13):
            z = x + y
            if z <= len(seq):
                pal_seq = seq[x:z]
                if pal_seq == S.reverse_complement(pal_seq):
                    results.append((x + 1, y))

    return results


f = "C:/Users/ettod/Downloads/rosalind_revp.txt"
fasta = list(SI.parse(f, "fasta"))
for ID in fasta:
    seq = str(ID.seq)
t = palindromes(seq)

for g in t:
    print(*g)
