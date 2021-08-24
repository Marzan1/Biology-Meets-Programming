profile = {
    'A': [0.4, 0.3, 0.0, 0.1, 0.0, 0.9],
    'C': [0.2, 0.3, 0.0, 0.4, 0.0, 0.1],
    'G': [0.1, 0.3, 1.0, 0.1, 0.5, 0.0],
    'T': [0.3, 0.1, 0.0, 0.4, 0.5, 0.0]
}
pattern = 'GAGCTA'
k = len(pattern)
pro = []
for i in range(k):
    pro.append(profile[pattern[i]][i])
probability = 1.0
print(pro)
for i in pro:
    probability *= i
print(probability)
