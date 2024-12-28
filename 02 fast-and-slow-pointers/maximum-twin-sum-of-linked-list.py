# Template for linked list node class

class LinkedListNode:
    # __init__ will be used to make a LinkedListNode type object.
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# Template for the linked list
class LinkedList:
    # __init__ will be used to make a LinkedList type object.
    def __init__(self):
        self.head = None

    # insert_node_at_head method will insert a LinkedListNode at head
    # of a linked list.
    def insert_node_at_head(self, node):
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = node

    # create_linked_list method will create the linked list using the
    # given integer array with the help of InsertAthead method.
    def create_linked_list(self, lst):
        for x in reversed(lst):
            new_node = LinkedListNode(x)
            self.insert_node_at_head(new_node)
    
    # __str__(self) method will display the elements of linked list.
    def __str__(self):
        result = ""
        temp = self.head
        while temp:
            result += str(temp.data)
            temp = temp.next
            if temp:
                result += ", "
        result += ""
        return result
    
# Template for printing the linked list with forward arrows
def print_list_with_forward_arrow(linked_list_node):
    temp = linked_list_node
    while temp:
        print(temp.data, end=" ")  # print node value
        
        temp = temp.next
        if temp:
            print("→", end=" ")
        else:
            # if this is the last node, print null at the end
            print("→ null", end=" ")

# Template to reverse the linked list
def reverse_linked_list(slow_ptr):
    prev = None
    next = None
    curr = slow_ptr
    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

# utility function to get the maximum twin sum
def maximum_sum(first_half, second_half):
    max_sum = 0
    while first_half and second_half:
        if first_half.data + second_half.data > max_sum:
            max_sum = first_half.data + second_half.data
        first_half = first_half.next
        second_half = second_half.next
    return max_sum


def twin_sum(head):
  
    # initialize two pointer
    slow, fast = head, head

    # find the mid
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    revert_data = reverse_linked_list(slow)
    max_sum = maximum_sum(head, revert_data)
    
    reverse_linked_list(revert_data)
    return max_sum