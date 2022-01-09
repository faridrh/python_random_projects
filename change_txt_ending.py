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

