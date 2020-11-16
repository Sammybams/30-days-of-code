def itos(num):
    """The function 'itos' takes in an integer as input parameter and converts it to a string."""

    if isinstance(num,int):
        #Checks for negative numbers and raises an error.
        if num<0:
            raise ValueError
        
        int_to_str = {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9'}

        #Adds each digit of the input to a list.
        string_form1 = []
        if num!=0:
            while num!=0:
                string_form1.append(num%10)
                num = num//10
        else:
            string_form1 = [0]
            
        #Converts the integers in the list to strings by comparing each of its digits to dictionary(int_to_str).
        string_form2 = []
        for i in string_form1:
            string_form2.append(int_to_str[i])

        #Joins the items(strings) of the list together.
        string_form3 = "".join(string_form2)
        string_form3 = string_form3[::-1]
    else:
         raise ValueError
        
    return string_form3
        
print(itos(12))
print(type(itos(12)))
   
def stoi(string1):
    """The function 'stoi' takes in a string of integer as input parameter and converts it to an integer."""

    if isinstance(string1,str):
        #The loops below are to check for errors with input.
        for i in string1:
            if not i.isdigit():
                raise ValueError
            
        #Converts each character in string to integer and adds it to a list after comparing it with dictionary(str_to_int). 
        str_to_int = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        int_form = []
        for i in string1:
            int_form.append(str_to_int[i])

        #Adds up the numbers after multiplying them by their corresponding units(powers of 10).
        int_form = sum(a*10**b for b, a in enumerate(int_form[::-1]))
    else:
        raise ValueError
    
    return int_form     #Returns the sum which is the value of the input in integer form.
    
print(stoi('11'))
print(type(stoi('11')))

def ftos(num1):
    """The function 'ftos' takes in a float as input parameter and converts it to a string."""
    if isinstance(num1,float):
        #Checks for negative numbers and raise an error.
        if num1<0:
            raise ValueError

        m = round(num1,0)
        n = num1 - m
        n1 = num1 - m
        n2 = num1 - m
        count=0
        i=10
        #This counts how many decimal places has the float.
        while i<=10 and not n.is_integer():
            count+=1
            n*=10
            i-=1
            if n.is_integer():
                break
            else:
                n1*=10
                n = round(n1,i)
            continue
        
        n = n2*10**count     #This converts the decimal part of the float to a whole number.

        #Concatenation of whole number part and decimal part separated by a dot after applying function 'itos' to them.
        float_to_string = itos(round(m)) + '.'+ itos(round(n))
        
    else:
        raise ValueError

    return float_to_string

print(ftos(24.12))
print(type(ftos(24.12)))

def stof(string2):
    """The function 'stof' takes in a string of float as input parameter and converts it to an integer."""
    if isinstance(string2,str):
        
        #The loops below are to check for errors with input.
        if not '.' in string2:
            raise ValueError
        if string2.count('.')>1:
            raise ValueError
        for i in string2:
            if i.isalpha():
                raise ValueError
        
        str_to_float = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}

        a = string2.index('.')
        b = string2[:a] #filters the whole number part.
        c = string2[a+1:]   #filters the decimal part.

        #Converts each character in decimal part to integer and adds it to a list after comparing it with dictionary(str_to_float). 
        float_form2 = []
        for j in c:
            float_form2.append(str_to_float[j])
        #Adds up the numbers after multiplying them by their corresponding units(powers of 10).  
        float_form2 = sum(c*10**(-(d+1)) for d, c in enumerate(float_form2))

        #After using function 'stoi' to get the whole number part, it is then added to the float form of the decimal part.
        final_float_form = stoi(b) + float_form2
    else:
        raise ValueError
    
    return final_float_form     #Returns the sum which is the value of the input in float form.

print(stof('12.34'))
print(type(stof('12.34')))
