def merge_list(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise TypeError("Both inputs must be lists.")
    
    for item in list1 + list2:
        if not isinstance(item, int):
            raise TypeError("All elements in both lists must be integers.")
    
    merged = list1 + list2

    n = len(merged)
    for i in range(n):
        for j in range(0, n - i - 1):
            if merged[j] > merged[j + 1]:
                merged[j], merged[j + 1] = merged[j + 1], merged[j]
    
    return merged

# a1 = [1, 5, 9]
# a2 = []
# print(merge_list(a1,  a2))