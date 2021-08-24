def hamming_distance(p, q):
    count = 0
    for i in range(0, len(p)):
        if p[i] != q[i]:
            count += 1
    return count


def approximate_pattern_matching(text, pat, di):
    k = len(pat)
    loop = len(text) - k + 1
    positions = []
    for i in range(loop):
        lst = text[i:i+k]
        s = hamming_distance(pat, lst)
        if s <= di:
            positions.append(i)
    return positions


pattern = 'TATGGATTC'
genome = 'TCGTGTGACCCGCAATGCTTGTTTATGGAGAGGTGTCTTTGCACCCGTGGCCACGTTGTACACGCTCGAATTATCGCGCCGGCGACAATGTCATGGTCTACCTAATCGAGCAGAACCCTCAGAAGCAAGACGAAATCGTTAATGTTCTCGGGGAGATCGGGGAGATCGCCCGATCGGATCGAATATGCTAAAAGCCAACTCGGCGGTATTGATGAAAAACTAGATAAGTCGCTTTAAAATATAGAACACAGCAGGCTTGTTGCACACGGTACGTTTGCACAAAGGGACAGCGTAGCGTGCTCTACTCGGCGACTGCTATACTGCTCGCCTTTTTCACCCGCCTGTGTAATAGCAACTCTCACTCTCTCGGGAACTGTTTGCCTCACGTAAGTTTCCCTAAGACTTTCTTAACCATAAGACCAGTGGACCTAACGGGACCACGACGTTACCTGCGTTATCATAGATACAACTAAGGTGGACTTTGTGCTAGAAGCTCGTAAACTAGCAGAAATCTAATTGCCGCAGACGCGGGACCGTCGGTTGTAACCATTCAATTACATCCCCCAGCGTCCGAGGACTGGGCATACACGAGTTTCAGCCAGTTCTCAGATAAGAGCCAAAGCAGCGGCGGATGAGATGCTGCCTAGCGCATGTGGGGTGACCCTGTCCCTATGTCGTATTTATTACTGGTACAATTAGGTCGGCGTTATTGATTACCGCGGAAAGAACGGGGCTTTCCCTATAGGCTTACGTCTAGTCCTGCGTACGAAAAACTACGATCTCACATCATATTCAATCAGACAGCGGTCTTAGGCTTCCCCCGGCGTCAAGAAGTCGGGAAAAATTCGGAAAGACGGAACAACTCTATCCAGAGGAAGTTGTTCTGCTCGGCGCGTTTTAAAACTCCCCTTAATTTCGGACCACTTTACGGTGATTGTGGGCTGGGTAACATAATCCCTGCTCACTTGCACCCCCCAAAAAACGGCGTATACTTTTGGTACCTGTCGAGACATTCCATGTTCCGGTCCCGTGCCGGTTAACCCCAGGAACCGTGCAGACAGCCATCCTACAAGGAGTCTACGTGGAACCTAAGCGTCCTCCTAACGAGACCTCTACTTCTCTTGAGCCCACTATCTTCGGCGTGCATTTGCGTGAACTCAGTCACTAGTCTGCGTACGATCCAGAGCGTAGTCTCTTTTCCCAACGTCATATAACTGTCCCGTTAAGCCTTTGCTTTTCCCAATCTAATATTTTGTTTATGTCTTGAGGCGTACACCATTGGGACGCACATCACTGTGGTATTTTTACCAGAACCGAGGTACGCCCTTAATAAGCCGAATCTGCGCCGGCCTGGTTGGCCGATCGCGGAGAAGGGAATGAGTGTCTGCCACTTCTAACGTTCACTGGCCAGGGAAATCTCTTGAGTCATTACCTGCATTATTGCGTCCAACGTAGCCTTTTCATAACCTCCCTCACATGGTCGCCTAGCACAGATTCGAAAGAGTCTTCTTCAGGGACAAACCGGTTGTAGAATCATCACAACGTCTTTTATAACATTCGATCATTGACGACACCGCAAACGCATGGTCCGATATGCATTAACGGTGCCTGGCTCGGTCGATCGGATCAGGGGGTTTTAGACTGCAGAGCGAATTGATTATCACGCGTGGAGTAGTTACTATCGCAGCAGGTCGCATTCAATCTAGCGACCTCTTGGTGAGCTAGCACTCCGTTCTACCATCTAGGTTCCTAATACAAATCACGAACGACTGTAAGGAGCTGGAAACTACAATGATGTGGTAGTGGCTAGGTAATATTGAATCGTGGGTGCCCTCCGACGTCCGAACGTTTGTACTGATAACAACAACTTCGTGACTCCTTAGGTCTAGCTCTGATTGGTGTAGGTGTGCTTTAGTCATCGGGGTGACAGGGTAGCGTCACTGTCGAGTTCTATGCTGCCCAAAGTTCCGAATATAAGGGTTACTAAACGCTCGACAAAGCCATGGCTATTGATGGCATTAAGTCTGGCTGTTAGCGAGGTGAGTAAATGATGCCCTATCAGAGCCCAAATCGGGGGGTGGCTCGAGCAGATCGACGAGTCCGAGTTAAGGGTAAAGTACTAAAGCTGTGTGGGATTTTCCCTTTTACAGAAGAAAACTCTGCTTAGGGTGTGAGTTACGTCGTACAGAGCTAAATGCAGGTGGGGCCGGGCTAGGCCCATGTTTCTGTTCCCATGACGGTTGTCTAGACTTCGGATACTGCAAAGTAACCCCCGTCGAGGCCCCGGACAGGGTCCACCTATGATGTTATGACTATGATGGGAAATCTTGAGAGGTTTATAAGGCGTGTCTGATATTCCCAGGCCAAGTAAGTAAGGTACCAACGTGGTGTTGCGGTGGAGGGTAATTCCCGGGCCGTCTACACTAACAGACGGCTCACGCCTGTACATGCATGACGGTTGGTTTGGCCAAGGAGTAGTATCCGGGCAGTTCGAAACACCAGTTGGTCGTTACCCAGACGTTAGGGAGTGAAAGGTGGATATTATGTATTGCCTTTATTACACAACAAGTCTCTAGGAAAGCACAGGATTAGCAGTCGGAAGCTGGTCTCACAACGGAGACGCACCAATGTATTTGTGCTTAAGCTGTTGTCAAAAAATCTTTCCTACATCGGACGATACACAGAGCGTACTGAGGCGAAACGTATGCTCACAGTCTGTACGCCTATAACTATATTCCGGGTTATAGTGGACATTCCAAACTCGATAGCACTACGACTCTTAATAAAGTGATTGTGGTACTACAAGAAATACGCGAGGGGGGCCGCTGTGCGCGTTCGACTAAAACGGTTTAAAGGAACGAGAAGCCCCTTGACTTTAGCTCCCAGCGGCGATGCGTATTGACAATGTAGATGGTATGGGAACAGAGCTGATATGTCCAGACCCTTGGATTAGCCATGAATCTGCGTACCTGCTCTACCCATAGCAATCCGTGCGCGAAACAATGTCGTGTTTAAACGGAAGGTTTAAATTAAGCTGAGAACTGTACCGCCCGACCACGCTTACTATGTTGCATTCAAGGTGGGCTATTACGTTTATTCGTCTCGAGTGTGACGAAGACACTATTATAAGCCTCGAAATTCCAGACTTTGCGGGAGCACCGTCCCGGTTAGCCGTAAGCAGAAGTAGTAGGGCTGCCGGATCCACCGCTATCCCTCGTAATACACTCGAGGGCGCCTACGGTTTGAGCCTGCCTCAGTTACTAAAGCGCTGAAGAATCGTCTCCTCCTCCAATCGGGGGCAGGGTAACTGGTAGCGGCACCGAGGATGTGACAGTCTTTCTAAACAAACAGTTCGATCGAGTCATGAAAATAGGCAAGCCACCACTCGCCTGCATGCTAAATAAGTCATCTTTTGTGTTCAGAACACCTCTGCAAATGAGTCTTTTCTTCCACTCGCCAAGGCGCACAATAGCCGTTCCAAGTTTTGTAGACGGTGAGATTTGAGGCCGAGTAATATACGGGCCTCACTATGATCTTGGCCATCCTTCAACCAGAAGCCTTGCTCGAGACCAATCATACACCATATAATGTTTGACAGTGTTGCAATATCTCCCCTAGATGGATATGACCTCACGAGAATTGGCACCACTGTGATTGCGAAGGACTGCTCATCAAGGCCTTCGACTGGATGCGCCCCGCAGTCAGTAAATCGGCTTCGCGATAGCACACACGTGTCAGAAAACCCCACGTCCCGTTTCAAAACTCCGGGCGTGAAGCAAGCTTACGGACGGCCCACTTGTTGCTTGGTGCGAACTCGAGGGGTAGAGCTCCGAAGTTTGATCACGCAGCCAACCAGCTAGGGGGTAGTGGAATCTCACGAACTCTCAACAAAGCGGGCGCCTTATTGCCGCACGTTGTGTTACCGCCGATGGAACTTGGAGTTGTAATCTCGTAGGGCGCGTCCAGATCGTCCCACATGATGCACTGAGCCTGCTTAGTCATATTCATGTGTAGCGCTCAGATTATCGTAGTTTCGGGACCCTACATTATTGAGGTGATCAACTCGCCGTGGCACTTCTCGAAGTAATCCGGAACGCTCGCTGAGCAGACGCTGGGTAGGCTAGTGGCAGCCTCTGCAAAGGCATGGATCAATATCTTCTTAAGACAGAGTGTCGTCTCCTCAGTGTGGGACGTGATTTTCGAATGCCACTGCCCTTCAACTGAATAGGGCGGCCCAACCTAGCGTTACATGGCGCGAAATCCGTTGTTACGCGGGAAGGGACAAATCACTCAGCGCTAGGCTCCCACAGCAGGGGTAACTAAGAGCGAAGCATGAACCGGCAGTCGGACAAAATCCTAACTTCTCCGACCGGTACAACGAATGTGAATGTGTATGCCGCAACCTAAGTTACCTTCGTATAGCGTGCGGCTTAAGGGTATAAACAGCCTCACCTCACCAGATACCTGTTGTCACAGTCACCATATACGTGGGCACCGACGGTCGACTGATGGTAACCGATATATGCTAAGGAGTTGAATCTAAGATGATCGCCGTACTGGTTGCACCCGAACGAGGGCCGCCAGCTTGAAGAGGCGCGGGACAAGAAACCAACGCGAGGGGAGGGGCCAGTCCGCTCTCCATTGAACAGATCTGGCGATGACGCGACGTACACTGATCGACGCAGTACGAAATGCTACCCATGATCGGCTGCCTGATTTAATGCCACAGATGGGTACTATTCTACTTAGGTCCACTAGGACTAAAGAAATTGCGTTGTCAGTCCCGTTCTCCACGCTTCAAATGGCCAGGGTCACGTATCTTCGTCCTCGTGCTAGTTCCAATAAATTTTAGCTTCACTCCAGCTATCGCTCTCAACATTTACAGCAAGTGTGACCCCTGCCGATGCACAGATCTGAGGCAGCCACCGCCAATTCAGCTCCCCACACAGAACGGCAATCTCGTTCCCACCGTGCCCTACAACCTCAACATGGGTAGCCAGCCGACAACATGGGACGCCAGAACACTAACGATTATTCGGATTAAAGCAGCTCGTGCAGAGTCCCAGTGATCAAACGAGATACGTGGGTTGCATCGGGTCCTCAGCACTTAACACCGTTAGGCACGTTATACTACCTCCGCCCCTATGTGGGTACTATTCACCTCCCAGTCTGGGTTGGAAGAGTGGGCAAGTTCCAGTTCGTGTCCGGCGTGGCTGAACGCAGATCGCCATGGTAAAGGATGCTGTACACGACACAATAGACCTCGCAATTGCCATTTTGTTGCGAATACAAGTGTGGAATTAGGTTGTGGTTTTACATCTGCTGCGCACCGGAAATTCCCGCTCCTTCAGTATCACGTACTGACGACTCGGAGGGCGCTGCGAATGGTGTCATAAGCATTGTCTGTAATCGTCAAAGGTGCGTATTGCTCGCGTGTAAAGTGAAGAAAGCTATTTGGAAGCGTTGGGTAGGTCTGTGGACTAAGGGCAGGGTTGAGATAGGGAACTGCAAAGGGACGTGGGTTGGATCGCATGACTAACACGATCCATCTGGTGAACGCTTACCGGGGGCAGTGTTGTACGTTCTTTTCGCTTCGAGATCCGCCCAGTGGGATCCAGATACCGGGTACGCCTTCATTTTAAATCAGCCGTCTTGGGTATCTGCCGGCCTAGATTCGTGCTTTTTCATTGGGGTTCTATGTCTACGTGAACAATTTATTCTGTTAAGGATCCATTCACTGAGACCTTCCGTTACACAGAGTCCATGGCCGTATCCCGTCTATTGCAAGTTGGACGACCTGGGATAGTCATGCCTAAGCTCCGCCGGAGACGAGGTGGTTCGTATCAGGCTCAGTGGCGGCATTATATGTTATTGATTAAGCGAAGGACATTGGATCGGTTTGCCTGCTGATGCCGCGGTGTACGGTATAAGATTGTGATACATATTCGGCAAGATCCTCCACCAGCTACAGGAAACCTGCTATTGAATACATGTGCACGAGTTCATGTTTCTTACTTCTTGACTTGTGTCCTTGGAAGCAAGTCCCATCGACAGGAAAGGCAAAGGCCGCTGAAGTTTCGAGAACCGTAACGATTAGTGCGCGGGGGAAGGCCGACAGGTGGGTCAACGATAAGGCTCTTGGACCTACCACATTCACACTTAAAAGGCCCGGGCAGACGACTGTACCATCCTGTAACTCCGCTTGACGTTGAACATGTTGAGGTATCTGGGGCGGGCGTCGGGGCGCTAATCTCCTGAAGATAGCCCAGAAGTTTAACTGATTTAGATGCGGGGCGTGCATAAGCATTCCTGTCGTATCGATCCACATTTATGACATCTCCCCATGAATAGAACAGGGACCTCAGCTCAACTTGTGCGCTACTAACGTTAGACTAAAGAACACAACGATTGCTCCAACCTGAATGCAAAAATAGTGATACTGCACGTTCAATGGACAATTGCTTACGCTGTGAGAGCCTAGTACGGTACAAAAACCTCCGTGCGGCCTCGAGGAGGATGATCGAAAGGGTATGCATGAAGGCTCAGCAAGCTTTACTGACAGTGAAGCGGCCTTTACCACCCCCACCCCCACGTCGTTCGACTAACTCATCTCTTAACATGTAATCCTATATGGGTGTCGACTGAGCATATAGCTTGGCCGTTAATCTATTCTTGTGGTGTGAATGATGAGATTTCGTTTGTTAAGAATCCGTGTGTCTCATGTACAGTGGCAAAAGCAAAATGTATAGACTCCATATCCACCAATAAAGCGTGGCTATCTGTTACTACCCCCGCTAGAACGACTCAATGTAATCTCGTGAGAGGCCCTAAACAACCGGCTAACACCTCAGCATAACTTTGTATTCAGGGCCGCAACATTTGTTTTAGGGACAGCCCTGGATCCAGGCCGAGAACCGAGGTGCGATATACAAAAGCTGGGGATGAACTTACACCGTTCACTCGGCTCGTAAGTAGTCTATAAAATATCTCTCACAGCAAGCGCTAGAAACCCTGATTCGCTCGCTTATTACTGGCGGTCGCATATCCGAATCACGGGCGATTCGTCACCCAGATAACAGTACCTGACCGAATTCGCGCGGGGGCCACCAGGCGCAAGAGCGTCTATGCTTGTTGTTGCTCACCCAAACCGATAATGTAAGATGGGACGTATTCAGGCTGATTCGCCCTACTTAAAGTTGAAGTCAGAGAGCGTCCACCATAACACGAGGCTCAACCTCCTCAGAGACATCAGCGTCTTATTTACGCTCAAGGCCGGTAGAGCTAGAGGTCAGTTACTTCCTCCCGGGAGTGAAACTGCCACTAGCTCGTCTTCGAGCATTGTTAGGCCCCAACGCCGAAGAACGGACATCAGCTTGACTACCCAAGCAAGTGGTAACGTCCAAACTAATTGACACACTCTGTAGAGTATGGCGTACTGTAATCGACCGTGGCACGGTGGAAGGACTATGACGGTCCCTCCGTCCGCGAACGACAGTCTAAAGACTGCGTACGGCTCAACGAAACTCACTTGCCTTTATTTCGCATGTCGCTGGAACTAAGCGATGTTGAAATAACAGGCCAGAAAGCACCCGTGACAAAGTTGTGCACATTCGACACTCTACATTCCGCTGGATAGATAATGTCCTTACCCGCATTCTTGCCGCGGGAACGTCTAAAGCCTGTAACAAAGGGGGTATACTCTGGGCCTTGGATGAATTAACTGTCTCAACGGTGCTCGGTACCCGGGGACTTGTTCGACCGTAGAGAATTCGGCGGTCTCAGCACGACAGCTGGACTTCGTAAGGACCTGCTGGCTTGGCATACTCGTTCTTGCCAGAGCCGGCCGGTAACGCTAGGAGTATCAGCATTTGTCAGTTGGGTTATCTAATAGTGATTCCTGGACTTGGAGCAGGGTGTCTCCCGTCTCATTGTGAGAAGTGCAATTTGAAATATATGGAAAAAACATCACTCCTCCCTATCGTCGGTGAGCAAGCTCCCCTCTAACGCTCTACACTTTAGACTAAGAGATAACGCCTAGTTCCAGTGCCTTAGATACTGATGCAAGGAGAAATTTCTTCAGACCACGAAAAGATATCCAGAATTGACCATGCTCCGGTATGCGGCTACTCTCACAACGGACTTCGCCATTTCCTAGACCAGATTTGAGTGGTACACCGGGCTTAGTGTGGGATGCAGGGCGGAACTAGTGGGGCTACCGAAGAATTCCTGTCCTACACTCGGATGAATTGCTAGTTAGAGAGGAAGACGGATCCACCGTTGCCTATACTTCTGTTACTACAGCCCGGATAACCAAACCGGGTGTATCTACTGACGATGCGAGCTGACGTTACACCCCTGGGGCTTTAGACCGTGCTACGATCCCAAAGCGGAGGTTGAATCGATTCTGGTTCACGAACGTTCAGCAGAAGCCAATCTCGAGGCCTGAAAGAGCCGAGGCGTTAACGCTGGCACGACGCGGAATACAAGCTTCTCAGATCACGCGTAGCGGGCTACAATGCTCTACGTCCATCACCTGCGATCCCCCGAAATGCGTCCACATAGGCCCCTAAGGCTAGCCAGCAAGTCTATGTAAACTTGGTGGTGTCGCGCTATGGAATGTTGACAAGTACACGTTGGTGGGGGTCGCTCCAAGACTTTATAACTACCAAGTGACGATTCCCCCTAAACCGACCATGGTTTGCAGCATGGCAGACTTCGCAGTACAAGAACTAGTAAGACCGGATTTCACCGTTTACATCAATGATTCGGTGAGACGATCCGAACGCAGTTCCCCAAAAGGGTCCGCATGCCTGAATGATGGACGATACTCCCGTACAACTACAGGACTCTGGACTTGTATGTCCGCATTTATTTGCACTCACTACGGCAGGACTTAACTCCGTAAAAAGAGCATCTCGTACCGGGATCACAGTAGGGCGATACAAAAGGCCGGGGATCACCGCGGGATTCTGGGGCAAACTGGGACTGTTGGCGTATAAGGAGTTCAGCGCGTTAGACCCGTTTTTCGCGGTCGGAACTCACCCATGGTGATGCGAAACAACACCCCAACGAACGATGCTGCATCTGGTTCCCGTCTTATCGATAGCATACGACTCTGGACCGTCACCTCACAACTTGAGGTCGAAACACCCCATCTGCGGTGAATCAGGTCGATCAGTGTGCCAGCATGGCCGGTAGACATTTCCGATATCCGACAAAGCTCCTTGGCACATATGTGAGTATGGTGATACTAGCTTCTCATCGGCTAGCGGAAACTCTCAGTGCCTCGATCTGTGGACACCCACAGTCCGACTAGTGACGGAATAACTACCTTATTCGATGCAACTCTCTTATGATGCCTTCTCAACGTTAGGCGCTTCCATAAACGACTCCTTTCACAAACGCGGAATAACGACAATTGGATGGTCCTGCGTCTGGTGGCAACTCCCCCGTTGCCTAACAGTTATGTTCGAACGCTAAACACAAACCATGCATGTTGAGTTACTGTTGTCATGTATGGGATTGCCAGCGTTCTCAGGGGCGGGGCGGCAACACAATACCAGATTTCATCAGACAAACAGGCATCTGTCCATGTGAGAGTATTAAACGGCATTATGTGATGGAAGGCAATTCACCGCGTACAATCATACGATTGGGCTGATTCGATCTGGGCTATATCCAAGACGGGGTATTAACTGCCGTATTGTAAAAGACTTTGTAAGCAGTCTATGTCGCCGGATCTATGAAGCCTGGTCTCGGAAAGATCCCGAATGAATTGTGAAATGGTTGCGGGGATATAAAGGAACATCCCCACGGCGATCTCCCTACCGCCCAGGTTCTAGTGAAAGTATCCCACGCCGTGGAGTATGTCTCTGGGACGGTTCACCTCGTCATTTTAAGGATTGGACTTTCGCTGATTACTGACTGATCAGACTATCGTAATTACCGCAACCGAATCGGTAATTTTGACCGGCTAGTTTCTGTAGCGCTCCACCGAGCACCCGAATAGACGGCGCAAATTGCTGACCATCAATTATGTAACGCTAAAGCTGGATCTCCGTACCTAATGTGCACCGTGGGTGCGCTCTTATGGCTCTGAGCAATCACAGTCTTTAATCCCGCAAAACAGGCTTAACATGGTGCACATAGCACTGATAATCCGATCGTCAGACGAGAAATTCTTTCTAACTCTTTGAGCTAGACTTCGTGAATTGGTAAAGGAGGTTTGACTACGGATACAACAAACTCGGAGGGTCTCTTCGTATGGCACCACTCCGGGCCTCCTCCATACGGCGGTCAACCAGTGCCGGACTGGCCGATCCGTTTTAGGCCGTTAATATGAAAACCACAAGTGTCTGCGGCAGGTCGGAGGCTGCGGTCCCGTGCACCACCAAGCGTCTCAATATAGTTGATGTAGTTATGAACGCGCGAGAAGTACTGTATGACAGCTTGGGGTAGGCGCGGTAGTTACCGAGGGTCGGCGGTGGGGCTTCGATCAACGAATAGCAGATAGCGGTCTAGCAACACAGGACGATAGACAGCGCGAAGACATGAGTCCACTCAGCATGCTCACCCAATAGTACCTGATCGGAACTTTCCGAGATCAATAGCGCTTCCTTAGTATGGATGATTGCTGCTGTAATCTACCTGACTGTCGAGCTGAAGACAACTAACTAAATCGCTACCATTAGATGTACGATCGCCGGTCCCAGTGGTGACCGCTTAGAGAAACCAGCGCAGGGCTTGTACGATCTGCAACTACAGACACCTACTGACTCAACTGCGGTCCATCATGGCACGTTTCGAGCCGGCTATACCGACGGCTTGACTGGCAGCAAAATCTAACGGTGAGGCAACGAAACAGCCCGGGCCCGTATGATTGCACCCTTACATCGCTCGGTTTGGGTCCCGATTTTTATCAGCACTGAAAATCTAATCATTGAGAGGCCGAAACGTTCTTGGATGGCCAGAGCTCGACAGTTACCAGCTCCCTTGTGTTACCGGCAATGTCGCTGCCACGGTGCTTCCTCTTAGGAGACATACCAAGGTTCTTACGACTGTGGGCAGGCCCATACGTGACGCACATGGGAGTTACTAGGCTTTTGAAACAACAACATTAACTCTACCGGTTATTATTGAATACTTGTCCTGGGAATAATGTCTTTCCGTAATCCAGGAGATCCCAAGCGGTGCCCGAAACCAGGTATCCTCGCCTAAACGATCCAGCACCGAACTTAAGAATCCACAAGCTGATCACGGGCTGTTTCCCGACGCTGAACTCTTGAGTCCAGACTCCTACAGGACATGTGTCCGTCCGGCGTCGAGTTTATCAGCCTTCGCGAGGCGTGTTATCCATACGCAGAAAACGGCGGACATTCAATAGCTCAGGTCCTCTTGCATATAATGAATGAATTTTGAATCTTACCCATACCGCCGGAAGTTATCATCGTCCGCCTCCTCCGTTCCGGCAGTTGTTGAAGAAAACCTGAGGAAATGTTGCGTAATCTCATTGAGACTATTCAGGTACTCAGGAATAATGTGCGCTTCTCAGCTCTTTAAGGTCGGAGCGTTACCAGAGGCGAATTCTATGGTTCAACATTCCCGACTTGATTCAGCATGCACGACGACCCACCCGGTTCCTTGATACGGGCCTTTATGTTGTCCTTTTTTCTTACGGCACGCGGGTCTGCCGAGTTTTACGCGATCCTGATTGGAATGCGAGGACAATAAGCCTGAACCTTTTTCTGAAGATACCCGTTATCCCTTTCTTGGCGTGCAAAGGGACTCCTCAGTCCAGATTAAGAATTTTCGCTGATCCAATTACAGTAGCCAAGTCTCCCAAGTCATATAACGCTCCCCCATGGTGGAACGTTGAGCAAATGCAGGACTCCTCTTGGTCCAGCCGTTGATCTTTGGGGGTACTGCTCCCCTCAAAACAGTGGTCTGGGGTCATCCCATACTGGACCTGCGCTTGCGTCGCATCAGTTCTAAACGTTGACGAACATCTGGAGGTGGAAACGAGAAATAACTAGGTTGTAACTACGGTTGCACGTGGAATGTACCGGAGCAGGCTACGGCCCTGGACCACAACTGGAGACTATGGTTAAAGGAGCACGTACGGTACGATGCTCGGGTGAATCTGTCACAGCAACTAGCGTTGTGCGAGCACCTTGCCCTGACAGTTTGTATTTGCTACCAAACTCAAGTTGAGGTTTCGATATCGGCCCGCTACGCCTATCCTCGAAGGTACCAAACCATTTGGTTAACCTCGGAGGCAGTCTTATTGCTCTAGGATTCTGACACGATCCGGCCAGCTTGTGATAGCCGCTGGATTCGGTCTGATTATCGCGCGAGTTACCTAAGTAGGCGGTGTCATTTCTACACCATCAGTTCAGAATAATCCCTAAATGTAGCCTAATACCCAGGCGCTGAATGCCGCGTTGTACCAGAGCATAGTCACTCCGTCCTAGAAATTGAGACTCCTCGAACGCCGATTAGACTCGGTGTCAACTAGGAGATAGGTACCTCAAGCGTTAATAACGCTGACTCGCTCATATCGCCACCCAGCAACGACTAAGGTAAGTTTCGTTAGGTCTTGCACAAGCAGAGTATATGCTAAATACCACTCGTCGTTGGACAGCGCCCTGCACGATTCAACTTTTCATTCTTGCCGGCTTTTAATAGATTTAGCGCGCGTTGAGAGAGTCGGACCTTGTCACGATCTAGAGTGTCGGTCGGACCAGTCTCTATAAACTACTAACAGAAAGTTCCGATAGTGAGAATAACTGCATGCGTTCTCACTCTCTGTTATTGGGTAACAGACTTCGTTGGTGAACGTAGTTCGCGGACGCTCGGATCGACCGCTGCGTGTCGTCCACAAGTGTTCAGGACTCCACAGGGAGGGATGACTCTGGTTTCTTACCGCTGGTAGGCCCGTTCTCCTCCGAGAGTACTCTCTTCTCCCTCCACGTTGGCCATATGGACGAGCGGAGGGAGGATTCCGGCGCAGGGGCCATCCTGGTGTTCTGATGACTGCGTACTTACAGACGGCAATAAATGGCGAGACGTCGTCCAAGTCTTATTGGAGCTCCTTTCTGGAGCATCTATTAACATTTGTCTCGCATAGCTGTCATGATTCAAGGTCGAGACACATTGGCGAAGCTGGTTCCGCAGCTGCACGCACCGGAGGCCCACTGAAAGAACAATTGCAGATGATGCACACGCAAGACACTAGGGTACCTCCTTGACACAGTAGTAACTTACTCTATTTACTTCGTCCGATTTTATTTCTGAGGCGCCAATGACCGTGTGACATGCGTCGATACCATTTTCTGTTTTCGTTAGTGAGTTATATAGCCGCTTGCCCTCAATAGGGATAGTTCTAACACAAGTGACACGCATACCATACTGCTCACGATCAGATGATGTTTTAATTTTATTCGAGCTGTAAGGCAGCTATTCCGGCTCTTTGGTCCCAGCTGTGGCCACTCGCATATTCTTCAATACTGCTGGGAACAACGGTTAAATGGTGATTGTCCTGACCCAAGTGACACCTCCACGATAGATCACAACCTCTCTAAGCGAGATGGCGTATCAGTTGTTGAATCGCAAAGAGCTAGGGCGCGGGTGTTTGACCTGTACGACGTGTCATGTAGCTAACAGTATATGGTGAGTAGCGTGACAGGCCGTTGGGGGGTTACCCCACACGACGGGTCTTCCACACGTGACCGACTTGGGCTTAACTTACTTATCATTGGACATAGGCGGTCCCCATTTTAAAGTAGCGGAACACCCGTCTCCGAGGATTGGTGTTGCAGGATAGAGATTAGAATTGACCGATTTGTGGGACAAGCGATTTCATCACTAGAGAGATATGGGTCCGCTTATAAAGTATCTTCAACAAAAGGTCACGCGGTCCATTATCCGACTAAGCTCCTCAGGGCGACCCGGCTCATGTTTACATTTCCTCCCAGCCCTGGGAGGCAGGGTATCTCAGTTAGACCTAGTCCACGTATCTGATAATTCTTTGACACACGCTAAGTAGTCAAAGAAGATCATCGAACTGTTAGCTGATGCGCGCGTACGAAAGAGCAAATTACTCGTAGCTTCTTGGGGCGGGGAATTAGACAATAGATTGATCTTTGCAGCATTTGCCGCAGGTGTCCCCATACAGTAGGGGACAGGCCTTTAGGTCGTCGACACAAGCCCTCTCTCCCCTAGCATAGATAAGAACGATACAGTAAAACGCTACTTTTCCCCGGGAAAAAACAGTCTCCGTGCGGATTGAGTATCAGCGTAGTAAGCACAATCTTTCAAGGTTGTGCTGTAGGCTTAGTGAGATCCTACCACACGGACGGGTAAGCTATGGGTCAAATGAGTCCTTGCGAACGCCGGGACATTGAAGACAGGTCCCGTAAAGACTCGGGCGACCGTTGTTTAGAGAGGGATAAGCTACGTTCACGTGCTGAATCGTATCATCATCTCTTGCTGTTCCGAATACCTACTCGCACCATGAATAGGTGCGAAGATCCCATGTGGCCTTGCGTGGACTTCTTCCAGTCCAATTAACGATCAGTATAGAACATTTGTGAAGATTCATCCAAAGGCCGAACTTCCTAGTCCGCGTTGTCGGGGTTTGCTCCCCAACTAAAAGCTGGCAACATAAGCTTGTTCAAAATCGGCACGTATCAACATGAACCTTCACCCTGCCTGGTCACTAAAGCAAATATTGTGAACAATTCAACTTAAGGGCAGATCTTTCGTTGTAGCTGGGACACGTCTGCCTTCTATCGCAGAGGGTTTACGCCATGACAGACGGCCCCTAACAGTGAGTACACCTTCTATGGACTAAGGGGCTGTCACTTCTAAGCTCAAAAACCAGTGACATGTGAATTTGCTTAAATAAGTAGGATCCGGTAGTGCGACTGCACGCACCGATCGGCTTCTGAAGCCCTTGCGCCGTAGGATAGACAACCAAGCTTAGAAATCTGAATCCGGGGTCGACGCCCCTATACATAAGGGCGTCGTTTTCCGCGGCACAATTCCTGAATAAGCCGGCGAGTATGGTAGGGGCTAGACCCCGCAACCATTGTTTCGGTGGTAGGGGGTAATCATTACATGGATGTATACACCTACAATGCCGTCGCGACTCGACTCGTGCGACCATCGTTAGTCAATGCGACATCGTGCGGCATCACGTTTCCCGAGACAGGTCTGATCACTCAGGACGCCTTGATCGGGCACTGCGGTGGGAGTCACGACGGAGATGTATTCACATACTGATCTTCGGGGTCTGGTAGATATGGTATGTCGCAATTGGTCGCTCCCGTGTCGGCGTCCGCGTCGTTTTGAAGGTCTTGACTAAATGCGCAAAGGTTTGCAAATTAGTAAAACGTCGATGCCAGAGGACGAGCTCGTCGACTAAATGATTACAGTAAAAGGGGCCTAGTCAGGAGCCCTCCTTATCAGCGCTCAGCATTAATATTGCGTCCAAAGCTTTCGATTCACAGAAACTATAGTAATTTCCAACTAGTAATAGCCTGACCCAACTCCTGCCCAGCGTCAGGCTGTGCATGCACATTAGTGCCTTGTCCCTACCAGTTCTCTGTGCCCTCCACCTACTTAAACCGTAATCGTCCCTCACCCCGGCCCTCTGGCACCTCTATAATTATCCGAGAAGTTTAGCAACCCCTAATTTAGTTCGAGACTGGATGATTTATCTACGGAAAGTCAATTAAACGTCGCCTGCAGTTGGGCCCACACTTAGTAAGAGACTGATACTTGGCTAACCACATACCATAAGGGAATCACATGATCGTGAGGACCGCTGAATAAACTCTTAATTCAAAAGGCTACTGGATGGCATACGGTCAAACACCGCGAGTGAAAAACTGTGGAATGTCCATAGTTCCTTTGCGCGACCAATAAATGGATCGATGTTCAGCCTGACTGTCAAAGTTTGGGGGCATTTCCACTTATACGGTATAAATTTGGCGGGTGTCGGATAAGCTATGTTGATCTTTTACTGCTCTGCGGTGCAAGGGCAACACGCGACGAGGCTCCTGAAGCCCCTCAAAGTCCTGACGGAGAATACCCAGTGAGTATGCCCCCCTGTTTGGCCGTCTGGTTGAGCAGAGAATCTTCATCAACCTTCGTTCGGCGCAACACCAGGATATATGTCAGATGTCGCCCGTTCCGGCTCATCAGTGTGGTGTTTCTGTTACTAAATGAGGAAGAACGCGCGCCAAACACCATCCTACCACATAGATACAATAACCGATCGCGGAGACGCGTCGTGAAGTATTGGGGGCATTGTTTTAAAGTAGTTGTCTCTAGCCGTAAGATACACGTATCGTAGTGCCCTTCAACACTTTAAGGGAGTTTACCATCACTATCAGATAACGGGGTTACATCCGTTCTTTTCAGTCGCTCCATGGCCCCCACGCTGTTACGCCCACGATACTACATCAGCAACGGTGGTTTACTTGGGGCCTCGCCCTTATCTGCAGTCAATGTTCGCATTACATCTAAAGGGGTCGAAGCGTTGATCAACGTTGGCCAAGCCGAGGGGTACGTCAGGCTGGTACGCCAACCGTGAGACACGTCCGTACCGTCTGACGGCTAGCTGTTTACTTCAGTTCCCGGCGTGGAGACCAATGATCGGTAGGTTGTCTCGCGTGTTCAGCCCCGGGCTAAAGGATCAATCGCTGCCCTTTCCTTGTAACAGACGAGTATTCTCAGTCCTTAAAGCCCTCGGTTTCGTAAAGGGAGCTCGCGGCGTGCCGCGAGTGAATGGCTGTCTTAATTAGTTTATACTTTCGTCACTTCAAAGGGACAACGTAGTCAGTGGAAAGCGTCGGCTATCGTGACCACCAGAATCCCTGCAACCGGCACACGTGCTCGGCTCCCAAGGATCCCGACGCCGCGAGCACCTTAAGTATTAAGGAGCCAGCATACATACCATTCACTAACACGTGTTCTCGCGATTACCTTTCAATGCATCTGCTTGAAGCACATAGGGTAGTGGAGTCACCTATCTTGATTTGCGTGGGCCACCCTAGCCAGGACGACAACGACCAAATGACCACGTCCAACCTTTAAATATGGGTGTATGGATTC'
d = 5
print(approximate_pattern_matching(genome, pattern, d))