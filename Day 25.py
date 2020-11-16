class Vector:
    """Every Vector has an x,y and z co-ordinate."""
    def __init__(self,x,y,z):
        """The Vector constructor takes in 3 integers, the x,y and z coordinates and initializes their values."""
        assert type(x)==int
        assert type(y)==int
        assert type(z)==int
        self.x = x
        self.y = y
        self.z = z

    def info(self):
        """
        The method 'info' returns the vector information as a string in the following form
        'xi+yj+zk', where x,y,and z have their usual meanings.
        """
        a = self.x
        b = self.y
        c = self.z
        if self.y>=0:
            b = "+"+str(self.y)
        if self.z>=0:
            c = "+"+str(self.z)
        return "{}i{}j{}k".format(a,b,c)

    def magnitude(self):
        """The method 'magnitude' calculates the magnitude of the vector and returns its value to 2 decimal places."""
        a = self.x
        b = self.y
        c = self.z
        d = (a**2+b**2+c**2)**(1/2)
        e = round(d,2)
        return e

    def __add__(self,other):
        """Given two vector objects A  and B  the result of A+B will be a new vector object with x,y and z value equal to the sum of that of A and B."""
        assert type(other)==Vector
        a = self.x
        b = self.y
        c = self.z
        d = other.x
        e = other.y
        f = other.z
        g = a+d
        h = b+e
        i = c+f
        vector = Vector(g,h,i)
        return vector

    def __sub__(self,other):
        """Given two vector objects A  and B the result of A-B will be a new vector object with x,y and z value equal to that of A –B."""
        assert type(other)==Vector
        a = self.x
        b = self.y
        c = self.z
        d = other.x
        e = other.y
        f = other.z
        g = a-d
        h = b-e
        i = c-f
        vector = Vector(g,h,i)
        return vector
    
    def __mul__(self,other):
        """
        Given a vector object and a scalar(integer) it returns a vector object with x,y and z equal to the scalar multiplied by the x,y and z coordinates of the original vector.
        Given 2 vector objects, it returns the scalar product of the vectors.
        """
        if type(other)==Vector:
            a = self.x
            b = self.y
            c = self.z
            d = other.x
            e = other.y
            f = other.z
            g = a*d
            h = b*e
            i = c*f
            return g+h+i
        elif type(other)==int:
            a = self.x
            b = self.y
            c = self.z
            d = a*other
            e = b*other
            f = c*other
            vector = Vector(d,e,f)
            return vector
        else:
            raise AssertionError

    def __pow__(self,other):
        """Given two vector objects it returns the cross product of the vector objects which is a new vector object."""
        assert type(other)==Vector
        a = self.x
        b = self.y
        c = self.z
        d = other.x
        e = other.y
        f = other.z
        i = b*f - e*c
        j = -1*(a*f - d*c)
        k = a*e - b*d
        vector = Vector(i,j,k)
        return vector

    def __eq__(self,other):
        """Compares two vectors to determine if they are equal in magnitude. Returns True or False."""
        assert type(other)==Vector
        
        if self.magnitude()==other.magnitude():
            return True
        else:
            return False
A = Vector(2,-5,7)
B = Vector(1,2,3)
print(B.info())
print(A.info())
print(A.magnitude())
C = A+B
print(C.info())
D = B - A
print(D.info())
E = A*2
print(E.info())
F = A*B
print(F)
G = A**B
print(G.info())
H = Vector(3,2,1)
print(H==A)
