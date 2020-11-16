def to_base(decimal,desired):
    """The function 'to_base' takes in a decimal integer and the desired base(in integer form i.e 2,4,8 or 16) as parameters and returns the converted number as a string."""
    #Checks if input 'decimal' is not an integer and raises Assertion Error.
    if not isinstance(decimal,int):
            raise AssertionError("Invalid input. Only integers are allowed as input.")
        
    conversion = []
    '''
    Loops check if desired base is 2,4,8 or 16 and converts the inputted decimal integer to the corresponding base.
    If the desired base is not 2,4,8 or 16 it raises an Assertion Error.
    '''
    if desired==2:
        while decimal!=0:
            conversion.append(str(decimal&(desired-1)))
            decimal = decimal>>1
            continue
    elif desired==4:
        while decimal!=0:
            conversion.append(str(decimal&(desired-1)))
            decimal = decimal>>2
            continue
    elif desired==8:
        while decimal!=0:
            conversion.append(str(decimal&(desired-1)))
            decimal = decimal>>3
            continue
    elif desired==16:
        while decimal!=0:
            hexadecimal = {0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}
            conversion.append(str(hexadecimal[decimal&(desired-1)]))
            decimal = decimal>>4
            continue
    else:
        raise AssertionError("Invalid input for desired base.")
    output = ("".join(conversion))[::-1]    #Joins the list of remainders in desired base and reverses it.
    return output

import pandas
