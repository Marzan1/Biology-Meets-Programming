def pseudo_count(motifs):
    c = {}
    k = len(motifs[0])
    for symbol in "ACGT":
        c[symbol] = []
        for j in range(k):
            c[symbol].append(1)
    t = len(motifs)
    for i in range(t):
        for j in range(k):
            symbol = motifs[i][j]
            c[symbol][j] += 1
    return c


mot = ["AACGTA", "CCCGTT", "CACCTT", "GGATTA", "TTCCGG"]

print(pseudo_count(mot))
