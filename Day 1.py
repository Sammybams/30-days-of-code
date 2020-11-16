def average(string):
    """The function 'average' takes in a string of integers as input parameter and returns the average of the numbers."""
    
    try:
        string = string.split() #This splits the numbers separated by space and converts them to a list.

        my_sum = 0
        for i in string:    #This loops through all the numbers in the new list and adds them together.
            my_sum +=int(i)

        my_average = my_sum/len(string) #The average of the numbers are found by dividing their sum by the amount of numbers.
        return round(my_average,2)  #This returns the average of the numbers rounded to two decimal places.

    except:
        return "Invalid input."
    
print(average('12 11 2 6 7 10'))
