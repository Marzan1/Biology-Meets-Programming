def symbol_array(genome, symbol):
    array = {}
    n = len(genome)
    extended_genome = genome + genome[0:n//2]
    for i in range(n):
        array[i] = pattern_count(extended_genome[i:i+(n//2)], symbol)
    return array


def pattern_count(text, pattern):
    count = 0
    for i in range(len(text)-len(pattern)+1):
        if text[i:i+len(pattern)] == pattern:
            count = count+1
    return count


genome = "CTGCTTCGCCCGCCGG"
symbol = "C"
print(symbol_array(genome, symbol))
