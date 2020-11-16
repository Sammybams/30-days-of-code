def termino(string):
    """The function named 'termino' takes in a string of parentheses and returns the minimum number of parentheses to be removed to make the string valid as an integer."""

    #Checks if input includes characters other than parenthese and prints an error message.
    if isinstance(string,str):
        #Checks if there is any character other than parentheses in input(string) and if there is, returns an error message.
        if any(a not in '()' for a in string):
            return "Invalid input. Only string of parentheses are allowed as input."

        #Checks if there are no closing pairs of parentheses in the string and returns the length of the string as output.
        if '()' not in string:
            return len(string)

        #Checks for closing pairs of parentheses and removes them from the string.
        while '()' in string:
            new_string = string.split('()')
            num_unmatched = "".join(new_string)
            break

        return len(num_unmatched)  #Returns the number of unmatched parentheses.
    else:
        return "Invalid input. Only string of parentheses are allowed as input."

print(termino('()())()'))
print(termino('((()))'))
print(termino(')('))
