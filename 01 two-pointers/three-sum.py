def find_sum_of_three(nums, target):
    # sort the list
    nums.sort()

    # iterate in range
    for i in range(len(nums) - 2):
        # initilize two pinters relative to |i|, 
        # |start| will be the next charater and |end| will the last in list 
        start, end = i + 1, len(nums) - 1

        # iterate until we explore all combinations
        while start < end:
            # a combination sum
            triplet = nums[i] + nums[start] + nums[end]
            # match found
            if triplet == target:
                return True
            # advance |start| to the next in list
            elif triplet < target:
                start += 1
            # advance |end| to the previous
            else:
                end -= 1
    # match not found
    return False