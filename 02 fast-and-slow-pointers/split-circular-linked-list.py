# Template for linked list node class

class LinkedListNode:
    # __init__ will be used to make a LinkedListNode type object.
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# Template for the circular linked list
class CircularLinkedList:
    # __init__ will be used to make a CircularLinkedList type object.
    def __init__(self):
        self.head = None

    # insert_node_at_head method will insert a LinkedListNode at head
    # of a circular linked list.
    def insert_node_at_head(self, node):
        if not self.head:
            # If list is empty, the new node will point to itself
            self.head = node
            node.next = node
        else:
            # Insert at head and make last node point to the new head
            last = self.head
            while last.next != self.head:
                last = last.next
            node.next = self.head
            self.head = node
            last.next = self.head  # Update last node to point to new head

    # create_linked_list method will create the linked list using the
    # given integer array with the help of InsertAtHead method.
    def create_linked_list(self, lst):
        for x in reversed(lst):
            new_node = LinkedListNode(x)
            self.insert_node_at_head(new_node)

    # __str__(self) method will display the elements of circular linked list.
    def __str__(self):
        result = ""
        if not self.head:
            return result
        temp = self.head
        result += str(temp.data)
        temp = temp.next
        while temp != self.head:
            result += " → " + str(temp.data)
            temp = temp.next
        result += " → (head)"  # Indicating the circular nature
        return result
        
def linked_list_to_array(head):
  if not head:
    return []

  result = []
  current = head
  seen_nodes = set()  

  while current not in seen_nodes:
    result.append(current.data)
    seen_nodes.add(current)
    current = current.next

  return result

# Template for printing the linked list with forward arrows

def print_circular_linked_list(linked_list_node):
    if not linked_list_node:
        print("List is empty", end=" ")
        return

    temp = linked_list_node
    seen_nodes = set()  # To track nodes we've already printed

    while temp and temp not in seen_nodes:
        print(temp.data, end=" ")  # print node value
        seen_nodes.add(temp)  # Add current node to seen nodes

        temp = temp.next
        if temp == linked_list_node:  # When we come back to the head node
            print("→ (head)", end=" ")
            break
        if temp:
            print("→", end=" ")
    print()  # Move to the next line after printing


def splitCircularLinkedList(head):
    # initialize slow and fast pointers
    slow, fast = head, head

    # continue until fast reaches the head again
    # slow pointer is at id
    while fast.next != head and fast.next.next != head:
        slow = slow.next
        fast = fast.next.next

    # two pointers
    head1 = head
    head2 = slow.next
    

    # point the end of first half to the head
    slow.next = head1 
    
    # find end of second half and connect to start of second half
    fast = head2
    while fast.next != head:
        fast = fast.next
        fast.next = head2

    return [head1, head2]




  


