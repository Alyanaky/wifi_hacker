# utils/helpers.py

def read_dictionary(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]
