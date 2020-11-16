def bits_of_gray(n):
    """
    The function 'bits_of_gray' takes in number of bits 'n' as input and returns a list of the gray codes.
    Gray Code system is a binary number system in which every successive pair of numbers differs in only one bit.
    Gray code is common in hardware so that we don't see temporary spurious values during transitions.
    """
    if isinstance(n,int):
        if n<0:
            return "Invalid input. Only positive integers are allowed."
        
        gray1 = []

        #This checks for numbers that differ by one bit in succession and converts them to binary form.
        for i in range(0, 2**n):
            gray=i^(i//2)
            #This adds the binary form to list 'gray1' while keeping the output as a n-digit(s).
            gray1.append(("{0:0{1}b}".format(gray,n)))
    else:
        return "Invalid input."

    return gray1

print(bits_of_gray(2))
print(bits_of_gray(3))
