def hamming_distance(p, q):
    count = 0
    for i in range(0, len(p)):
        if p[i] != q[i]:
            count += 1
    return count


def approximate_pattern_count(text, pat, di):
    k = len(pat)
    loop = len(text) - k + 1
    count = 0
    for i in range(loop):
        lst = text[i:i+k]
        s = hamming_distance(pat, lst)
        if s <= di:
            count += 1
    return count


Text = "TATCTCGGGGTCACAATCGGTCGGTAGCTCGGTATCTCGGTAGCTCGGGGTCTCGGGGTCTATCTAGCTCGGTATCACAATCGGTCGGACAATAGCTCGGTAGCTCGGTCGGGGTCTAGCACAATCGGTAGCTAGCACAAACAAGGTCGGTCTAGCTATCTATCTCGGTATCTCGGTCGGACAATCGGTATCGGTCACAATCGGTAGCTCGGACAATCGGACAAGGTCTCGGTATCGGTCTCGGTATCTAGCACAAGGTCGGTCACAAGGTCACAAGGTCGGTCTCGGGGTCTAGCACAATCGGTCGGGGTCTATCTATCACAAGGTCTATC"
k = 7
d = 3
loop = len(Text) - k + 1
loop_1 = 4 ** k
ta = []
t = []
for i in range(loop):
    pattern = Text[i:i+k]
    pat = 0
    for j in range(loop_1):
        pat = approximate_pattern_count(Text, pattern, d)
    ta.append(pat)
fr = max(ta)
for i in range(loop):
    pattern = Text[i:i+k]
    for j in range(loop_1):
        pat = approximate_pattern_count(Text, pattern, d)
        if pat == fr:
            t.append(pattern)
print(set(t))
