import pathlib
import os
from config import MAX_CHARS
from google.genai import types

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

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="get the content of the files in the specified directory to a maximum of 10000 characters. Constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file_path of the file that needs to be read.",
            ),
        },
        required=["file_path"],
    ),
) 