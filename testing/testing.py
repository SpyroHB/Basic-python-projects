def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError()



