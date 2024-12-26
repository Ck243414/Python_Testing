# write a python program to print the contents of a directory using OS module
import os

def print_directory_contents(directory_path):
    try:
        # Get the list of files and directories in the specified path
        contents = os.listdir(directory_path)
        print(f"Contents of directory '{directory_path}':")
        
        for item in contents:
            print(f"- {item}")
    except FileNotFoundError:
        print(f"Error: The directory '{directory_path}' does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to access '{directory_path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
directory_path = input("Enter the path of the directory: ")
print_directory_contents(directory_path)
