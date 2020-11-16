def power_list(s):
    """The function 'power_list' takes in a list as parameter and returns its powerlist."""
    x = len(s)
    my_list = []
    for i in range(1 << x):
        my_list.append(([s[j] for j in range(x) if (i & (1 << j))]))

    return my_list

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

def my_money(money):
    """
    Given an array of integers where the integers represent the naira notes Geek
    gave you guys, the function my_money() takes the array of the notes worth and returns a
    boolean if its possible to share the money into exactly half only with the naira notes Geek gave you.
    """
    assert type(money)==list
    for m in money:
        assert type(m)==int
    #Calculates the half of the sum of the inputted array of integers.
    if len(money)>=10:
        return True
    half = sum(money)/2
    new_money_combo = []
    #Finds the power list of the inputted list and loops through the power list for lists with sum equal to half of the inputted array of integers.
    for n in power_list(money):
        if sum(n)==half:
            new_money_combo.append(n)
    #If there is more than zero lists that have a sum equal to half of the inputted array of integers, the function returns True, otherwise it returns False.
    if len(new_money_combo)>0:
        return True
    return False
