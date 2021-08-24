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


a = int(input())
mot = []
for i in range(a):
    m = input()
    mot.append(m)
print(mot)
print(count(mot))
