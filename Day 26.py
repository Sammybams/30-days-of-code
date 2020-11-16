def mergesort(array):
    """The function 'mergesort' takes in an unsorted array and returns a sorted version using the merge sort algorithm."""
    assert type(array)==list
    for m in array:
        assert type(m)==int
    a = len(array)
    #Checks if the length of the list is greater than 1
    if a>1:
        mid = a//2
        #Splits the list into two
        left = array[:mid]
        right = array[mid:]
        #The function calls itself to further split the lists until it has a length of 1
        mergesort(left)
        mergesort(right)
        
        #i = initial index of first subarray
        #j = initial index of second subarray
        #k = initial index of merged subarray
        
        i=j=k=0
        b = len(left)
        c = len(right)
        #Checks for each element in the left and right list, their order and places them in ascending order
        while i<b and j<c:
            if left[i]<right[j]:
                array[k]=left[i]
                i+=1
            else:
                array[k]=right[j]
                j+=1
            k+=1
        #Copies th leftover elements of both lists if there are any.
        while i<b:
            array[k]=left[i]
            i+=1
            k+=1

        while j<c:
            array[k]=right[j]
            j+=1
            k+=1

    return array

def long_pal_index(s,left,right):
    """The function 'long_pal_index' checks for the palindromic substring in a string."""
    left_index = 0
    right_index = 0
    while left>=0 and right<len(s):
        if s[left]==s[right]:
            left_index = left
            right_index = right
        else:
            break

        left-=1
        right+=1
    return s[left_index:right_index+1]

def long_pal(s):
    """Given a string s, the function 'long_pal' finds the longest palindromic substring in s."""
    assert type(s)==str
    assert s.isalpha()
    assert len(s)>=0 and len(s)<=1000
    #Sets the default longest palindromic substring to an empty string.
    largest_pal = ""
    for i in range(len(s)):
        #Checks for the palindromic substring
        pal_Odd = long_pal_index(s,i,i)
        pal_Even = long_pal_index(s,i,i+1)
        #Sets the larger palindromic substring between the left and the right.
        larger_pal = pal_Odd if len(pal_Odd)>len(pal_Even) else pal_Even
        #Sets the largest palindromic substring between the currently known largest and the new larger substring.
        largest_pal = largest_pal if len(largest_pal)>=len(larger_pal) else larger_pal
    #With respect to constraints, it returns None if the length of the longest substring is 1
    #But otherwise returns the string.
    if len(largest_pal)<2:
        return None
    return largest_pal

def factorial(num):
    """The function 'factorial' finds the factorial of a number."""
    fact = 1
    while num>=1:
        fact*=num
        num-=1
    return fact

def probability(f,d,n,oc):
    """
    Given the number of faces on a dice(f), the number of dices thrown(d),
    the desired number(n) and the desired range of occurrence(oc),
    the  function 'probability' returns the probability of n facing up on the dices oc times.
    """
    assert type(f)==int
    assert 5<f<9
    assert type(d)==int
    assert 1<d<20
    assert type(n)==int
    assert 0<n<=f
    assert type(oc)==range
    if list(oc)==[]:
        raise AssertionError
    a = min(oc)
    b = max(oc)
    assert a>=0 and a<=d
    assert b>=0 and b<=d
    prob = 0
    #Using Binomial Probability Distribution
    while a<=b:
        m = factorial(d)/(factorial(d-a)*factorial(a))
        n = (1/f)**a
        o = ((f-1)/f)**(d-a)
        prob+=(m*n*o)
        a+=1
    return round(prob,4)
