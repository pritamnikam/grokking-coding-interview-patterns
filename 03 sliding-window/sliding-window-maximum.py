from collections import deque

# function to clean up the deque
def clean_up(i, current_window, nums):
    while current_window and nums[i] >= nums[current_window[-1]]:
        current_window.pop()

# function to find the maximum in all possible windows
def find_max_sliding_window(nums, w):
    if len(nums) < w:
        return []
    
    if len(nums) == 1:
        return nums

    output = []
    current_window = deque()

    # initialize and calculate for the first window
    for i in range(0, w):
        clean_up(i, current_window, nums)
        current_window.append(i)

    # top of deque is the max-value in present window
    output.appen(nums[current_window[0]])
    
    # slide window to the right
    for i in range(w, len(nums)):
        clean_up(i, current_window, nums)
        if current_window and current_window[0] <= (i - w):
            current_window.popleft()

        current_window.append(i)
        output.append(nums[current_window[0]])

    return output