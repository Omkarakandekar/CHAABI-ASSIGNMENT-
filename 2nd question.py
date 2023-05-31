def get_file_type(extension_type_list, filenames):
    file_types = {}
    extension_type_pairs = extension_type_list.split(";")

    for filename in filenames:
        file_extension = filename.split(".")[-1]
        file_type = "unknown"

        for pair in extension_type_pairs:
            extension, type = pair.split(",")
            if extension == file_extension:
                file_type = type
                break

        file_types[filename] = file_type

    return file_types


extension_type_list = "xls,spreadsheet;xlsx,spreadsheet;jpg,image"
filenames = ["abc.jpg", "xyz.xls", "text.csv", "123"]
file_types = get_file_type(extension_type_list, filenames)
print(file_types)
