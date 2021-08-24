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


text = "TCGCGCCGGGTCATAACTGTTGCGGACCAGTGCAGATGTGTCACACGCAGTGATCTTATAAGCACTCAATTCGATGAGGGAAGGTACCGAGATAACGCTCTTATCCGTGAGGTTTCCTTCTCAGACTTACCCGCATCGAAATTAACTGCCCGGTTGAGGAAACGCCGTGCAGGGAACGAGATAGGTGGAGAGCAAGGGGACCCCGTACAAAACTTTGTCCCGTGTGTAACCAAGTACAATATAGATGCTCGCTTATCCCCTGACAGGGCTAGAAAGCTTGGCAGTACCACGCAACGCTTCGCCGGGCGTGACTAGCGACTCCCCAAATTCCTTGTAATCGGA"
pattern = "TGTAA"
d = 2
print(approximate_pattern_count(text, pattern, d))
