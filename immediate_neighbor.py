def immediate_neighbor(pattern):
    neighbor_hood = ()
    for i in range(1, len(pattern)):
        symbol = pattern[i]
        for x in 'ACGT':
            if x != symbol:
                neighbor = pattern[:i] + x + pattern[i+1:]
                neighbor_hood.add(neighbor)
    return neighbor_hood
