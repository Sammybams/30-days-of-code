def order(unsorted):
    """
    Given an unsorted array of integers,the function 'order' takes this as parameter and returns a tuple of 2 elements.
    The first element should be the length of the longest consecutive elements sequence and the second, a sorted list of the remaining elements.
    If more than one sequence qualifies the function returns the one with lower values.
    """
    if isinstance(unsorted,list):
        #Checks if there are repeated integers and then returns an error message if there is.
        for i in unsorted:
            if unsorted.count(i)>1:
                raise AssertionError("Invalid input. Only array of unique integers is allowed.")
        #Loops below check for errors with input and if any found returns an error message.
        for i in unsorted:
            if isinstance(i,int):
                unsorted = unsorted
            else:
                raise AssertionError("Invalid input. Only array of unique integers is allowed.")
            
        sorted1 = sorted(unsorted)  #This sorts the inputted array of integers.
        consecutive_list1 = []
        consecutive_list2 = []
        non_consecutive_list = []
        #Checks for consecutive and non-consecutive numbers and adds them to the their corresponding list.
        for i in range(1,len(unsorted)):
            while abs(sorted1[i-1]-sorted1[i])==1:
                consecutive_list1.append(sorted1[i])
                consecutive_list2.append(sorted1[i-1])
                break
            else:
                non_consecutive_list.append(sorted1[i])
                
        main_consecutive_list = sorted(list(set(consecutive_list1)|set(consecutive_list2)))    #Merges all consecutive numbers.
        non_consecutive_list = sorted(list(set(non_consecutive_list)-set(main_consecutive_list))) #Gets the non-consecutive numbers in the array. 

        #Fetches the index(es) of where integers in the sorted array become non-consecutive and adds them to list 'index'. 
        index = []
        for j in range(1, len(main_consecutive_list)):
            while abs(sorted1[j-1]-sorted1[j])!=1:
                index.append(j)
                break
        
        #If index is empty, it returns the provided solution and if not, the inputted array goes through more processing.
        if index==[]:
            return (len(main_consecutive_list),non_consecutive_list)
        else:
            new_list = []
            prev_index = 0
            for l in index:
                new_list.append(main_consecutive_list[prev_index:l])
                prev_index = l
            new_list.append(main_consecutive_list[index[-1]:])

            #Fetches the list with the longest consecutive elements and converts its elements back to integer form.
            maxlist1 = max(new_list, key = len)
            
        #Filters the list containing the longest consecutive elements from the inputted array of integers.  
        main_non_consecutive_list = sorted(list(set(sorted1)-set(maxlist1)))
    else:
        raise AssertionError("Invalid input. Only array of unique integers is allowed.")
    return (len(maxlist1), main_non_consecutive_list)
    
print(order([100,4,200,1,3,2]))
