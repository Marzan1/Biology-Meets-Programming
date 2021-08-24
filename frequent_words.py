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


def frequent_words(text, k):
    words = []
    freq = frequency_map(text, k)
    m = max(freq.values())
    for key in freq:
        if freq[key] == m:
            w = key
            words.append(w)
    return words


dna = input()
k = int(input())
print(frequent_words(dna, k))
