'''
This file is useful if you want to replace format of .txt
file to something else. For example if you have files filename.cpp.txt,
then OS takes it as a Notebook file If file has a different original
ending and changed for some reason and you want to add that to the file
then append ending you with like this, 
after removing txt:  file_name_new +=".csv"
'''
import os
path = r"D:\My Documents\cpp"
directories = os.listdir(path)
file_name_updated = ''
for file in directories:
    if file[-1] == 't': #if old file ending is t
        file_name_updated = file[:-4] #then remove .txt part
        pathOld = os.path.join(path,file)
        pathNew = os.path.join(path, file_name_updated)
        os.rename(pathOld,pathNew)

