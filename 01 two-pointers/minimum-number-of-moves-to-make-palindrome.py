def min_moves_to_make_palindrome(s):
    # strings are immutable in Python
    s = list(s)
    
    # 1. init moves to keep track of total moves required
    moves = 0

    # 2. start iterating string from both ends
    i, j = 0, len(s) - 1

    while i < j:
        # 3. use inner loop to search backward from j to find a character that matches s[i]
        k = j
        while k > i:
            if s[i] == s[k]:
                for m in range(k, j):
                    s[m], s[m+1] = s[m+1], s[m]
                    moves += 1
                j -= 1
                break
            k -= 1
        if k == i:
            moves += len(s) // 2 - i
        i += 1
    return moves