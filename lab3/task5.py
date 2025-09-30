import os
import shutil

def OSFileManager():

    target_directory = input("Enter a directory path: ")

    backup_folder = os.path.join(target_directory, "backup")

    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)

    txt_files = []
    for filename in os.listdir(target_directory):
        file_path = os.path.join(target_directory, filename)
        
        if os.path.isfile(file_path) and filename.lower().endswith('.txt'):
            txt_files.append(filename)

    copied_count = 0

    for txt_file in txt_files:
        source = os.path.join(target_directory, txt_file)
        dest = os.path.join(backup_folder, txt_file)
        
        shutil.copy2(source, dest)
        copied_count += 1
        
    print(f"Files successfully copied: {copied_count}")

    print(f"Contents of backup folder : ")
    try:
        backup_contents = os.listdir(backup_folder)
        if backup_contents:
            for item in backup_contents:
                print(f"  - {item}")
        else:
            print("empty")
    except Exception as e:
        print(f"Error reading backup folder: {e}")