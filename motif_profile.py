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


def motifs(profile, dns):
    for key in profile:
        for i in profile[key]:
            m = max(profile[key])
