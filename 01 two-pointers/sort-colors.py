def sort_colors(colors):
    # initialize two pointers start, end to keep the '0's and '2's
    # and, keep another current pointer, to find present position 
    start, current, end = 0, 0, len(colors) - 1

    # iterate until we reach the end
    while current <= end:
        # if a match found for '0'
        if colors[current] == '0':
            # swap and advance |start| and |current|
            colors[current], colors[start] = colors[start], colors[current]
            start += 1
            current += 1
        # match found for '1'
        elif colors[current] == '1':
            # advance current
            current += 1
        # match found for '2'
        else:
            #swap and advance |current| and |end|
            colors[current], colors[end] = colors[end], colors[current]
            end -= 1

    return colors