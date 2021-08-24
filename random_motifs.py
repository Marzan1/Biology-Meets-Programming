import random
dna = ["TTACCTTAAC", "GATGTCTGTC", "ACGGCGTTAG", "CCCTAACGAG", "CGTCAGAGGT"]
t = len(dna)
l = len(dna[0])
motif = []
for i in range(t):
    r = random.randint(1, t)
    print(r)
    motif.append(dna[i][r:r+4])
    print(motif)
