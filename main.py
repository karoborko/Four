import Score as sc
import Greedy as g

DNA = [('tagtggtcttttgagtgtagatctgaagggaaagtatttccaccagttcggggtcacccagcagggcagggtgacttaat'),
       ('cgcgactcggcgctcacagttatcgcacgtttagaccaaaacggagttggatccgaaactggagtttaatcggagtcctt'),
       ('gttacttgtgagcctggttagacccgaaatataattgttggctgcatagcggagctgacatacgagtaggggaaatgcgt'),
       ('aacatcaggctttgattaaacaatttaagcacgtaaatccgaattgacctgatgacaatacggaacatgccggctccggg'),
       ('accaccggataggctgcttattaggtccaaaaggtagtatcgtaataatggctcagccatgtcaatgtgcggcattccac'),
       ('tagattcgaatcgatcgtgtttctccctctgtgggttaacgaggggtccgaccttgctcgcatgtgccgaacttgtaccc'),
       ('gaaatggttcggtgcgatatcaggccgttctcttaacttggcggtgcagatccgaacgtctctggaggggtcgtgcgcta'),
       ('atgtatactagacattctaacgctcgcttattggcggagaccatttgctccactacaagaggctactgtgtagatccgta'),
       ('ttcttacacccttctttagatccaaacctgttggcgccatcttcttttcgagtccttgtacctccatttgctctgatgac'),
       ('ctacctatgtaaaacaacatctactaacgtagtccggtctttcctgatctgccctaacctacaggtcgatccgaaattcg')]


######################### GREEDY MOTIF SEARCH ######################
plik = open("greedy.txt", 'w')
plik.write('GREEDY MOTIF SEARCH\n')
s = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
t = len(DNA)
assert t > 0, 'error'
score_list = []
for k in range(3, 80):
    max_score = sc.Score(s, DNA, k)
    g_place, greedy = g.Greedy_Motif_Search(DNA, k, t)
    score = sc.Score(g_place, DNA, k)
    best_score = round(score / max_score, 2)
    score_list.append(best_score)
the_best_score = max(score_list)
y = score_list.index(the_best_score) + 3
plik.write("Best score = %f\n" % the_best_score)
plik.write("k-mer length: %d\n" % y)
greedy_pleace, greedy = g.Greedy_Motif_Search(DNA, 10, t)
greedy = ', '.join(greedy)
plik.write(greedy)
plik.close()

