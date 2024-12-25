def is_palindrome(string):
  # utility function
  def is_palindrome_range(i, j):
     return all(string[j] == string[j - k + i] for k in range(i, j))
  
  # initialize two pinters at opposit ends
  left, right = 0, len(string) - 1

  # continue to match until both pointers meet
  while left < right:
    if string[left] != string[right]:
      return is_palindrome_range(left + 1, right) or is_palindrome_range(left, right - 1)
    left += 1
    right -= 1

  return True
