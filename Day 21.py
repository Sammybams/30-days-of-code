def find_neighbor(image,start,pixel):
    """The function 'find_neighbor' checks through possible directions and returns the positions that are in the boundary and are equal to pixel."""
    
    a = start[0]
    b = start[1]
    e = len(image)
    for i in image:
        f = len(i)
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    res = []
    #Checks through the possible directions the pointer can move and finds the location that is equal to pixel.
    for x,y in directions:
        if a+x<0 or b+y<0 or a+x>=e or b+y>=f  or image[a+x][b+y]!=pixel:
            continue
        res.append((a+x,b+y))
    return res

def overflow(image,start,filler,pixel):
    """
    Given an image array, coordinate (x, y) representing the pivot coordinates (row and column) of the flooding,
    the filler and the pivot pixel itself, the function named 'overflow' "floods" the image with the filler.
    _____________________________________________________________
    
    To "flood" an image, starting with the pivot pixel, the value of any pixel that is connected 4-directionally
    and is equal to it is replaced with the filler value as well as the pivot pixel.
    It does this for the surrounding pixels and continues till the image is flooded.
    """
    assert type(image)==list
    for l in image:
        assert type(l)==list
        for m in l:
            assert type(m)==int
    assert type(start)==tuple
    for o in start:
        assert type(o)==int
    assert type(filler)==int
    assert type(pixel)==int
    
    
    a = start[0]
    b = start[1]
    e = len(image)
    
    if image[a][b]!=pixel:
        raise AssertionError
    
    #Loops through possible positions and stores the postions that are connected(as the value of the pixel) in a list.
    directions1 = find_neighbor(image,start,pixel)
    directions2 = find_neighbor(image,start,pixel)
    directions2.append(start)
    
    seen = []
    seen.append(start)
    image[a][b]=filler
    #Loops through the positions we have and check if we have not gone through it before and the finds its connecting neighbours.
    for i in directions1:
        if i not in seen:
            seen.append(i)
            for j in find_neighbor(image,i,pixel):
                directions1.append(j)
                directions2.append(j)
    #Loops through the positions of all the connecting neighbours and our start and changes their value to the filler.
    for i in directions2:
        image[i[0]][i[1]]=filler
    return image
