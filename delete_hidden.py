import os
import tkinter as tk
from tkinter import filedialog

def delete_files_with_prefix(prefix, path):
    deleted_files = []
    for root, _, files in os.walk(path):
        for file in files:
            if file.startswith(prefix):
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    deleted_files.append(file_path)
                    print(f"Deleted {file_path}")
                except OSError as e:
                    print(f"Error deleting {file_path}: {e}")
    return deleted_files

def select_directory():
    root = tk.Tk()
    root.withdraw()
    directory = filedialog.askdirectory(title="Select a directory to search for files")
    return directory

if __name__ == "__main__":
    prefix = "._"
    drive_path = select_directory()

    if not drive_path:
        print("No directory selected.")
    else:
        print(f"Deleting files starting with '{prefix}' in the selected directory: {drive_path}")
        deleted_files = delete_files_with_prefix(prefix, drive_path)

        if deleted_files:
            print(f"Deleted the following files:")
            for deleted_file in deleted_files:
                print(f"- {deleted_file}")
        else:
            print(f"No files starting with '{prefix}' were found in the selected directory.")

