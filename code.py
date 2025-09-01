import os
import shutil

def organize_files(folder_path):
    # Check if the folder exists
    if not os.path.exists(folder_path):
        print("Folder does not exist.")
        return


    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

  
        if os.path.isdir(file_path):
            continue


        file_ext = filename.split('.')[-1].lower()

        ext_folder = os.path.join(folder_path, file_ext + "_files")
        os.makedirs(ext_folder, exist_ok=True)

        shutil.move(file_path, os.path.join(ext_folder, filename))

    print("Files have been organized successfully!")


if __name__ == "__main__":
    folder = input("Enter the folder path to organize: ").strip()
    organize_files(folder)
