def pattern_count(pattern, text):
    count = 0
    for i in range(len(text)-len(pattern)+1):
        if text[i:i+len(pattern)] == pattern:
            count = count+1
    return count


def faster_symbol_array(genome, symbol):
    array = {}
    n = len(genome)
    extended_genome = genome + genome[0:n//2]
    array[0] = pattern_count(symbol, genome[0:n//2])
    for i in range(1, n):
        array[i] = array[i-1]
        if extended_genome[i-1] == symbol:
            array[i] = array[i] - 1
        if extended_genome[(n//2) + i - 1] == symbol:
            array[i] = array[i] + 1
    return array


genome = "AAAAGGGG"
symbol = "A"
print(faster_symbol_array(genome, symbol))

