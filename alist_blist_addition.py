def slicing_elements(nvals):
    nvals=4
    message='Input a number: '
    a=[ ]
    for i in range(nvals):
        a.append(float(input(message)))
    print('The list = ',a)
    b=[7, 0, -3, 8]
    c=[ ]
    for i in range(nvals):
        c.append(a[i] + b[i])
    print('The element-by-element list addition = ',c)