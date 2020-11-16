def insertion(a_list):
    """The function 'insertion' takes in a list of integers or strings (never a combination) and returns the sorted list."""
    #The loops below check for errors with input.
    check1 = []
    check2 = []
    assert type(a_list)==list
    for i in a_list:
        if type(i)==str:
            check1.append(1)
        elif type(i)==int:
            check2.append(1)
        else:
            raise AssertionError
    if check1!=[] and check2!=[]:
        raise AssertionError
    #Checks if the number before another number in the inputted list is greater and
    #then inserts the lesser number in the position of the greater number and viceversa.
    for m in range(1,len(a_list)):
        cur = a_list[m]
        position = m
        while position>0 and a_list[position-1]>cur:
            a_list[position]=a_list[position-1]
            position-=1

        a_list[position]=cur
    return a_list   #returns the sorted list

def biggie(array,index1):
    """
    Given an array of numbers and an index i,
    the function 'biggie' returns the index of the nearest number greater than the number at index i,
    where distance is measured in array indices.
    """
    assert type(array)==list
    assert type(index1)==int
    assert index1>=0 and index1<len(array)
    for m in array:
        assert type(m)==int
    if max(array)==array[index1]:
        raise AssertionError
    
    my_list1 = []
    #Checks for numbers in the inputted array greater than the number at the inputted index.
    for i in array:
        if i>array[index1]:
            my_list1.append(i)
    my_list2 = []
    #Gets the indexes of the numbers greater than the number at the inputted index.
    for j in my_list1:
        my_list2.append(array.index(j))

    #Gets the distance between the inputted index and the indexes of the numbers greater than the number at the inputted index.
    my_list3 = []
    my_list4 = []
    for k in my_list2:
        if k>index1:
            my_list3.append(k-index1)
        else:
            my_list4.append(k-index1)
    #Checks if the numbers greater are towards the right or  left and returns the appropriate index of the nearest number greater.
    if my_list3==[]:
        return max(my_list4)+index1
    else:
        a = min(my_list3)
    if my_list4==[]:
        return min(my_list3)+index1
    else:
        b = max(my_list4)
    #Checks if the distance from the inputted index and the numbers greater are equal, greater  or less than each other and then
    #returns the appropriate index of the nearest number greater.
    if abs(b)>a:
        return a+index1
    elif abs(b)==a:
        return b+index1 or a+index1
    else:
        return b+index1
