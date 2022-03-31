import os
import shutil

frm_dir="C:/Users/nsara/Downloads"
to_dir="C:/Users/nsara/Downloads/images"
list_of_files=os.listdir(frm_dir)
print(list_of_files)
for file_name in list_of_files:
    name,extension=os.path.splitext(file_name)
    print(name)
    print(extension)
    if extension=='':
        continue
    if extension in ['.gif','.png','.jpg','.jpeg','.jfif']:
        path1 = frm_dir+'/'+file_name
        path2 = to_dir+'/'+"C:/Users/nsara/Downloads/images"
        path3 = to_dir+'/'+"C:/Users/nsara/Downloads/images"+'/'+file_name
        # print("path1", path1)
        print("path2", path2)
        
    if os.path.exists(path2):
        #print("Moving " + file_name + ".....")
        shutil.move(path1,path3)
    else:
        os.makedirs(path2)
       # print("Moving " + file_name + ".....")
        shutil.move(path1,path3)