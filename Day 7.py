def my_cars(array):
    """
    You come to the garage and you see different cars parked there in a straight line.
    All the cars are of different worth.
    You are allowed to choose any amount of cars and they will be yours.
    The only condition is that you can't select  2 cars that are parked beside each other.
    i.e There must be at least one car between any 2 cars you choose.
 
    Given an array where the elements are arranged in order of the cars and the magnitude of each element is the worth of the car,
    the function 'my_cars' takes in the array and returns the maximum worth of cars you can get from the GeekTutor.
    """
    if isinstance(array,list):
        #This checks for errors with input.
        for i in array:
            if not isinstance(i,int):
                raise AssertionError("Invalid input.")
        array1,array2,total = ([] for i in range(3))

        #Checks for numbers that are not side by side and appends them to their correspoding list.
        for i in range(len(array)):
            if i%2==0:
                array1.append(array[i])
            else:
                array2.append(array[i])
        #Adds the two lists to a new list as sublists.
        total.append(array1)
        total.append(array2)
    else:
        raise AssertionError("Invalid input.")

    return sum(max(total, key=sum)) #Returns the sum of the list with the maximum worth.
