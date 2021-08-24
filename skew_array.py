def skew_array(genome):
    skew = [0]
    i = 0
    for x in genome:
        if x == 'C':
            skew.append(skew[i] - 1)
        elif x == 'G':
            skew.append(skew[i] + 1)
        else:
            skew.append(skew[i])
        i += 1
    return skew


print(skew_array("GAGCCACCGCGATA"))
