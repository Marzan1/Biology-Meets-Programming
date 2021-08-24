def reverse(pattern):
    rev = ''
    for char in pattern:
        rev = char + rev
    return rev


def complement(pattern):
    d = {'A': "T", 'T': 'A', 'G': 'C', 'C': 'G'}
    com = ''
    for char in pattern:
        com += d.get(char)
    return com


def reverse_complement(pattern):
    a = reverse(pattern)
    b = complement(a)
    return b


pattern = 'AAAACCCGGT'
print(reverse_complement(pattern))
