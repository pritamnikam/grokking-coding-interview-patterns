def is_strobogrammatic(num):
    # hash of the strobogrammatic numbers
    dict = {
        '0': '0',
        '1': '1',
        '8': '8',
        '6': '9',
        '9': '6'
    }
    # init two poiters  
    start, end = 0, len(num) - 1

    # move both pointers inward until they cross
    while start < end:
        # pair of digits does not match, its not a valid rotation
        if (num[start] not in dict) or (num[end] != dict[num[start]]):
            return False
        
        start += 1
        end -= 1

    return True