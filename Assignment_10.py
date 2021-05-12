#!/usr/bin/env python
# coding: utf-8

# # 1.How do you distinguish between shutil.copy() and shutil.copytree()?

# In[ ]:


A.shutil.copytree() method recursively copies an entire directory tree rooted at source (src) to the destination directory. The destination directory, named by (dst) must not already exist. 
It will be created during copying. Permissions and times of directories are copied with copystat() and individual files are copied using shutil.copy2().


# In[ ]:


import shutil 
import os
path = 'C:/Users / saleem / Desktop / DataScience'
print("Before copying file:") 
print(os.listdir(path)) 
src = 'C:/Users / saleem / Desktop / DataScience / source'
dest = 'C:/Users / saleem / Desktop / DataScience / destination'
destination = shutil.copytree(src, dest) 
print("After copying file:") 
print(os.listdir(path)) 
print("Destination path:", destination)

shutil.copy() method in Python is used to copy the content of source file to destination file or directory. It also preserves the file’s permission mode but other metadata of the file like the file’s creation and modification times is not preserved.
# In[ ]:


import os
import shutil
path = '/home/User/Documents'
print("Before copying file:")
print(os.listdir(path))
source = "/home/User/Documents/file.txt"
perm = os.stat(source).st_mode
print("File Permission mode:", perm, "\n")
destination = "/home/User/Documents/file(copy).txt"
dest = shutil.copy(source, destination)
print("After copying file:")
print(os.listdir(path))
perm = os.stat(destination).st_mode
print("File Permission mode:", perm)
print("Destination path:", dest)


# # 2.What function is used to rename files?
A.os. rename() method in Python is used to rename a file or directory. This method renames a source file/ directory to specified destination file/directory
# # 3.What is the difference between the delete functions in the send2trash and shutil modules?
A.The send2trash functions will move a file or folder to the recycle bin, while shutil modules will permanently delete files and folders
# # 4.ZipFile objects have a close() method just like File objects’ close() method. What ZipFile method is equivalent to File objects’ open() method?
A. ZipFile objects are conceptually similar to the File objects you saw returned by the open() function, they are values through which the program interacts with the file. To create a ZipFile object, call the zipfile.ZipFile() function.
passing it a string of the .ZIP file’s filename. Note that zipfile is the name of the Python module, and ZipFile() is the name of the function.
# In[ ]:


import zipfile, os
rom pathlib import Path
p = Path.home()
exampleZip = zipfile.ZipFile(p / 'example.zip')
exampleZip.namelist()


# In[ ]:


spamInfo = exampleZip.getinfo('spam.txt')
spamInfo.file_size


# In[ ]:


spamInfo.compress_size
exampleZip.close()


# # 5.Create a programme that searches a folder tree for files with a certain file extension (such as .pdf or .jpg). Copy these files from whatever location they are in to a new folder.

# In[6]:


import os, shutil

def selectiveCopy(folder, extensions, destFolder):
    folder = os.path.abspath(folder)
    destFolder = os.path.abspath(destFolder)
    print('Looking in', folder, 'for files with extensions of', ', '.join(extensions))
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            name, extension = os.path.splitext(filename)
            if extension in extensions:
                fileAbsPath = foldername + os.path.sep + filename
                print('Coping', fileAbsPath, 'to', destFolder)
                shutil.copy(fileAbsPath, destFolder)

extensions = ['.pdf', '.jpg']
folder = 'randomFolder'
destFolder = 'selectiveFolder'
selectiveCopy(folder, extensions, destFolder)


# In[ ]:




