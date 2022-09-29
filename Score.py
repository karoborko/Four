
def Score(s,DNA,k):
    score = 0
    for i in range(k):
        cnt = dict(zip("acgt",(0,0,0,0)))
        assert (len(cnt)==4), 'too many elements in the dictionary'
        assert(cnt)=={'a': 0, 'c': 0, 'g': 0, 't': 0},'dict and zip in Score function dont work'
        for j, s_val in enumerate(s):
            base = DNA[j][s_val+i]
            cnt[base]+=1
        score += max(cnt.values())
    return score


if __name__ == '__main__':
    assert(Score([0,1,2],['aagaa','tttat','aatat'],2))==4,'Score function doesnt work correctly'
    assert(Score([0,0,0],['aagaa','tttat','aatat'],5))==11,'Score function doesnt work correctly'
    assert(Score([0,0,0],['aagaa','tttat','aatat'],0))==0,'Score function doesnt work for k=0'
    assert(Score([7,0,0],['aagaa','tttat','aatat'],0))==0,'Score function doesnt work for k>t'
    assert(Score([0],['aagaa','tttat','aatat'],0))==0,'Score function doesnt work for small s'
    print('Score function works correctly')
