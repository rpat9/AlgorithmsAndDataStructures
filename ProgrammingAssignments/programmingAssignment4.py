# Chapter 4 -Programming Project [P-4.23]: implement a recursive function with signature find(path, filename) that reports all entries of the file system rooted at the 
# given path (relative path i.e. from wherever the program is located) having the given file name (partial match). 

import os

def find (path, filename):
    
    """
    This function searches for a specific filename in a given path using recursion.
    
    Parameters:
    path (str): The root path from which the search should begin.
    filename (str): The filename to search for. A partial match is sufficient.
    
    Returns:
    None. The function should print the full path of each matching file.
    """
    
    try:
        entries = os.listdir(path) # Trys to list all entries in the specified path
    except:
        print(f"Error accessing {path}") # Provides an error message if the path is invalid / not found
        return
    
    for entry in entries:
        full_path = os.path.join(path, entry) # Creates the full path
        
        if entry.endswith(filename): # Checks if path matches filename
            print(full_path) 
        
        if os.path.isdir(full_path): 
            find(full_path, filename) # Recursively calls the function
            

if __name__ == "__main__":
    path = "./TDir"
    filename = ".docx"
    find (path, filename)