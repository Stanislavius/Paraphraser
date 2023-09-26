from nltk import *
import copy
import itertools


def get_permutable_phrs(i_tree, path = [], phrs = ["NP"], conj = [",", "CC"]):
    result = []
    for i in range(len(i_tree)):
        if type(i_tree[i]) == Tree:
            j = 0
            stage, phr, found = 0, "", []
            while j < len(i_tree[i]):
                if type(i_tree[i][j]) != Tree:
                    j = j + 1
                    continue
                if i_tree[i][j].label() in phrs and found == []:
                    found.append(path+[i]+[j])
                    phr = i_tree[i][j].label()
                    stage = 1
                elif found != [] and i_tree[i][j].label() in conj:
                    stage = 2
                elif i_tree[i][j].label() == phr and stage == 2:
                    found.append(path+[i]+[j])
                    stage = 1
                else:
                    if (len(found) > 1):
                        result.append(found)
                    stage, phr, found = 0, "", [] 
                j = j + 1
            if len(found) > 1:
                result.append(found)
            result += get_permutable_phrs(i_tree[i], path+[i], phrs, conj)
    return result  
                    
def get_permutations(input_tree, permutable_phrs, limit = 20):
    variants_of_permutation = []
    res = []
    for i in range(len(permutable_phrs)):
        local_perm = [i for i in range(len(permutable_phrs[i]))]
        local_perm = itertools.permutations(local_perm)
        variants_of_permutation.append(list(local_perm))
    
    permutations = list(itertools.product(variants_of_permutation[0],
                                          variants_of_permutation[1]))
    for i in range(2, len(variants_of_permutation)):
        permutations = list(itertools.product(permutations,
                                              variants_of_permutation[i]))
    i = 1 #in order to not include initial tree
    while i < len(permutations) and (i-1) < limit:
        permutated_tree = copy.deepcopy(input_tree)
        for j in range(len(permutations[i])):
            for z in range(len(permutations[i][j])):
                permutated_tree[permutable_phrs[j][z]] = \
                input_tree[permutable_phrs[j][permutations[i][j][z]]]
        res.append(permutated_tree)
        i = i + 1
    return res
        
    

def get_paraphrases(input_tree, limit = 20, adjust = True):
    i_tree = Tree.fromstring(input_tree)
    permutable = get_permutable_phrs(i_tree)
    phrs = get_permutations(i_tree, permutable, limit)
    if(adjust == True):
        for i in range(len(phrs)):
            phrs[i] = str(phrs[i])
            phrs[i] = phrs[i].replace("\n", "")
            phrs[i] = {"tree" : phrs[i]}
        phrs = {"paraphrases" : phrs}
    return phrs
    


if(__name__ == "__main__"):
    s = "(S (NP (NP (DT The) (JJ charming) (NNP Gothic) (NNP Quarter) ) (, ,) (CC or) (NP (NNP Barri) (NNP Gòtic) ) ) (, ,) (VP (VBZ has) (NP (NP (JJ narrow) (JJ medieval) (NNS streets) ) (VP (VBN filled) (PP (IN with) (NP (NP (JJ trendy) (NNS bars) ) (, ,) (NP (NNS clubs) ) (CC and) (NP (JJ Catalan) (NNS restaurants) ) ) ) ) ) ) )"
    paraphrases = get_paraphrases(s)
    import json
    with open('data.json', 'w') as f:
        json.dump(paraphrases, f)
