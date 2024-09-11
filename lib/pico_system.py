import uos
import json
from time import sleep


""" Includes methods for different data relatet operationes """

def check_disk_space(path="."):
    """ Returns avelitable discspace in bytes """
    stat = uos.statvfs(path)
    free_space = stat[0] * stat[3]
    return free_space

def file_exists(file_path:str) -> bool:
    """ Returns True if file exist, false if not"""
    print(f"file path, checking: {file_path}")
    try:
        # Attempt to get file information
        stat_info = uos.stat(file_path)
        # If the above line doesn't raise an exception, the file exists
        return True
    except OSError as e:
        # If the exception indicates that the file doesn't exist (ENOENT), return False
        if e.args[0] == 2:  # 2 corresponds to ENOENT (No such file or directory)
            return False
        # If it's a different error, raise it
        print(f"Error checking file existence: {e}")
        raise e

def get_files(folder_path:str, file_type:str) -> list:
    """ Returns a list of selected file types in folder. Return an empty list if nothing is found """
    return_files = []
    # List all the files in the specified folder
    file_names = uos.listdir(folder_path) # Might get error if file does not exist?
    # Check for desiered file type
    for file_name in file_names:
        #print(file_name)
        if file_type in file_name:
            return_files.append(file_name)
    if not return_files:
        print("No files found in the specified folder.")
    return return_files
    
def save_data(data, file_path:str, mode:str="w"):
    with open(file_path, mode) as file:
        file.write(data)

def get_data(filepath:str, mode:str="r"):
    """ Returns content of a file"""
    with open(filepath, mode) as f:
        data = f.read()
    return data

def save_json_data(data, filepath:str, mode:str="w"):
    """ Saves json data """
    with open(filepath, mode) as f:
        json.dump(data, f)

def get_json_data(filepath):
    """ Returns file data in json format """
    with open(filepath, "r") as f:
        data = json.load(f)
    return data

def delete_file(file_path:str):
    """ Deletes the selected file """
    try:
        uos.remove(file_path)
        print(f"The file '{file_path}' has been deleted.")
    except OSError as e:
        print(f"Error deleting the file '{file_path}': {e}")