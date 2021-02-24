# import os

# os.path.join('folder1', 'folder2', 'folder3', 'file.png')

# os.getcwd() Get current working directory

# os.chdir('c:\\') Change current working directory

# Theres 2 types of file paths

# Absolute File path:
# Absolute file path will always start with the root directory
# ex: 'c:\\folder1\\folder2\\spam.png'

# Relative File path:
# Relative file is relative to the current directory
# ex: spam.png

# os.path.abspath() for changing paths to absolute

# os.path.isabs check if the paths is absolute or not

# os.path.relpath()

# os.path.dirname('c:\\folder1\\folder2\\spam.png') gives you the directory name of the path you specified 'c:\\folder1\\folder2'

# os.path.basename('c:\\folder1\\folder2\\spam.png') gives you the base name of the object or directory 'spam.png'

# os.path.exists('c:\\folder1\\folder2\\spam.png') check if path exists 

# os.path.isfile('') checks if the path is a file
# os.path.isdir('')  checks if the path is a directory

# os.path.getsize('') check the size of the directory
# os.listdir('') list all the directory from the filepath

###
# This small program get the total size of the directory base on the file path
# totalSize = 0
# for filename in os.listdir('c:\\automatebook'):
#       if not os.path.isfile(os.path.join('c:\\automatebook', filesname)):
#           continue
#       totalSize = totalSize + os.getsize(os.path.isfile(os.path.join('c:\\automatebook', filesname)))

# os.unlink('') this delete a single file

# os.rmdir('') Remove a directory

# import shutil
# shutil.copy('','') Creates a copy of a file
# shutil.move('','') Move the file from one location to another or rename a file
# shutil.rmtree('') Delete everything inside the folder plus the directory

# pip install send2trash

# import send2trash
# send2trash.send2trash('') Send the file to the recycling bin instead of deleting it