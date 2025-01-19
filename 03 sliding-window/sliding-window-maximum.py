from collections import deque

# Remove all indexes from current window whose corresponding 
# values are smaller than or equal to current value 
def cleanup(i, current_window, nums):
    while current_window and nums[i] >= nums[current_window[-1]]:
        current_window.pop()

# Function to find maximum in all windows
def find_max_sliding_window(nums, w):
    if len(nums) == 1:
        return nums
    
    output = []
    current_window = deque()

    # fill the first window elements
    for i in range(w):
        cleanup(i, current_window, nums)
        current_window.append(i)
    
    # first element always hold the max in current window
    output.append(current_window[0])

    # loop existing element in the nums array 
    for i in range(w, len(nums)):
        cleanup(i, current_window, nums)
        # slide window to the right
        if current_window and current_window[0] <= (i-w):
            current_window.popleft()
        
        current_window.append(i)
        # add the max element to the output aray
        output.append(nums[current_window[0]])

    return output