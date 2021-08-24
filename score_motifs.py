def count(motifs):
    c = {}
    k = len(motifs[0])
    for symbol in "ACGT":
        c[symbol] = []
        for j in range(k):
            c[symbol].append(0)
    t = len(motifs)
    for i in range(t):
        for j in range(k):
            symbol = motifs[i][j]
            c[symbol][j] += 1
    return c


def consensus(motifs):
    k = len(motifs[0])
    co = count(motifs)
    consensus = ""
    for j in range(k):
        m = 0
        frequent_symbol = ""
        for symbol in "ACGT":
            if co[symbol][j] > m:
                m = co[symbol][j]
                frequent_symbol = symbol
        consensus += frequent_symbol
    return consensus


def score(motifs):
    d = count(motifs)
    e = consensus(motifs)
    k = len(motifs[0])
    s = 0
    for i in range(k):
        for j in 'ACGT':
            if j != e[i]:
                s += d[j][i]
    return s


a = int(input())
mot = []
for i in range(a):
    m = input()
    mot.append(m)

print(score(mot))
print(consensus(mot))
