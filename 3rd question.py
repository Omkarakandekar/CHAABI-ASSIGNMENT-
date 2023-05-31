def sort_list_of_dicts(lst, key):
    sorted_list = sorted(lst, key=lambda x: x[key])
    return sorted_list

# Test case 1
input_list1 = [
    {"fruit": "orange", "color": "orange"},
    {"fruit": "apple", "color": "red"},
    {"fruit": "banana", "color": "yellow"},
    {"fruit": "blueberry", "color": "blue"}
]
sorted_list1 = sort_list_of_dicts(input_list1, "fruit")
print(sorted_list1)

# Test case 2
input_list2 = [
    {"fruit": "orange", "color": "orange"},
    {"fruit": "apple", "color": "red"},
    {"fruit": "banana", "color": "yellow"},
    {"fruit": "blueberry", "color": "blue"}
]
sorted_list2 = sort_list_of_dicts(input_list2, "color")
print(sorted_list2)
