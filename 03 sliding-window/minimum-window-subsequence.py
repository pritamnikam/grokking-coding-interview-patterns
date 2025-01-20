def min_window(str1, str2):
    
    size_str1, size_str2 = len(str1), len(str2)
    min_sub_len = float('inf')
    index_s1, index_s2 = 0, 0
    min_subsequence = ""

    # iterate over str1
    while index_s1 < size_str1:
        # check if the character pointed by index_s1 in str1
        # is the same as the character pointed by index_s2 in str2
        if str1[index_s1] == str2[index_s2]:         
            # if the pointed character is the same
            # in both strings increment index_s2
            index_s2 += 1

            # check if a valid substring has been found
            if index_s2 == size_str2:
                # initialize start to the index where all characters of
                # str2 were present in str1
                start, end = index_s1, index_s1
                index_s2 -= 1

                # decrement pointer index_s2 and start a reverse loop
                while index_s2 >= 0:
                    # decrement pointer index_s2 until all characters of
                    #  str2 are found in str1
                    if str1[start] == str2[index_s2]:
                        index_s2 -= 1
                    
                    # decrement start pointer everytime to find the
                    # starting point of the required subsequence
                    start -= 1
                start += 1
                
                # update min_sub_len and min_subsequence if current subsequence is shorter
                if end - start + 1 < min_sub_len:
                    min_sub_len = end - start + 1
                    min_subsequence = str1[start : end + 1]
                
                # set index_s1 to end + 1 to continue checking in str1
                # after this discovered subsequence
                # index_s1 = end + 1
                index_s1 = start
                index_s2 = 0
                # continue
        # increment pointer index_s1 to check next character in str1
        index_s1 += 1
    # return the minimum window subsequence
    return min_subsequence        
