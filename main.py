import os


def search_file(file_name):
    for root, dirs, files in os.walk('/'):
        if file_name in files:
            file_path = os.path.join(root, file_name)
            return os.path.dirname(file_path)
    return "File not found"


if __name__ == '__main__':
    file_name = input("Enter file name: ")
    print(search_file(file_name))

