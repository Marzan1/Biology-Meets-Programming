def pr(text, profile):
    k = len(text)
    pro = 1.0
    for i in range(k):
        pro *= profile[text[i]][i]
    return pro


def most_probability(text, k, profile):
    loop = len(text) - k + 1
    score = -1
    for i in range(loop):
        pattern = text[i:i+k]
        patty = pr(pattern, profile)
        if patty > score:
            proba = pattern
            score = patty
    return proba


profil = {'A': [0.25, 0.0, 0.25], 'C': [0.25, 0.5, 0.5], 'G': [0.5, 0.0, 0.0], 'T': [0.0, 0.5, 0.25]}
dna = ["ATGAGGTC", "GCCCTAGA", "AAATAGAT", "TTGTGCTA"]
k = len(dna)
for i in range(k):
    a = most_probability(dna[i], 3, profil)
    print(a)
