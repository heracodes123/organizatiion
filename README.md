# File Organizer Script

A simple Python script that organizes files in a given folder into subfolders based on their file extensions. For example, all `.txt` files will be moved into a `txt_files` folder, `.jpg` files into a `jpg_files` folder, and so on.


# Features
- Automatically creates folders for each file extension.
- Moves files into their respective extension-based folders.
- Skips existing folders (does not move directories).
- Easy to run with minimal setup.



# Requirements
- Python 3.x  
- Standard library modules (`os`, `shutil`) — no external installations required.

  Example
Before:
Downloads/
│── notes.txt
│── photo.jpg
│── report.pdf

After running the script:
Downloads/
│── txt_files/
│    └── notes.txt
│── jpg_files/
│    └── photo.jpg
│── pdf_files/
     └── report.pdf


#Notes

The script ignores directories inside the target folder.
If files already exist in the destination folder, they may be overwritten.

# License
This project is free to use and modify.
