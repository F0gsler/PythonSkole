def ComprehensionListNum(numbersList):
    comp_sqrList = [i**2 for i in numbersList]
    return comp_sqrList
def  ComprehensionListStr(stringsList):
    comp_stringsList = [s for s in stringsList if len(s) > 3]
    return comp_stringsList

def ComprehensionSetsNum(numbersSets):
    comp_evenSets = {i for i in numbersSets if i % 2 == 0}
    return comp_evenSets

def  ComprehensionSetsStr(wordsSets):
    comp_WordsSets = [word[0] for word in wordsSets]
    return comp_WordsSets

def ComprehensionDictKeysValues(keys, values): 
    ny_dict = {k: v for k, v in zip(keys, values)}
    return ny_dict

def  ComprehensionDictStudent(students_scores):
    ny_dict = {navn: karakter for navn, karakter in students_scores.items() if karakter > 4}
    return ny_dict

def merge(L1, L2):
    new_merge = L1 + L2
    return new_merge

def detect_ranges(L1):
    L1 = sorted(L1)
    ranges = []
    current = [L1[0]]

    for num in L1[1:]:
        if num == current[-1] + 1:
            current.append(num)
        else:
            ranges.append(current)
            current = [num]
    ranges.append(current)
    return ranges


