def frequency_map(text, k):
    freq = {}
    n = len(text)
    for i in range(n - k + 1):
        pattern = text[i:i+k]
        freq[pattern] = 0
        for i in range(n - k + 1):
            if text[i:i+k] == pattern:
                freq[pattern] += 1

    return freq


k = int(input())
dna = input()
print(frequency_map(dna, k))
