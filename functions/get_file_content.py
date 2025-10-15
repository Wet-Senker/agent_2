import pathlib
import os

def get_file_content(working_directory, file_path):
    print(working_directory) # DEBUG
    print(file_path) # DEBUG
    print(os.path.abspath(file_path))
    if not os.path.abspath(file_path).startswith(working_directory):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    elif not os.path.isfile(file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    return "all good" # DEBUG
    

print(get_file_content(os.getcwd(), 'file.txt')) 