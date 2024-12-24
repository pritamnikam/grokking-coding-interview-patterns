def find_next_permutation(digits):
    i = len(digits) - 2
    while i >= 0 and digits[i] >= digits[i+1]:
        i -= 1
    if i == -1:
        return False
    
    j = len(digits) - 1
    while digits[j] <= digits[i]:
        j -= 1
    
    digits[i], digits[j] = digits[j], digits[i]
    digits[i + 1:] = reversed(digits[i + 1:])
    return True

def find_next_plaindrome(num_str):
    n = len(num_str)
    if n == 1:
        return ""
    
    half_length = n // 2
    left_half = list(num_str[:half_length])

    if not find_next_permutation(left_half):
        return ""
    
    if n % 2 == 0:
        next_palindrome = ''.join(left_half + left_half[::-1])
    else:
        middle_digit = num_str[half_length]
        next_palindrome = ''.join(left_half + [middle_digit] + left_half[::-1])

    if next_palindrome > num_str:
        return next_palindrome
    
    return ""