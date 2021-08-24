def neighbors(pattern, d):
    if d == 0:
        return pattern
    if len(pattern) == 1:
        return {'A', 'C', 'G', 'T'}
    neighbor_hood = []
    first = pattern[1:]
    suffix_neighbors = neighbors(first, d)
    for s in suffix_neighbors:
        if hamming_distance(first, s) < d:
            for x in 'ACGT':
                n = x + s
                neighbor_hood.append(n)
        else:
                n = pattern[0] + s
                neighbor_hood.append(n)
    return neighbor_hood


def hamming_distance(p, q):
    count = 0
    for i in range(0, len(p)):
        if p[i] != q[i]:
            count += 1
    return count


print(neighbors('ATGT', 1))
