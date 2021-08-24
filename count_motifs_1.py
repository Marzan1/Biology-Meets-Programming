a = int(input())
motifs = []
for i in range(a):
    m = input()
    motifs.append(m)
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
print(c)
p = {}
for symbol in "ACGT":
    p[symbol] = []
    for j in range(k):
        p[symbol].append(0)
for i in range(t):
    for j in range(k):
        symbol = motifs[i][j]
        p[symbol][j] = c["A"][j] / t
print(p)
