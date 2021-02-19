import os
## pics: 保存随机setu的路径
file_root = os.walk("setu_database")
pics = []
for path, dir_list, file_list in file_root:
    for file_name in file_list:
        pics.append(os.path.join(path, file_name))
