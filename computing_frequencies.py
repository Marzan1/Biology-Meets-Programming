def computing_frequencies(text, k):
    loop = (4 ** k)
    loop_1 = len(text) - k + 1
    frequency_array = []
    for i in range(loop):
        frequency_array.append(0)
    for i in range(loop_1):
            pattern = text[i:i+k]
            j = pattern_to_number(pattern)
            frequency_array[j] += 1
    return ' '.join(map(str, frequency_array))


def pattern_to_number(pattern):
    if len(pattern) == 0:
        return 0
    symbol = pattern[len(pattern) - 1]
    prefix = pattern[:-1]
    d = {"A": "0", "C": "1", "G": "2", "T": "3"}
    a = int(d[symbol])
    result = 4 * pattern_to_number(prefix) + a
    return result
