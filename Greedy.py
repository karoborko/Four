import Score as s


def Profile_list(DNA):
    rows = len(DNA)
    columns = len(DNA[0])
    assert columns > 0, 'sequences cannot be empty'
    assert rows > 0, 'DNA cannot be empty'
    profile = []
    try:
        for j in range(columns):
            A = 1
            C = 1
            G = 1
            T = 1
            for i in range(rows):
                if (DNA[i][j] == 'a'):
                    A = A + 1
                elif (DNA[i][j] == 'c'):
                    C = C + 1
                elif (DNA[i][j] == 'g'):
                    G = G + 1
                elif (DNA[i][j] == 't'):
                    T = T + 1
            amount = A + C + G + T
            A = round(A / amount, 3)
            C = round(C / amount, 3)
            G = round(G / amount, 3)
            T = round(T / amount, 3)
            profile.append([A, C, G, T])
    except:
        print('ERROR! Profile_list function doesnt work')
    else:
        return profile


def The_Best_Pattern(DNA, k, Profile):

    best_score = 0
    position = 0
    try:
        for i in range(len(DNA) - k + 1):
            score = 1
            for j in range(k):
                if DNA[i + j] == 'a':
                    score *= Profile[j][0]
                elif DNA[i + j] == 'c':
                    score *= Profile[j][1]
                elif DNA[i + j] == 'g':
                    score *= Profile[j][2]
                elif DNA[i + j] == 't':
                    score *= Profile[j][3]
            if (best_score < score):
                best_score = score
                position = i
    except:
        print('ERROR! The_Best_Pattern function doesnt work')
    else:
        return position, DNA[position:position + k]


def Greedy_Motif_Search(DNA, k, t):
    best_motifs = [DNA[i][0:k] for i in range(t)]
    l = len(DNA[0])
    best_motif_place = [0] * t
    try:
        for i in range(l - k + 1):
            motif = []
            motif_place = []
            kmer = DNA[0][i:i + k]
            motif.append(kmer)
            motif_place.append(i)

            for v in range(1, t):
                profil = Profile_list(motif)
                position, kmer = The_Best_Pattern(DNA[v], k, profil)
                motif.append(kmer)
                motif_place.append(position)
            if (s.Score(motif_place, DNA, k) > s.Score(best_motif_place, DNA, k)):
                best_motif_place = motif_place
                best_motifs = motif
    except:
        print('ERROR! Greedy Motif Search')
    else:
        return best_motif_place, best_motifs


if __name__ == '__main__':
    print('test of the Greedy Motif Search function')
    dna = [('ggcgttcaggca'), ('aagaatcagtca'), ('caaggagttcgc'), ('cacgtcaatcac'), ('caataatattcg')]
    print(Greedy_Motif_Search(dna, 5, len(dna)))
    assert (Profile_list(['a', 't', 'g', 'c'])) == [[0.25, 0.25, 0.25, 0.25]], 'Profile_list function doesnt work'
    assert (Profile_list(['a'])) == [[0.4, 0.2, 0.2, 0.2]], 'problem with theLaplace in the Profile_list function'
    assert (The_Best_Pattern('aagaaa', 3, [[0.4, 0.2, 0.2, 0.2], [0.4, 0.2, 0.2, 0.2], [0.4, 0.2, 0.2, 0.2]])) == (
    3, 'aaa'), 'The_Best_Pattern doesnt work'
    assert (Greedy_Motif_Search(['aaaa', 'aaac', 'acaa'], 2, 3)) == (
    [0, 0, 2], ['aa', 'aa', 'aa']), 'Greedy_Motif_Search doesnt work'
    print('functions work fine!')
