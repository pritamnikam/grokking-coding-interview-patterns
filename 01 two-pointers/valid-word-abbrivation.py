def valid_word_abbreviation(word, abbr):
    # We initialize one pointer to the start of the word and the other to the start of the abbreviation.
    word_index, abbr_index = 0, 0

    # iterate over abbr
    while abbr_index < len(abbr):
        # if curretn position is a digit
        if abbr[abbr_index].isdigit():
            if abbr[abbr_index] == '0':
                return False
            num = 0

            # form a number
            while abbr_index < len(abbr) and abbr[abbr_index].isdigit():
                num = num * 10 + int(abbr[abbr_index])
                abbr_index += 1
            word_index += num
        else:
            # current position is alphabet and does not match to the char in word
            if word_index >= len(word) or word[word_index] != abbr[abbr_index]:
                return False
            word_index += 1
            abbr_index += 1

    return word_index == len(word) and abbr_index == len(abbr)