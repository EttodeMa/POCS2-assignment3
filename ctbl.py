from Bio import Phylo


def char_table(t, g):
    for subt in t.clades:
        if not subt.is_terminal():
            binarystr(subt, g)
            char_table(subt, g)


def binarystr(t, g):
    res = ""
    term = set(g.get_terminals())
    subterm = set(t.get_terminals())
    no_subterm = term - subterm

    on = []
    off = []

    for i in subterm:
        on.append(i.name)
    for j in no_subterm:
        off.append(j.name)

    for p in y:
        if p in on:
            res += "1"
        elif p in off:
            res += "0"
    print(res)


with open("C:/Users/ettod/Downloads/rosalind_ctbl.txt") as x:
    s = Phylo.read(x, "newick")
    y = []
    for t in s.find_clades():
        if t.name:
            y.append(t.name)

    y = sorted(y)
g = s.root
char_table(g, g)
