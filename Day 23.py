def check_right_diagonals(image,start):
    """
    The function 'check_right_diagonals' checks if the diagonals in a matrix
    from the inputted start point to the end of the matrix towards the right are equal to 1
    and returns a list containing tuples of their positions.
    """
    a = start[0]
    b = start[1]
    e = len(image)
    for m in image:
        f = len(m)
    x = 1
    y = 1
    res = []
    if a+x<0 or b+y<0 or a+x>=e or b+y>=f:
        return res
    while image[a+x][b+y]==1:
        res.append((a+x,b+y))
        x+=1
        y+=1
        if a+x<0 or b+y<0 or a+x>=e or b+y>=f:
            break
    return res

def check_left_diagonals(image,start):
    """
    The function 'check_left_diagonals' checks if the diagonals in a matrix
    from the inputted start point to the end of the matrix towards the left are equal to 1
    and returns a list containing tuples of their positions.
    """

    a = start[0]
    b = start[1]
    e = len(image)
    for m in image:
        f = len(m)
    x = 1
    y = -1
    res = []
    if a+x<0 or b+y<0 or a+x>=e or b+y>=f:
        return res
    while image[a+x][b+y]==1:
        res.append((a+x,b+y))
        x+=1
        y-=1
        if a+x<0 or b+y<0 or a+x>=e or b+y>=f:
            break
    return res

def my_exes(matrix,thresh=None):
    """
    The function 'my_exes' takes in a binary 2-D matrix a and an optional parameter thresh
    which represents the highest order to be considered and has a default value of None
    and  returns the number of Xs in the 2-D matrix as an integer.
    _____________________________________________________________
    
    If thresh is None the total number of X's from all possibilities should be returned
    else it represents the maximum dimension to be considered.
    """
    assert type(matrix)==list
    for m in matrix:
        assert type(m)==list
        for n in m:
            assert type(n)==int
            if n!=0 and n!=1:
                raise AssertionError
    if thresh!=None:
        assert type(thresh)==int
        assert thresh>0 and thresh<=len(matrix)-1
    if len(matrix)<=1:
        raise AssertionError
    
    e = len(matrix)
    for m in matrix:
        f = len(m)
    #Loops through the 2-D matrix and finds the positions of all its elements before the last row.
    locations_to_check = []
    for i in range(e):
        for j in range(f):
            locations_to_check.append((i,j))
        if i==e-2:
            break
    #Loops through the positions in the 2-D matrix and finds the X's that are present based on the thresh provided.
    thresh2 = []
    for w in locations_to_check:
        #Checks if the element in each position is equal to 1 and finds it right diagonals.
        if matrix[w[0]][w[1]]==1:
            x = check_right_diagonals(matrix,w)
            if x==[]:
                continue
            #Checks the corresponding left diagonal of the initial position
            for y in x:
                z = (w[0],y[1])
                if matrix[z[0]][z[1]]==0:
                    continue
                o = check_left_diagonals(matrix,z)
                if o==[]:
                    continue
                #Checks if the positions supposedly form a square and meets the thresh value criteria
                #then adds them to a list 'thresh2'
                for p in o:
                    if p[0]==y[0] and thresh==None:
                        thresh2.append(p)
                    elif p[0]==y[0] and (y[0]-w[0])<=thresh:
                        thresh2.append(p)
    '''                 
    for w in locations_to_check:
        #Checks if the element in each position is equal to 1 and finds it right diagonals.
        if matrix[w[0]][w[1]]==1:
            if w[1]!=0 and w[1]!=e-1 and w[0]<=e-3:
                if matrix[w[0]+1][w[1]-1]==1 and matrix[w[0]+1][w[1]+1]==1 and matrix[w[0]+2][w[1]]==1:
                    thresh2.append(1)
    '''
    #The length of the list 'thresh2' is equal to the number of X's in the 2-D matrix.
    return len(thresh2)
print(my_exes([
    [1,0,1,0,1],
    [0,1,0,1,0],
    [1,0,1,0,1],
    [0,1,0,1,0],
    [1,0,1,0,1]]))
