import os
file_root = os.walk("setu_database")
pics = []
for path, dir_list, file_list in file_root:
    for file_name in file_list:
        # print(os.path.join(path,file_name))
        pics.append(os.path.join(path, file_name))