# Reverse dictionary mapping 
def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse


# Counting Each Letter with 
def histogram(sentence):
    d = dict()
    for x in sentence:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
    return d


# Similiar to invert_dict "Reverse traverse in dictionary"
def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError()



