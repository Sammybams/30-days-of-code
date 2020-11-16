def selection(my_list):
    """The function 'selection' takes in a list as input and returns the rearranged version of the list."""
    assert type(my_list)==list
    for i in my_list:
        assert type(i)==int
    #Loops through the length of the list and checks for the last number in the list that is greater than the first lowest number encountered and then swaps their positions.
    for i in range(len(my_list)):
        b = i
        for j in range(i+1,len(my_list)):
            if my_list[b]>my_list[j]:
                b = j
        my_list[i], my_list[b] = my_list[b], my_list[i]
    return my_list  #Returns the rearranged list.

def short_sub(string, my_set):
    """
    Given a string and a set of characters, the function named 'short_sub' returns the shortest substring
    containing all the characters in the set.
    """
    no_of_chars = 256
    assert type(string)==str
    assert type(my_set)==set
    for i in my_set:
        assert type(i)==str
    pat = []
    for i in my_set:
        pat.append(i)
    len1 = len(string)  
    len2 = len(pat)  
  
    #Checks if string's length is less than pattern's length and raises AssertionError.
    if len1 < len2:
        raise AssertionError
  
    seen_path = [0] * no_of_chars 
    seen_str = [0] * no_of_chars  
  
    #Stores occurrences of characters of pattern. 
    for i in range(0, len2):  
        seen_path[ord(pat[i])] += 1
  
    start, start_index, min_len = 0, -1, float('inf')  
  
    #Loops through the string
    count = 0  
    for j in range(0, len1):  
      
        #Counts the occurrences of characters of string.
        seen_str[ord(string[j])] += 1

        #If the string charcater matches the set of characters it counts with an increment of 1.
        if (seen_path[ord(string[j])] != 0 and seen_str[ord(string[j])] <=seen_path[ord(string[j])]):  
            count += 1
  
        #If all characters have been matched, it minimizes the length of the match by removing unwanted characters.
        if count == len2:  
          
            while (seen_str[ord(string[start])] > seen_path[ord(string[start])] or seen_path[ord(string[start])] == 0):  
              
                if (seen_str[ord(string[start])] > seen_path[ord(string[start])]):  
                    seen_str[ord(string[start])] -= 1
                start += 1
              
            #Updates the size of the matched characters.
            length_of_window = j - start + 1
            if min_len > length_of_window:  
              
                min_len = length_of_window  
                start_index = start  
  
    #If there is no match it raises assertion error.  
    if start_index == -1: 
        raise AssertionError 
 
    return string[start_index : start_index + min_len]  
