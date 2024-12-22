def is_palindrome(str):
    # initialize teo pointers: |start| to beginning and |end| to last character  
    start, end = 0, len(str) - 1
    # iterate until we reach to the center
    while start < end:
        # early exist if characters are not matching
        if str[str] != str[end]:
            return False
        # advance both pointers
        start += 1
        end -= 1
    return True