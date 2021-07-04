import os
import shutil
import time

def get_fileorfolder_age(path):
    see_time=os.stat(path).st_ctime
    return see_time

def remove_folder(path):
    if(not shutil.rmtree(path)):
        print("removed successfully")
    else:
        print("enable to delete")

def remove_file(path):
    if(not os.remove(path)):
        print("removed successfully")
    else:
        print("enable to delete")

def main():
    source=input("Enter source directory: ")
    days=30
    deleted_folders=0
    deleted_files=0
    sec=time.time()-(days*24*60*60)
    if(os.path.exists(source)):
        for root_folder,folders,files in os.walk(source):
            if(sec>=get_fileorfolder_age(root_folder)):
                remove_folder(root_folder)
                deleted_folders+=1
                break
            else:
                for folder in folders:
                    folder_path=os.path.join(root_folder,folder)
                    if(sec>=get_fileorfolder_age(folder_path)):
                        remove_folder(folder_path)
                        deleted_folders+=1
                for file in files:
                    file_path=os.path.join(root_folder,file)
                    if(sec>=get_fileorfolder_age(file_path)):
                        remove_file(file_path)
                        deleted_files+=1
        else:
            if sec>=get_fileorfolder_age(source):
                remove_file(source)
                deleted_files+=1
    else:
        print("this file does not exsits")

    print(f"total folders deleted : {deleted_folders}")
    print(f"total files deleted : {deleted_files}")

main()


