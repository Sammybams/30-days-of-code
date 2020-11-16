def adder(fraction):
    """The function 'adder' takes in an array of fractions represented as strings and returns the sum of these fractions as a string with the numerator and denominator in their simplest form."""
    assert type(fraction)==list
    for n in fraction:
        if '/' not in n:
            raise AssertionError
    numbers = '0123456789/'
    for o in fraction:
        for p in o:
            if p not in numbers:
                raise AssertionError
    my_list1 = []
    my_list2 = []
    my_list3 = []
    my_list4 = []
    my_list5 = []
    #Separates the numerators from the denominators and adds them to corresponding lists.
    for i in fraction:
        my_list1.append(int(i[0:(i.index('/')):]))
        my_list2.append(int(i[(i.index('/'))+1:]))
    #Checks for zero division error.
    for i in my_list2:
        if i==0:
            raise AssertionError
        
    #Calculates the common denominator the fractions should have.
    LCM = 1
    for j in my_list2:
        LCM*=j
    #Changes the value of the numerator with respect to the common denominator they should share.
    for k in my_list2:
        for l in range(1,LCM+1):
            if k*l==LCM:
                my_list3.append(l)
               
    for m in range(len(my_list1)):
        my_list4.append(my_list1[m]*my_list3[m])
        
    numerator = sum(my_list4)   #Adds the numerators together.
    #Loops through numbers from one to the common denominator and finds the highest common factor of the numerator.
    for p in range(1,LCM+1):
        if LCM%p==0:
            if numerator%p==0:
                my_list5.append(p)
    a = max(my_list5)   #Highest common factor of the numerator.
    b = numerator//a    #New numerator in simplest form
    c = LCM//a          #New denominator in simplest form
    return str(b)+"/"+str(c)

def swap(a,b):
    """The function 'swap' takes in two variables and swaps their contents."""
    assert type(a)==int
    assert type(b)==int

    #Using bitwise XOR to swap numbers.
    a = a^b
    b = a^b
    a = a^b
    
    return a,b
