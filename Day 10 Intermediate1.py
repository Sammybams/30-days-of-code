class Student:
    """The class 'Student' takes an object which has an age, weight and height."""
    def __init__(self,age,weight,height):
        """The constructor takes in 3 parameters, a student's age, weight and height and initializes them to those values."""
        self.age = age
        self.weight = weight
        self.height = height
        if not (isinstance(self.age,int)):
            raise AssertionError
        if not (isinstance(self.weight,float)):
            raise AssertionError
        if not (isinstance(self.height,float)):
            raise AssertionError
        if self.weight<0:
            raise AssertionError
        if self.age<0:
            raise AssertionError
        if self.height<0:
            raise AssertionError
        

    def info(self):
        """
        Function 'info' when called returns a tuple containing the age and Body Max Index(BMI)(rounded to 2dp) of the student.
        BMI=weight/(height**2)
        """
        a = self.age
        b = self.weight
        c = self.height
        if not (isinstance(a,int)):
            raise AssertionError
        if not (isinstance(b,float)):
            raise AssertionError
        if not (isinstance(c,float)):
            raise AssertionError
        if a<0:
            raise AssertionError
        if b<0:
            raise AssertionError
        if c<0:
            raise AssertionError
        z = round(b/(c**2),2)
        return (a,z)

def average(my_list):
    """The function 'average' takes a list of student objects and when called returns a tuple containing the average age,weight and height(in that order) of the students in the next 10 years(Assuming that weight increases by 5% each year and height increases by 2% each year)."""
    new_age = []
    new_weight = []
    new_height = []

    for i in my_list:
        if not (isinstance(i.age,int)):
            raise AssertionError
        if not (isinstance(i.weight,float)):
            raise AssertionError
        if not (isinstance(i.height,float)):
            raise AssertionError
        if i.age<0:
            raise AssertionError
        if i.weight<0:
            raise AssertionError
        if i.height<0:
            raise AssertionError
        new_age.append(i.age+10)
        new_weight.append(round(i.weight*(1.05**10),2))
        new_height.append(round(i.height*(1.02**10),2))

    average_new_age = round(sum(new_age)/len(new_age),2)
    average_new_weight = round(sum(new_weight)/len(new_weight),2)
    average_new_height = round(sum(new_height)/len(new_height),2)
    return (average_new_age,average_new_weight,average_new_height)
    
Fortune=Student(23,45.67,7.6)
print(Fortune.info())
Joba=Student(22,40.01,8.3)
print(average([Fortune,Joba]))
