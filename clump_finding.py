def frequency_map(text, k):
    freq = {}
    n = len(text)
    for i in range(n-k+1):
        pattern = text[i:i+k]
        freq[pattern] = 0
        for j in range(n-k+1):
            if pattern == text[j:j+k]:
                freq[pattern] = freq[pattern] + 1
    return freq


def clump_finding(genome, k, l, t):
    clumps = []
    rng = len(genome) - k + 1
    for i in range(rng):
        text = genome[i:i+l]
        freqmap = frequency_map(text, k)
        for key in freqmap:
            if freqmap[key] >= t:
                if key not in clumps:
                    clumps.append(key)
    return clumps


print(clump_finding("CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA", 5, 50, 4))
