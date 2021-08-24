def number_to_pattern(index, k):
    d = {"0": "A", "1": "C", "2": "G", "3": "T"}
    if k == 1:
        return d[str(index)]
    else:
        prefixindex = index // 4
        r = str(index % 4)
        symbol = d[r]
        prefixpattern = number_to_pattern(prefixindex, k - 1)
        return prefixpattern + symbol


print(number_to_pattern(19, 4))
