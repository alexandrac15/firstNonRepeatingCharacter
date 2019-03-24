



def function(s):
    occ=dict()

    for char in s:
        if char  in occ:
           occ[char]+=1
        else:
            occ[char]=1

    for char in occ:
        if occ[char]==1:
            return char





