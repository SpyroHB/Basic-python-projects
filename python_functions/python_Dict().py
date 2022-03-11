import readline


def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse


def histogram(s):
    d = dict()
    for x in s:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
    return d






