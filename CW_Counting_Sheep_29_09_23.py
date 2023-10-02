def count_sheeps(sheep):
    numsheep = 0
    for i in range(len(sheep)):
        if sheep[i] == True:
            numsheep +=1
        else:
            pass
    return numsheep