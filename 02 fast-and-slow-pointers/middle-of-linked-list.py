def get_middle_node(head):
    if head is None:
        return None
    
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow