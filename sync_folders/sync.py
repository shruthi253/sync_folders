import os
import shutil
import hashlib
import time


def synchronize(source_path, replica_path, log_file_path):

    # Create the log file
    with open(log_file_path, 'a') as log_file:
        log_file.write(f'Started synchronization at: {time.ctime()}\n')
        
    # Walk through the source folder for directories and files
    for root, dirs, files in os.walk(source_path):
        # replica_root = root.replace(source_folder, replica_folder)
        relative_path = os.path.relpath(root, source_path)
        replica_root = os.path.join(replica_path, relative_path)

        # Create corresponding directories in the replica folders
        for dir in dirs:
            #source_dir_path = os.path.join(root, dir)
            replica_dir_path = os.path.join(replica_root, dir)
            if not os.path.exists(replica_dir_path):
                os.makedirs(replica_dir_path)
                log_operation(log_file_path, f'Created directory: {replica_dir_path}')

        # Copy files to the replica folder
        for file in files:
            source_file_path = os.path.join(root, file)
            replica_file_path = os.path.join(replica_root, file)

            if not os.path.exists(replica_file_path) or not are_files_identical(source_file_path, replica_file_path):
                #copies file including its metadata
                shutil.copy2(source_file_path, replica_file_path)         
                log_operation(log_file_path, f'Copied file: {replica_file_path}')  
        print('first set over')
    
    # Walk through Replica for files and folders
    for root, dirs, files in os.walk(replica_path):
        relative_path = os.path.relpath(root, replica_path)
        source_root = os.path.join(source_path, relative_path)

        # Remove folders from the replica folder that do not exist in the source folder
        for dir in dirs:
            replica_dir_path = os.path.join(root, dir)
            source_dir_path = os.path.join(source_root, dir)

            if not os.path.exists(source_dir_path):
                shutil.rmtree(replica_dir_path)
                log_operation(log_file_path, "Removed directory: " + replica_dir_path) 
        
        # Remove files from the replica folder that do not exist in the source folder
        for file in files:
            replica_file_path = os.path.join(root, file)
            source_file_path = os.path.join(source_root, file)

            if not os.path.exists(source_file_path):
                os.remove(replica_file_path)
                log_operation(log_file_path, "Removed file: " + replica_file_path) 

    log_operation(log_file_path, f'Synchronization completed at: {time.ctime()}')


def log_operation(log_file_path, message):
    with open(log_file_path, 'a') as log_file:
        log_file.write(f'{message}\n')
    print(message)

def are_files_identical(file1, file2):

    # Buffer size to avoid out of memory issues
    BLOCK_SIZE = 65536   #64 kilobytes

    hasher1 = hashlib.md5()
    hasher2 = hashlib.md5()

    with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
        while True:
            data1 = f1.read(BLOCK_SIZE)
            data2 = f2.read(BLOCK_SIZE)

            if not data1 and not data2:
                break

            hasher1.update(data1)
            hasher2.update(data2)

    return hasher1.hexdigest() == hasher2.hexdigest()