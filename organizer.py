import os
import shutil

def organize_files(directory):
    if not os.path.exists(directory):
        print(f"Directory {directory} doesn't exist.")
        return

    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        
        if os.path.isfile(filepath):
            # Get the file extension and create a directory name based on the extension
            file_ext = filename.split('.')[-1]
            dir_name = file_ext + '_files'
            
            # Create directory if it doesn't exist
            new_dir_path = os.path.join(directory, dir_name)
            if not os.path.exists(new_dir_path):
                os.makedirs(new_dir_path)
            
            # Move file to the new directory
            shutil.move(filepath, os.path.join(new_dir_path, filename))

    print(f"Organized all files in {directory}.")

def main():
    directory = input("Enter directory path to organize: ")
    organize_files(directory)

if __name__ == "__main__":
    main()
