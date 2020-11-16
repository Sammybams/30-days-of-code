def leftedge(matrix1,tuple1,tuple2):
    a = tuple1[0]
    b = tuple1[1]
    c = tuple2[0]
    d = tuple2[1]
    e = matrix[a]
    f = e[b]
    g = matrix[c]
    h = g[d]
    new_k = []
    if f==0:
        raise AssertionError
    count = []
    if b==0:
        if a==0:
            if matrix[1][0]==1: 
                count.append(1)
                new_k.append((1,0))
                k =new_k[0]
            elif matrix[0][1]==1:
                count.append(1)
                new_k.append((0,1))
                k =new_k[0]
            else:
                raise AssertionError
        elif a==(len(matrix)-1):
            if matrix[len(matrix)-2][0]==1:
                count.append(1)
                new_k.append((len(matrix)-2,0))
                k =new_k[0]
            elif matrix[(len(matrix)-1)][1]==1:
                count.append(1)
                new_k.append((len(matrix)-1,1))
                k =new_k[0]
            else:
                raise AssertionError
        else:
            if matrix[a-1][0]==1:
                count.append(1)
                new_k.append((a-1,0))
                k =new_k[0]
            elif matrix[a+1][0]==1:
                count.append(1)
                new_k.append((a+1,0))
                k =new_k[0]
            elif matrix[a][1]==1:
                count.append(1)
                new_k.append((a,1))
                k =new_k[0]
            else:
                raise AssertionError
    else:
        k = tuple1
    return [k,sum(count)]
matrix = [[1, 0, 1, 1],[1, 0, 1, 0],[1, 1, 1, 0],[1, 1, 1, 0]]
print(leftedge(matrix,(0,0),(0,3)))
def rightedge(matrix,k,tuple2):
    a = tuple1[0]
    b = tuple1[1]
    c = tuple2[0]
    d = tuple2[1]
    e = matrix[a]
    f = e[b]
    g = matrix[c]
    h = g[d]
    if f==0:
        raise AssertionError
    count = []
    new_k = []
    if b==(len(matrix)-1):
        if a==0:
            if matrix[0][len(matrix)-2]==1:
                count.append(1)
                new_k.append((0,len(matrix)-2))
                k =new_k[0]
            elif matrix[1][len(matrix)-1]==1:
                count.append(1)
                new_k.append((1,len(matrix)-1))
                k =new_k[0]
            else:
                raise AssertionError
        elif a==(len(matrix)-1):
            if matrix[len(matrix)-2][len(matrix)-1]==1:
                count.append(1)
                new_k.append((len(matrix)-2,len(matrix)-1))
                k =new_k[0]
            elif matrix[(len(matrix)-1)][len(matrix)-2]==1:
                count.append(1)
                new_k.append((len(matrix)-1,len(matrix)-2))
                k =new_k[0]
            else:
                raise AssertionError
        else:
            if matrix[a-1][len(matrix)-1]==1:
                count.append(1)
                new_k.append((a-1,len(matrix)-1))
                k =new_k[0]
            elif matrix[a+1][len(matrix)-1]==1:
                count.append(1)
                new_k.append((a+1,len(matrix)-1))
                k =new_k[0]
            elif matrix[a][len(matrix)-2]==1:
                count.append(1)
                new_k.append((a,len(matrix)-2))
                k =new_k[0]
            else:
                raise AssertionError
    else:
        k = tuple1
    
    return [k,sum(count)]
def topedge(matrix,k,tuple2):
    a = tuple1[0]
    b = tuple1[1]
    c = tuple2[0]
    d = tuple2[1]
    e = matrix[a]
    f = e[b]
    g = matrix[c]
    h = g[d]
    new_k = []
    if f==0:
        raise AssertionError
    count = []
    if a==0:
        if b!=(0 or len(matrix)-1):
            if matrix[0][b-1]==1:
                count.append(1)
                new_k.append((0,b-1))
                k =new_k[0]
            elif matrix[0][b+1]==1:
                count.append(1)
                new_k.append((0,b+1))
                k =new_k[0]
            elif matrix[1][b]==1:
                count.append(1)
                new_k.append((1,b))
                k =new_k[0]
            else:
                raise AssertionError
        else:
            k = tuple1
    else:
        k = tuple1
    
    return [k,sum(count)]
def bottomedge(matrix,k,tuple2):
    a = tuple1[0]
    b = tuple1[1]
    c = tuple2[0]
    d = tuple2[1]
    e = matrix[a]
    f = e[b]
    g = matrix[c]
    h = g[d]
    if f==0:
        raise AssertionError
    count = []
    if a==len(matrix)-1:
        if b!=(0 or len(matrix)-1):
            if matrix[len(matrix)-1][b-1]==1:
                count.append(1)
                new_k.append((len(matrix)-1,b-1))
                k =new_k[0]
            elif matrix[len(matrix)-1][b+1]==1:
                count.append(1)
                new_k.append((len(matrix)-1,b+1))
                k =new_k[0]
            elif matrix[len(matrix)-2][b]==1:
                count.append(1)
                new_k.append((len(matrix)-2,b))
                k =new_k[0]
            else:
                raise AssertionError
        else:
            k = tuple1
    else:
        k = tuple1
     
    return [k,sum(count)]
def middle(matrix,k,tuple2):
    a = tuple1[0]
    b = tuple1[1]
    c = tuple2[0]
    d = tuple2[1]
    e = matrix[a]
    f = e[b]
    g = matrix[c]
    h = g[d]
    if f==0:
        raise AssertionError
    if matrix[a][b-1]==1:
        count.append(1)
        new_k.append((a,b-1))
        k = new_k[0]
    elif matrix[a][b+1]==1:
        count.append(1)
        new_k.append((a,b+1))
        k = new_k[0]
    elif matrix[a-1][b]==1:
        count.append(1)
        new_k.append((a-1,b))
        k = new_k[0]
    elif matrix[a+1][b]==1:
        count.append(1)
        new_k.append((a+1,b))
        k = new_k[0]
    else:
        raise AssertionError
    return [k,sum(count)]

def pathfinder(matrix,tuple1,tuple2):
    """
    The function 'pathfinder' takes in the 2D plane (a square matrix represented as a list of lists), a tuple containing coordinates of the start point and a tuple containing coordinates of the destination.
    The function returns an integer representing the lowest number of steps required to reach the destination.
    The 2D plane will be a matrix of zeroes and ones where 1s are pathways and 0s are obstacles. 
    """
    my_count = []
    k = tuple1
    while k!=tuple2:
        if leftedge(matrix,k,tuple2)!=[k,0]:
            k = leftedge(matrix,k,tuple2)[0]
            my_count.append(leftedge(matrix,k,tuple2)[1])
        elif rightedge(matrix,k,tuple2)!=[k,0]:
            k = rightedge(matrix,k,tuple2)[0]
            my_count.append(rightedge(matrix,k,tuple2)[1])
        elif topedge(matrix,k,tuple2)!=[k,0]:
            k = topedge(matrix,k,tuple2)[0]
            my_count.append(topedge(matrix,k,tuple2)[1])
        elif bottomedge(matrix,k,tuple2)!=[k,0]:
            k = bottomedge(matrix,k,tuple2)[0]
            my_count.append(bottomedge(matrix,k,tuple2)[1])
        elif middle(matrix,k,tuple2)!=[k,0]:
            k = middle(matrix,k,tuple2)[0]
            my_count.append(middle(matrix,k,tuple2)[1])
        else:
            raise AssertionError
        k = k
        
    return sum(my_count)
matrix = [[1, 0, 1, 1],[1, 0, 1, 0],[1, 1, 1, 0],[1, 1, 1, 0]]
print(pathfinder(matrix,(0,0),(0,3)))
