#CONSIDERING ONLY LISTS AS ARRAYS
def bubble_sort(my_list):
    """The function 'bubble_sort' takes in an array of integers and sorts the elements of the array using bubble sort algorithm and returns the number of swaps required to sort the array completely."""
    assert type(my_list)==list
    for i in my_list:
        assert type(i)==int
    
    count = 0
    a = len(my_list)
    #This checks through the array of integers and swaps numbers if the number on the left is greater than the one on the right.
    for i in range(0,a-1):
        for j in range(0, a-1-i):
            if my_list[j]>my_list[j+1]:
                my_list[j],my_list[j+1]=my_list[j+1],my_list[j]
                count+=1

    return count
print(bubble_sort([10,9,8,7,6,5,4,3,2,1]))

#CONSIDERING LISTS AND TUPLES AS ARRAYS
def bubble_sort(my_list):
    """The function 'bubble_sort' takes in an array of integers and sorts the elements of the array using bubble sort algorithm and returns the number of swaps required to sort the array completely."""
    assert type(my_list)==list or tuple
    for i in my_list:
        assert type(i)==int
    my_list2 = []
    for i in my_list:
        my_list2.append(i)
    count = 0
    a = len(my_list2)
    #This checks through the array of integers and swaps numbers if the number on the left is greater than the one on the right.
    for i in range(0,a-1):
        for j in range(0, a-1-i):
            if my_list2[j]>my_list2[j+1]:
                my_list2[j],my_list2[j+1]=my_list2[j+1],my_list2[j]
                count+=1

    return count
print(bubble_sort((10,9,8,7,6,5,4,3,2,1)))
print(bubble_sort([10,9,8,7,6,5,4,3,2,1]))
