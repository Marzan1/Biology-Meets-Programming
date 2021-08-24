def pr(text, profile):
    k = len(text)
    pro = 1.0
    for i in range(k):
        pro *= profile[text[i]][i]
    return pro


pattern = 'AAGTTC'
matrix = {
    'A': [0.4, 0.3, 0.0, 0.1, 0.0, 0.9],
    'C': [0.2, 0.3, 0.0, 0.4, 0.0, 0.1],
    'G': [0.1, 0.3, 1.0, 0.1, 0.5, 0.0],
    'T': [0.3, 0.1, 0.0, 0.4, 0.5, 0.0]
}
print(pr(pattern, matrix))
