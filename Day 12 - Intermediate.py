def find_neighbor(matrix,start):
    """The function 'find_neighbor' checks through possible directions and returns the positions that are in the boundary and are equal to 1."""
    
    a = start[0]
    b = start[1]
    e = len(matrix)
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    res = []
    for x,y in directions:
        if a+x<0 or b+y<0 or a+x>=e or b+y>=e  or matrix[a+x][b+y]==0:
            continue
        res.append((a+x,b+y))
    return res

def pathfinder(matrix,start,stop):
    """
    The function 'pathfinder' takes in the 2D plane (a square matrix represented as a list of lists), a tuple containing coordinates of the start point and a tuple containing coordinates of the destination.
    The function returns an integer representing the lowest number of steps required to reach the destination.
    """
    assert type(matrix)==list
    assert type(start)==tuple
    assert type(stop)==tuple
    
    for m in matrix:
        for n in m:
            if n!=0 and n!=1:
                raise AssertionError
    a = start[0]
    b = start[1]

    c = stop[0]
    d = stop[1]
    e = len(matrix)
    
    if matrix[a][b]==0 or matrix[c][d]==0:
        raise AssertionError
    #Loops through possible positions and counts the number of steps until it reaches the destination.
    queue = []
    seen = set()
    seen.add(start)
    queue.append(start)
    total = -1
    while len(queue):
        total+=1
        for _ in range(len(queue)):
            cur = queue.pop(0)
            if cur == stop:
                return total
            neighbors = find_neighbor(matrix,cur)
            for i in neighbors:
                if i not in seen:
                    seen.add(i)
                    queue.append(i)

    return 0
matrix = [
          [1, 0, 1, 1],
          [1, 0, 1, 0],
          [1, 1, 1, 0],
          [1, 1, 1, 0]]
print(pathfinder(matrix,(0,0),(0,3)))
matrix2 =  [
    [1, 1, 1, 0, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 1, 1],
    [1, 0, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 1],
    [1, 0, 0, 1, 1, 0, 1, 0],
    [0, 0, 0, 1, 1, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 0, 1]]
print(pathfinder(matrix2,(2,3),(3,7)))
matrix3 = [[1,1,1],[0,0,1],[0,0,1]]
print(pathfinder(matrix3,(0,0),(2,2)))
