def circular_array_loop(nums):  
    n = len(nums)
    for i in range(n):
        slow, fast = i, i
        forward = nums[i] > 0

        while True:
            slow = next_step(slow, nums[slow], n)
            if is_not_cycle(nums, forward, slow):
                break

            fast = next_step(fast, nums[fast], n)
            if is_not_cycle(nums, forward, fast):
                break

            fast = next_step(fast, nums[fast], n)
            if is_not_cycle(nums, forward, fast):
                break

            if fast == slow:
                return True            

    return False


# utility function to calculate next step
def next_step(pointer, value, size):
    result = (pointer + value) % size
    if result < 0:
        result += size
    
    return result

# utility to detect cycle doesn't exist
def is_not_cycle(nums, prev_direction, pointer):
    curr_direction = nums[pointer] > 0

    if (prev_direction != curr_direction) or (abs(nums[pointer] % len(nums)) == 0):
        return True
    return False