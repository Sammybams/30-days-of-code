def resolve(d,my_list):
    """
    The function 'resolve' takes in a list of tokens(strings, integers or a combination) and a dictionary from token to token.
    It resolves each token and returns a list of the resolved tokens in the same order.
    """
    new_list = []
    j=0
    #Loops through each character in the inputted list
    for m in my_list:
        i = m
        #Loops through the inputted dictionary, resolves each token and adds them to the list 'new_list'.
        while i in d:
            i = d[i]
            if i==m:
                break
        new_list.append(i) 
    return new_list

def bin(list1,list2):
    """
    The function 'bin' takes in a list of integers and a list of the lower limit of bins as parameters.
    It then returns the number of elements in each bin as a list.
    """
    #Returns results for inputs of empty lists.
    if list1==[]:
        return [0]*len(list2)
    if list2==[]:
        return  []
    #Check for errors in our input and raises Assertion Error.
    for i in list1:
        if not isinstance(i,int):
            raise AssertionError
        if i<0:
            raise AssertionError
    for i in list2:
        if not isinstance(i,int):
            raise AssertionError
        if i<0:
            raise AssertionError
    else:
        #Checks if input have contrasting ranges and raises AssertionError
        if max(list2)>max(list1):
            raise AssertionError
        
        new_list = []
        prev_index = list1.index(list2[0])
        #Breaks the inputted list of integers into sublists according to the lower limits in the second input.
        for i in range(1,len(list2)):
            j=0
            if list2[i] in list1:
                new_list.append(list1[prev_index:(list1.index(list2[i]))])
                prev_index = list1.index(list2[i])
            else:
                j=0
                y = list2[i]
                while j>=0 and y not in list1:
                    j+=1
                    y = y+j
                    continue
                new_list.append(list1[prev_index:(list1.index(y))])
        #Checks if all lower limits are in the list of integers or not and finds the corresponding last range.
        if set(list2)&set(list1)==set(list2):
            b = len(list(range(list2[-1],list1[-1]+1)))
        else:
            b = len(list(range(y,list1[-1]+1)))
        #Adds all the numbers in ranges but the last range.
        a_list = []
        for k in new_list:
            for l in k:
                if l in list1:
                    a_list.append(l)
        #Calculates the number in each bin and adds it to the list 'b_list'
        b_list = []
        for m in new_list:
            b_list.append(len(set(m)&set(a_list)))
        b_list.append(b)
                    
        return b_list
