def skew_array(genome):
    d = {'A': 0, 'T': 0, 'C': -1, 'G': 1}
    skew = [0]
    for i in range(len(genome)):
        skew.append(d[genome[i]] + skew[i])
    return skew


def minimum_skew(genome):
    skew = skew_array(genome)
    positions = []
    for i in range(len(genome)):
        if skew[i] == min(skew):
            positions.append(i)
    return positions
