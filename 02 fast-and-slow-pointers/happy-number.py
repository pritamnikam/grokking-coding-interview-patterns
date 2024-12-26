def is_happy_number(n):
    # helper function to get sum of squared digits 
    def sum_of_squared_digits(num):
        sum = 0
        while num:
            x = num % 10
            num = num // 10
            sum += x**2
        return sum
    
    # initialize fast and slow pointers 
    slow_pointer, fast_pointer = n, sum_of_squared_digits(n)
    # loop until fast_pointer reaches 1 or both pointers are equal
    while fast_pointer != 1 and slow_pointer != fast_pointer:
        slow_pointer = sum_of_squared_digits(slow_pointer)
        fast_pointer = sum_of_squared_digits(sum_of_squared_digits(fast_pointer))

    if fast_pointer == 1:
        return True
    return False