"""
LinkedList
"""
class Element(object): # Node() some prefer this
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        """Add new_element in Linked List"""
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
            
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        current_position = 1
        current = self.head
        if position < 1:
            return None
        while current and current_position <= position:
            if current_position == position:
                return current
            current = current.next
            current_position+=1
            
        return None
    
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        current_position = 1
        current = self.head
        if position > 1:
            while current and current_position<=position:
                if current_position == position-1:
                    old_element = current.next
                    current.next = new_element
                if current_position == position:
                    new_element.next = old_element
                current = current.next
                current_position +=1
        elif position == 1:
            new_element.next = self.head
            self.head = new_element
    
    
    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        prev = None
        while current.next and current.value != value:
            prev = current
            current = current.next
        
        if current.value == value:
            if prev:
                prev.next = current.next
            else:
                self.head = current.next
            

# TEST CASES
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

print("Test get_postion")
# Test get_position
# Should print 3
print(ll.head.next.next.value)
# Should also print 3
print(ll.get_position(3).value)

print("Test Insert")
# # Test insert
ll.insert(e4,3)
# # Should print 4 now
print(ll.get_position(3).value)

print("Test delete")
# Test delete
ll.delete(1)
# Should print 2 now
print(ll.get_position(1).value)
# Should print 4 now
print(ll.get_position(2).value)
# Should print 3 now
print(ll.get_position(3).value)
