import random


def GibbsSampler(Dna, k, t, N):
    Motifs = RandomMotifs(Dna, k, t)
    BestMotifs = Motifs.copy()
    for j in range(1, N):
        i = random.randint(0, t - 1)
        Profile_Motifs = []
        for f in range(0, t):
            if f != i:
                Profile_Motifs.append(Motifs[f])
        Profile = ProfileWithPseudocounts(Profile_Motifs)
        Mot = ProfileGeneratedString(Dna[i], Profile, k)
        Motifs = Profile_Motifs.copy()
        Motifs.insert(i, Mot)
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
    return BestMotifs


def ProfileGeneratedString(Text, profile, k):
    n = len(Text)
    probabilities = {}
    for i in range(0, n-k+1):
        probabilities[Text[i:i+k]] = Pr(Text[i:i+k], profile)
    probabilities = Normalize(probabilities)
    return WeightedDie(probabilities)


def Pr(Text, Profile):
    k = len(Text)
    pro = []
    p = 1.0
    for i in range(k):
        pro.append(Profile[Text[i]][i])
    for i in pro:
        p *= i
    return p


def Normalize(Probabilities):
    n = {}
    s = 0
    for k in Probabilities:
        s += Probabilities[k]
    for i in Probabilities:
        n[i] = 0
        for j in n:
            if i == j:
                n[j] = Probabilities[i] / s
    return n


def WeightedDie(Probabilities):
    p = random.uniform(0, 1)
    c = 0
    for i in Probabilities:
        c += Probabilities[i]
        if p < c:
            kmer = i
            return kmer


def RandomMotifs(Dna, k, t):
    motifs = []
    for i in range(t):
        r = random.randint(0, t-1)
        motifs.append(Dna[i][r:r+k])
    return motifs


def ProfileWithPseudocounts(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile = Pseudocounts(Motifs)
    for symbol in "ACGT":
        for j in range(k):
            profile[symbol][j] = profile[symbol][j] / (t + 4)
    return profile


def Pseudocounts(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    count = {}
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
             count[symbol].append(1)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count


def Score(Motifs):
    d = Pseudocounts(Motifs)
    e = Consensus(Motifs)
    k = len(Motifs[0])
    score = 0
    for i in range(k):
        for j in 'ACGT':
            if j != e[i]:
                score += d[j][i]
    return score


def Consensus(Motifs):
    k = len(Motifs[0])
    count = Pseudocounts(Motifs)
    consensus = ""
    for j in range(k):
        m = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if  count[symbol][j] > m:
                m = count[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
    return consensus


if __name__ == "__main__":
    k, t, N = [int(a) for a in input().strip().split(" ")]
    Dna = []
    for _ in range(t):
        Dna.append(input())
    best_motifs = GibbsSampler(Dna, k, t, N)
    for _ in range(200):
        new = GibbsSampler(Dna, k, t, N)
        if Score(new) < Score(best_motifs):
            best_motifs = new[:]
    print(*best_motifs, sep='\n')

"""sample input
dna = ['CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA',
'GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG',
'TAGTACCGAGACCGAAAGAAGTATACAGGCGT',
'TAGATCAAGTTTCAGGTGCACGTCGGTGAACC',
'AATCCACCAGCTCCACGTGCAATGTTGGCCTA']
k = 8
t = 5
N = 100"""
