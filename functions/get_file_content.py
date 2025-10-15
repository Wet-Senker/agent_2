import pathlib
import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    abs_file_path = os.path.abspath(file_path)
    if not abs_file_path.startswith(working_directory):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    elif not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    with open(abs_file_path, "r") as f:
        file_content = f.read(MAX_CHARS)
        if os.path.getsize(abs_file_path) > MAX_CHARS:
            file_content += f'[...File "{file_path}" truncated at 10000 characters]'
        return file_content
    
        
print(get_file_content(os.getcwd(), 'file.txt')) 