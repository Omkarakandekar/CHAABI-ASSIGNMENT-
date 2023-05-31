def get_sublist(lst, start_index, end_index):
    sublist = lst[start_index:end_index+1:2]
    return sublist

# Test the function
lst = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
start_index = 2
end_index = 9

result = get_sublist(lst, start_index, end_index)
print(result)
