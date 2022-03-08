def elements_elemntsAddition(nvals):
    nvals=4
    message='Input a number: '
    a=[ ]
    for i in range(nvals):
        a.append(float(input(message)))
    b=[7, 0, -3, 8]
    c=[ ]
    for i in range(nvals):
        c.append(a[i] + b[i])
    return 'The element-by-element list addition = ',c


# Slicing elements of list
def slicing(nvals):
    nvals=8
    message='Input a number: '
    a=[ ]
    b = []
    for i in range(nvals):
        a.append(float(input(message)))
    for i in a[0::2]:
        b.append(i)
    return b


#In Reverse Form
def reverse_slicing(nvals):
    nvals = 5
    message='Input a number: '
    a=[ ]
    b=[ ]
    for i in range(nvals):
        a.append(float(input(message)))
    for i in a[-1],a[-2],a[-3],a[-4],a[-5]:
        b.append(i)
    return b 


###########################################################

