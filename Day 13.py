class Node:
    """In the class 'Node' every node has a value (integer)  and a next(type Node)."""
    def __init__(self, value):
        self.value = value
        self.next = None
        
def append(head,k):
    """The function append adds the parameter 'k' to the end of the Node object(linked list)."""

    assert type(k)==int
    assert type(head)==Node
    a = Node(k)
    if head.value is None:
        head.value = a
    else:
        m = head
        while m.next:
            m = m.next
        m.next = a

def pop(head):
    """The function pop removes the last element in the linked list."""
    assert type(head)==Node
    d = head
    if head.next==None:
        head = None
    else:
        c = head
        while c.next.next:
            c =  c.next
        c.next = None
Head = Node(5)
append(Head,7)
append(Head,9)
append(Head,11)
pop(Head)
print(Head.next.next.value)
