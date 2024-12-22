import re

def reverse_words(sentence):
    # remove leading and trailing whitespaces
    sentence = re.sub(' +', ' ', sentence.strip())
    
    # conver to list of characters
    # for in-place modification as string are immutable in python
    sentence = list(sentence)
    str_len = len(sentence) - 1

    # reverse the whole string
    str_rev(sentence, 0, str_len)

    start = 0
    # iterate through the sentence to find and reverse each word
    for end in range(0, str_len + 1):
        if end == str_len or sentence[end] == ' ':
            # include character for last word
            end_idx = end if end == str_len else end - 1
            # reverse current word
            str_rev(sentence, start, end_idx)
            
            # move 'start' to the start of next word
            start = end + 1
    
    return ''.join(sentence)

def str_rev(_str, start, end):
    while start < end:
        _str[start], _str[end] = _str[end], _str[start]
        start += 1
        end -= 1