def find_duplicate(nums):
    # traverse nums using fast and slow pointers
    fast = slow = nums[0]
  
    # move slow one step and 
    # fast double the speed
    # until they meet
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    
    # move slow pointer from the nstart
    # and fast from the meeting point
    # advance one step at a time
    slow = nums[0]
   
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    
    # return fast as the meeting point
    return fast