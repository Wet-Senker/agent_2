import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    abs_cwd = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_cwd):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_file_path):
        f'Error: File "{file_path}" not found.'
    if not abs_file_path.endswith(".py"):
        f'Error: "{file_path}" is not a Python file.'

    subprocess.run(["python", abs_file_path], timeout=30, stdout=True, stderr=True, cwd=abs_cwd)
    