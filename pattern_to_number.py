def pattern_to_number(pattern):
    if len(pattern) == 0:
        return 0
    symbol = pattern[len(pattern) - 1]
    prefix = pattern[:-1]
    d = {"A": "0", "C": "1", "G": "2", "T": "3"}
    a = int(d[symbol])
    result = 4 * pattern_to_number(prefix) + a
    return result


print(pattern_to_number('ACAT'))
