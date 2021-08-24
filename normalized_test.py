probabilities = {'AC': 0.1, 'GT': 0.1, 'AG': 0.1, 'TC': 0.1}
n = {}
s = 0
for k in probabilities:
    s += probabilities[k]
for i in probabilities:
    n[i] = 0
    print('i=', i)
    for j in n:
        print('j=', j)
        if i == j:
            n[j] = probabilities[i] / s
            print('n=', n)
print(n)
