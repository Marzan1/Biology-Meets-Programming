import random
k = 8
t = 5
dna = ["CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA", "GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG", "TAGTACCGAGACCGAAAGAAGTATACAGGCGT", "TAGATCAAGTTTCAGGTGCACGTCGGTGAACC", "AATCCACCAGCTCCACGTGCAATGTTGGCCTA"]


def randomized_motif_search(dna, k, t):
    m = random_motifs(dna, k, t)
    best_motifs = m
    i = 0
    while i < 1000:
        i += 1
        profile = profile_with_pseudocounts(m)
        m = motifs(profile, dna, k)
        if score(m) < score(best_motifs):
            best_motifs = m[:]
        else:
            return best_motifs


def random_motifs(dna, k, t):
    motifs = []
    for i in range(t):
        r = random.randint(1, t)
        motifs.append(dna[i][r:r+k])
    return motifs


def profile_most_probable_kmer(text, k, profile):
    loop = len(text) - k + 1
    most = []
    for i in range(loop):
        pattern = text[i:i+k]
        most.append(pr(pattern, profile))
    maximum = max(most)
    for i in range(loop):
        pattern = text[i:i+k]
        if pr(pattern, profile) == maximum:
            return pattern


def pr(text, profile):
    k = len(text)
    pro = []
    p = 1.0
    for i in range(k):
        pro.append(profile[text[i]][i])
    for i in pro:
        p *= i
    return p


def motifs(profile, dna, k):
    loop = len(dna)
    motifs = []
    for i in range(loop):
        motifs.append(profile_most_probable_kmer(dna[i], k, profile))
    return motifs


def consensus(motifs):
    k = len(motifs[0])
    count = pseudocounts(motifs)
    consensus = ""
    for j in range(k):
        m = 0
        frequent_symbol = ""
        for symbol in "ACGT":
            if count[symbol][j] > m:
                m = count[symbol][j]
                frequent_symbol = symbol
        consensus += frequent_symbol
    return consensus


def score(motifs):
    d = pseudocounts(motifs)
    e = consensus(motifs)
    k = len(motifs[0])
    score = 0
    for i in range(k):
        for j in 'ACGT':
            if j != e[i]:
                score += d[j][i]
    return score


def pseudocounts(motifs):
    t = len(motifs)
    k = len(motifs[0])
    count = {}
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
             count[symbol].append(1)
    for i in range(t):
        for j in range(k):
            symbol = motifs[i][j]
            count[symbol][j] += 1
    return count


def profile_with_pseudocounts(motifs):
    t = len(motifs)
    k = len(motifs[0])
    profile = pseudocounts(motifs)
    for symbol in "ACGT":
        for j in range(k):
            profile[symbol][j] = profile[symbol][j] / (t + 4)
    return profile


N = 250
BestMotifs = randomized_motif_search(dna, k, t)
for i in range(N):
    m = randomized_motif_search(dna, k, t)
    if score(m) < score(BestMotifs):
        BestMotifs = m


for i in BestMotifs:
    print(i)
