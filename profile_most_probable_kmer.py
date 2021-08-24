def pr(text, profile):
    k = len(text)
    pro = 1.0
    for i in range(k):
        pro *= profile[text[i]][i]
    return pro


def profile_most_probable_kmer(text, k, profile):
    loop = len(text) - k + 1
    score = -1
    proba = ''
    for i in range(loop):
        pattern = text[i:i+k]
        patty = pr(pattern, profile)
        if patty > score:
            proba = pattern
            score = patty
    return proba


profil = {'A': [0.125, 0.125, 0.25], 'C': [0.5, 0.375, 0.125], 'G': [0.125, 0.125, 0.25], 'T': [0.25, 0.375, 0.375]}
kmer = []
for i in range(4):
    pat = input()
    kmer.append(profile_most_probable_kmer(pat, 3, profil))
for m in kmer:
    print(m)

