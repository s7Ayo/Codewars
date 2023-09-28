def accum(s):
    lst = []
    lst[:] = [char for char in s.upper()]
    outputlist =[]
    for i in range(len(lst)):
        outputlist.append(lst[i] + (lst[i].lower()*i))
    outputlist = '-'.join(outputlist)
    return(outputlist)          
