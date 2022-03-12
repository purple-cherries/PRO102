import os
import shutil

src = 'C:/Users/vkaun/Downloads'
dst = 'C:/Users/vkaun/Downloads'

files = os.listdir(src)


for file in files:
    name,ext = os.path.splitext(file)

    if ext == '':
       continue
    if ext in ['.zip']:
        path1 = src+'/'+file
        path2 = dst+'/'+'ZipFiles'
        path3 = dst+'/'+'ZipFIles'+'/'+file

        if os.path.exists(path2):
            print('Moving '+ file)        
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print('Moving '+ file)        
            shutil.move(path1,path3)