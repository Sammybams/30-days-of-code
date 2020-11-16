class Node:
    """
    Each node has a value which can be accessed as self.value
    Each node has a left and right Node which are accessible as self.left and self.right respectively.
    """
    def __init__(self,value):
        """The Node constructor takes the value(integer) and initializes the value of a node to the value of the value given to the constructor."""
        assert type(value)==int
        self.value = value
        self.left = None
        self.right = None
        
def dealing_with_lists(node,num):
    """The function 'dealing_with_lists' inserts a new integers in order to the Binary Search Tree."""
    if node is None: 
        return Node(num) 
  
    # Checks for the order of the inputs and inserts it in the rightful position
    if num < node.value:
        node.left = dealing_with_lists(node.left, num) 
    else: 
        node.right = dealing_with_lists(node.right, num) 
  
    # Returns the (unchanged) node pointer 
    return node 

def insert_to_tree(array):
    """The function 'insert_to_tree' takes an array and inputs the elements of the array in order into a binary tree and returns the root."""
    assert type(array)==list
    if array==[]:
        raise AssertionError
    for m in array:
        assert type(m)==int
    node = Node(array[0])
    array.remove(array[0])
    #Loops through the integers in the list and inserts them in order.
    for i in array:
        dealing_with_lists(node,i)

    return node

def find_path(head,a,b):
    """The function 'find_path' find the longest distance from the root to a leaf node in the binary tree."""
    #Loops through the leaf node starting from the root in the binary tree until it finds the maximum distance from the root.
    if head is None:
        if b[0] < a:
            b[0] = a
        return b
    find_path(head.left,a+1,b)
    find_path(head.right,a+1,b)
    
def max_height(head):
    """
    The function 'max_height' takes in the root of the binary tree and
    returns the maximum height (i.e the maximum distance from the root to the leaf node).
    """
    #Checks if the input is None and returns zero(0) as its maximum height.
    #Else, it loops through the binary tree to find the maximum distance from the root to the leaf node.
    assert type(head)==Node
    if head is None:
        return 0
    b = [0]
    find_path(head,0,b)

    return b[0]
