# Just Following the Course "i already mentioned this built-in functions"
def min_max(t):
    return min(t) ,max(t)


# Using * in sum_all parameter will take any "n args"
def sum_all(*values):
    s = 0
    for x in values:
       s += x
    return s


# traversing in two sequences "t1[0] == t2[0]"
def has_match(t1, t2):
    for x, y in zip(t1, t2):
        if x == y:
            return True
    return False








