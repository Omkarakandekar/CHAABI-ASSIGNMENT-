def compare_lists(list1, list2):
    common_elements = list(set(list1) & set(list2))
    not_common_elements = list(set(list1) ^ set(list2))
    return common_elements, not_common_elements

# Test the function
mainstream = ["One Punch Man", "Attack On Titan", "One Piece", "Sword Art Online", "Bleach", "Dragon Ball Z", "One Piece"]
must_watch = ["Full Metal Alchemist", "Code Geass", "Death Note", "Stein's Gate", "The Devil is a Part Timer!", "One Piece", "Attack On Titan"]

common, not_common = compare_lists(mainstream, must_watch)
print(common)
print(not_common)
