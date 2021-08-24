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


dna = {
    'A': [0.4, 0.3, 0.0, 0.1, 0.0, 0.9],
    'C': [0.2, 0.3, 0.0, 0.4, 0.0, 0.1],
    'G': [0.1, 0.3, 1.0, 0.1, 0.5, 0.0],
    'T': [0.3, 0.1, 0.0, 0.4, 0.5, 0.0]
}
print(consensus(dna))
