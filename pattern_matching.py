def pattern_matching(pattern, genome):
    positions = []
    k = len(pattern)
    loop = len(genome) - k + 1
    for i in range(0, loop):
        if genome[i:i+k] == pattern:
            positions.append(i)
    return positions


pattern = input()
genome = input()
print(pattern_matching(pattern, genome))
