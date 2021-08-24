import random


def weighted_die(probabilities):
    kmer = ''
    p = random.uniform(0, 1)
    c = 0
    for i in probabilities:
        c += probabilities[i]
        if p <= c:
            kmer = i
            return kmer


dic = {'AC': 0.1, 'GC': 0.2, 'TA': 0.4, 'CA': 0.1, 'GT': 0.2}
print(weighted_die(dic))
