def reverse_sort_dictionary(data_dict):
    if not isinstance(data_dict, dict):
        raise TypeError("Input must be a dictionary.")
    

    for key, value in data_dict.items():
        if not isinstance(key, str):
            raise TypeError("All keys must be strings.")
        if not (isinstance(value, tuple) and len(value) == 2):
            raise TypeError("Each value must be a tuple of length 2.")
        if not all(isinstance(v, int) for v in value):
            raise TypeError("Tuple elements must be integers (phone number, age).")
    
    keys = list(data_dict.keys())
    n = len(keys)
    for i in range(n):
        for j in range(0, n - i - 1):
            if keys[j] < keys[j + 1]:
                keys[j], keys[j + 1] = keys[j + 1], keys[j]

    result = [(key, data_dict[key][0]) for key in keys]
    
    return result

# a = {"Tom" : (5464512, 24) , "Sara" : (5446987, 32) , "Mary" : (1557896, 20)}
# print(reverse_sort_dictionary(a))