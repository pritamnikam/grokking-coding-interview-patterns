def find_repeated_sequences(dna, k):
    
    string_length = len(dna)

    if string_length < k:
        return set()

    # Mapping of characters
    mapping = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    
    # Base value
    base_value = 4

    # Numeric representation of the sequence
    numbers = []
    for i in range(string_length):
        numbers.append(mapping.get(dna[i]))

    # Current hash value
    hash_value = 0

    # 1. Hash set to store the unique hash values
    # 2. Output set to store the repeated substrings
    hash_set = set()
    output = set()

    for i in range(string_length - k + 1):
        
        # If the window is at it's initial position, calculate the hash value from scratch
        if i == 0:
            for j in range(k):
                hash_value += numbers[j] * (base_value ** (k - j - 1))
            
        # Otherwise, utilize the previous hash value
        else: 
            previous_hash_value = hash_value
            hash_value = ((previous_hash_value - numbers[i - 1] * (base_value ** (k - 1))) * base_value) + numbers[i + k - 1]
        
        # If the current hash value is present in the hash set, the current substring has been repeated, so we add it to the output
        if hash_value in hash_set:
            output.add(dna[i : i + k])
            
        # We add the evaluated hash value to the hash set
        hash_set.add(hash_value)

    return output