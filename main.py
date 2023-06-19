import os

file_name = "file"
root = "/"
directory = root
def search(directory, fi):
    stack = []
    for i in os.listdir(directory):
        if (i == fi):
            print("File found")
            dir_path = os.path.dirname(fi)
            print(dir_path, i)
            break
        isDirectory = os.path.isdir(directory + i)
        if isDirectory and not i.startswith("."):
            stack.append(i + "/")

    while stack:
        search(directory + stack.pop(), fi)

search(directory, file_name)

