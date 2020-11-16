def match(list_string):
    """The function 'match' when given a list of words, finds all indices pairs such that the concatenation of the two words is a palindrome."""
    assert type(list_string)==list
    for i in list_string:
        assert type(i)==str
        assert i.isalpha()
    #Loops through all the possible substrings of the list of words to find the word pairs that are palindromes.
    my_match = []
    for i in range(0,len(list_string)):
        for j in range(0,len(list_string)):
            if i!=j:
                a = list_string[i]
                b = list_string[j]
                c = a+b
                d = b+a
                if c==c[::-1]:
                    if (i,j) not in my_match:
                        my_match.append((i,j))
                elif d==d[::-1]:
                    if (j,i) not in my_match:
                        my_match.append((j,i))
    return my_match

def isBalanced(string):
    """
    Given a string comprising of opening parentheses, closing parentheses and asterix(*)
    where * could represent an opening parentheses, closing parentheses or an empty string,
    the function 'isBalanced()' takes in the string and determines if the string is balanced or not.
    It returns True if it is Balanced and False otherwise.
    """
    assert type(string)==str
    if any(a not in '(*)' for a in string):
        raise AssertionError
    string = list(string)   #Converts the inputted list to a string.
    #Loops through the list, checks for opening and closing parentheses and removes them from the list.
    k = 0
    while True:
        if k>=len(string)-1 or len(string)==0:
            break
        if string[k]=='(':
            if ')' in string[k:]:
                b = string[k:].index(')')
                c = string.pop(k)
                d = string.pop(k+b-1)
            else:
                break
        else:
            k+=1
            continue
        
    #Checks if the list is empty and returns True
    if string==[]:
        return True
    #Loops through the list, checks for opening parentheses as '*' and closing parentheses and removes them from the list.
    k = 0
    while True:
        if k>=len(string)-1 or len(string)==0:
            break
        if string[k]=='*':
            if ')' in string[k:]:
                b = string[k:].index(')')
                c = string.pop(k)
                d = string.pop(k+b-1)
            else:
                break
        else:
            k+=1
            continue
        
    #Checks if the list is empty and returns True 
    if string==[]:
        return True
    
    #Loops through the list, checks for opening parentheses and closing parentheses as '*'and removes them from the list.
    k = 0
    while True:
        if k>=len(string)-1 or len(string)==0:
            break
        if string[k]=='(':
            if '*' in string[k:]:
                b = string[k:].index('*')
                c = string.pop(k)
                d = string.pop(k+b-1)
            else:
                break
        else:
            k+=1
            continue
        
    #Checks if the list is empty and returns True
    if string==[]:
        return True
    #Checks if the list contains only asterix and returns True.
    if not any(a not in '*' for a in string):
        return True
    return False
