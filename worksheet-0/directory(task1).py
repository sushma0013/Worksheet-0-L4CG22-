def calculate_directory_size(directory):
    total_size = 0
    for key, value in directory.items():
        if isinstance(value, dict):  
            total_size += calculate_directory_size(value)
        elif isinstance(value, (int, float)):  
            total_size += value
    return total_size  


directory_structure = {
    "file1.txt": 200,
    "file2.txt": 300,
    "subdir1": {
        "file3.txt": 400,
        "file4.txt": 100
    },
    "subdir2": {
        "subsubdir1": {
            "file5.txt": 250
        },
        "file6.txt": 150
    }
}


total_size = calculate_directory_size(directory_structure)
print(f"Total Directory Size: {total_size} KB")


