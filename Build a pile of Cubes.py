def find_nb(m):
    n = 0
    sum = 0
    while sum< m:
        n+=1 
        sum += n**3
        
    if sum == m:
        return n 
    else:
        return -1
