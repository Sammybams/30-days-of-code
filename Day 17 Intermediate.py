
def power_list(s):
    """The function 'power_list' takes in a list as parameter and returns its powerlist."""
    my_list = [[]]
    for i in s:
        my_subset = [subset + [i] for subset in my_list]
        my_list.extend(my_subset)
    return my_list

def power_list_sum(s):
    """The function 'power_list' takes in a list as parameter and returns its powerlist."""
    x = len(s)
    my_list = []
    for i in range(1 << x):
        my_list.append(sum(([s[j] for j in range(x) if (i & (1 << j))])))

    return sorted(my_list)
def combo(N,K):
    """The function 'combo' takes in a list of N integers and a positive integer K and returns a list of all combinations of K elements in the list."""
    assert type(N)==list
    assert type(K)==int
    for k in N:
        assert type(k)==int
    assert K>0 and K<=len(N)
    
    main_combo = []
    #Finds the power list of the inputted list and loops through the power list for lists with length 'K'.
    for l in power_list(N):
        if len(l)==K:
            main_combo.append(l)
    return main_combo   #Returns a list of list combinations with length 'K'.

def search_for_money(a,b,c,d):
    if c>=b:
        mid = b + (c-b)//2
        if a[mid]==d:
            return 1
        elif a[mid]>d:
            return search_for_money(a,b,mid-1,d)
        else:
            return search_for_money(a,mid+1,c,d)
    else:
        return -1

def my_money(money):
    """Given an array of integers where the integers represent the naira notes Geek gave you guys, the function my_money() takes the array of the notes worth and returns a boolean if its possible to share the money into exactly half only with the naira notes Geek gave you."""
    assert type(money)==list
    for m in money:
        assert type(m)==int
    #Calculates the half of the sum of the inputted array of integers.
    half = sum(money)/2
    new_money_combo = power_list_sum(money)
    b = len(new_money_combo)-1
    a = search_for_money(new_money_combo,0,b,half)
    if a==1:
        return True
    else:
        return False

'''
MAKE A CONSTRAINT TO CHECK IF THE LENGTH OF THE INPUTTED STRING IS GREATER
THAN 30, THEN SET IT TO TRUE OR FALSE.
'''
print(my_money([5,50,100,10]))
end = time.time()
print(end - start)
print(my_money([1000,500,500]))
end = time.time()
print(end - start)
print(my_money([5, 5, 10, 100, 100, 200, 200, 500, 500, 1000,500,200,100,5,10,5,10,100,1000,500,200,300,50,5,10,20]))
end = time.time()
print(end - start)
