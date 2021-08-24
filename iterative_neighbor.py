def immediate_neighbor(pattern):
    neighbour_hood = []
    for i in range(len(pattern)):
        symbol = pattern[i]
        for x in 'ACGT':
            if x != symbol:
                neighbour = pattern[:i] + x + pattern[i+1:]
                neighbour_hood.append(neighbour)
    return neighbour_hood


def iterative_neighbor(pattern, d):
    neighbor_hood = [pattern]
    for j in range(d):
        for x in neighbor_hood:
            neighbor_hood = neighbor_hood + immediate_neighbor(x)
            neighbor_hood = list(set(neighbor_hood))
    return neighbor_hood


print(iterative_neighbor('ACG', 1))
