def pseudo_count(motifs):
    c = {}
    k = len(motifs[0])
    for symbol in "ACGT":
        c[symbol] = []
        for j in range(k):
            c[symbol].append(1)
    t = len(motifs)
    for i in range(t):
        for j in range(k):
            symbol = motifs[i][j]
            c[symbol][j] += 1
    return c


def pseudo_profile(motifs):
    k = len(motifs[0])
    t = len(motifs)
    profile = pseudo_count(motifs)
    for symbol in "ACGT":
        for j in range(k):
            profile[symbol][j] = profile[symbol][j] / (t + 4)
    return profile


def consensus(motifs):
    k = len(motifs[0])
    co = pseudo_count(motifs)
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
    d = pseudo_count(motifs)
    e = consensus(motifs)
    k = len(motifs[0])
    s = 0
    for i in range(k):
        for j in 'ACGT':
            if j != e[i]:
                s += d[j][i]
    return s


def pr(text, profile):
    k = len(text)
    pro = 1.0
    for i in range(k):
        pro *= profile[text[i]][i]
    return pro


def most_probability(text, k, profile):
    loop = len(text) - k + 1
    score = -1
    proba =''
    for i in range(loop):
        pattern = text[i:i+k]
        patty = pr(pattern, profile)
        if patty > score:
            proba = pattern
            score = patty
    return proba


def greedy_motifs_pseudocounts(dna, k, t):
    best_motifs = []
    for i in range(0, t):
        best_motifs.append(dna[i][0:k])
    n = len(dna[0])
    loop = n - k + 1
    for i in range(loop):
        motifs = []
        motifs.append(dna[0][i:i+k])
        for j in range(1, t):
            p = pseudo_profile(motifs[0:j])
            motifs.append(most_probability(dna[j], k, p))
        if score(motifs) < score(best_motifs):
            best_motifs = motifs
    return best_motifs


dna = [
"GGCGTTCAGGCA",
"AAGAATCAGTCA",
"CAAGGAGTTCGC",
"CACGTCAATCAC",
"CAATAATATTCG"
]
k = 3
t = 5
print(greedy_motifs_pseudocounts(dna, k, t))
