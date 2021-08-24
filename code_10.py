def hamming_distance(p, q):
    count = 0
    for i in range(0, len(p)):
        if p[i] != q[i]:
            count += 1
    return count


def approximate_pattern_matching(pat, text, di):
    k = len(pat)
    loop = len(text) - k + 1
    count = 0
    for i in range(loop):
        lst = text[i:i+k]
        s = hamming_distance(pat, lst)
        if s <= di:
            count += 1
    return count


pattern = 'GAGG'
genome = 'TTTAGAGCCTTCAGAGG'
d = 2
print(approximate_pattern_matching(pattern, genome, d))
