def rotate(array):
    """The function 'rotate' when given a square 2-D array of integers rotates the array 90° clockwisely."""
    assert type(array)==list
    for m in array:
        assert type(m)==list
        for n in m:
            assert type(n)==int
    for g in range(len(array)):
        if len(array)!=len(array[g]):
            raise AssertionError
    
    a = len(array)
    #Loops through the matrix and swaps the numbers at the edges clockwisely.
    for i in range(a//2):
        for j in range(i,a-i-1):
            b = array[i][j]
            array[i][j] = array[a-1-j][i]
            array[a-1-j][i] = array[a-1-i][a-1-j]
            array[a-1-i][a-1-j] = array[j][a-1-i]
            array[j][a-1-i] = b
    return array

def loop_read(my_array):
    """The function 'loop_read' takes in a 2D array and returns a string containing all the elements starting from top left element and going in a round loop."""
    assert type(my_array)==list
    check1 = []
    check2 = []
    for b in my_array:
        assert type(b)==list
        for c in b:
            if type(c)==str:
                check1.append(1)
            elif type(c)==int:
                check2.append(1)
            else:
               raise AssertionError
    if check1!=[] and check2!=[]:
       raise AssertionError
    if my_array==[]:
        raise AssertionError
    string = []
    e = len(my_array)
    for i in my_array:
        f = len(i)
    x = 0
    y = 0
    
    #Loops through the 2D array and copies it's elements to a list 'string'.
    while (x<e) and (y<f):
        #Moves towards the right and copies its elements
        for p in range(y,f):
            string.append(str(my_array[x][p]))
            
        #Moves downwards and copies its elements
        x+=1
        for q in range(x,e):
            string.append(str(my_array[q][f-1]))
            
        #Moves towards the left and copies its elements
        f-=1
        if x<e:
            for r in range(f-1,y-1,-1):
                string.append(str(my_array[e-1][r]))
                
        #Moves upwards and copies its elements
            e-=1
        if y<f:
            for s in range(e-1,x-1,-1):
                string.append(str(my_array[s][y]))
                
            y+=1
    #Joins the elements of the list 'string' separated by spaces.     
    return " ".join(string)
    
print(loop_read([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]))
