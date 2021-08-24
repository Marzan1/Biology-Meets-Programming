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


def profile(motifs):
    profile = count(motifs)
    k = len(motifs[0])
    t = len(motifs)
    for symbol in "ACGT":
        for j in range(k):
            profile[symbol][j] = profile[symbol][j] / t
    return profile


a = int(input())
motifs = []
for i in range(a):
    m = input()
    motifs.append(m)
print(profile(motifs))
