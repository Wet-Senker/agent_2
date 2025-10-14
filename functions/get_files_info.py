import os

def get_files_info(working_directory, directory="."):
    full_user_path = os.path.join(working_directory, directory)
    abs_user_path = os.path.abspath(full_user_path)
    if not abs_user_path.startswith(working_directory):
        return f'Error: Cannot list "{abs_user_path}" as it is outside the permitted working directory'
    if not os.path.isdir(abs_user_path):
        return f'Error: "{abs_user_path}" is not a directory'
    
    try:
        file_info = []
        for file in os.listdir(abs_user_path):
            file_info.append(f"{os.path.basename(file)}: file_size={os.path.getsize(file)} bytes, is_dir={os.path.isdir(file)}")

        return "\n".join(file_info)

    except Exception as e:
        return f"Error listing files: {e}"