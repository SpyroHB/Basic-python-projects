def slicing(nvals):
    nvals=8
    message='Input a number: '
    a=[ ]
    b = []
    for i in range(nvals):
        a.append(float(input(message)))
    print('The list = ',a)

    for i in a[0::2]:
        b.append(i)
    print(b)

############################################################
#In Reverse Form
def reverse_slicing(nvals):
    nvals = 5
    message='Input a number: '
    a=[ ]
    b=[ ]
    for i in range(nvals):
        a.append(float(input(message)))
    print('The list = ',a)

    for i in a[-1],a[-2],a[-3],a[-4],a[-5]:
        b.append(i)
    print(b) 


###########################################################

