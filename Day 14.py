class Node:
    """In the class 'Node', every node has a value (integer)  and a next(type Node)."""
    def __init__(self, value):
        assert type(value)==int
        self.value = value
        self.next = None

class Queue:
    """In the class 'Queue', every queue has a parameter head(type Node)."""
    def __init__(self):
        self.head = None

    def enqueue(self,value):
        """The function 'enqueue' adds the parameter 'value' to the end of the queue."""
        assert type(value)==int
        a = Node(value)
        if self.head is None:
            self.head = a
        else:
            m = self.head
            while m.next:
                m = m.next
            m.next = a

    def dequeue(self):
        """The function 'pop' removes the first element in the queue and returns the element removed."""
        c = self.head
        d = self.head
        if self.head==None:
            raise AssertionError
        else:
            self.head = c.next
            c = None
            return d.value

    def front(self):
        """The function 'front' returns the first element in the queue."""
        if self.head==None:
            return None
        else:
            return self.head.value

    def count(self):
        """The function 'count' returns the number of elements in the queue."""
        f = self.head
        count = []
        while f:
            count.append(f.value)
            f = f.next
        return len(count)
my_queue = Queue()
print(my_queue.front())
my_queue.enqueue(8)
my_queue.enqueue(10)
my_queue.enqueue(23)
my_queue.enqueue(4)
my_queue.enqueue(13)
my_queue.enqueue(45)
print(my_queue.front())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.front())
print(my_queue.count())
print(my_queue.head.next.next.value)

