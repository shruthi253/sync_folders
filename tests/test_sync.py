from sync_folders.sync import are_files_identical,synchronize
import os

def test_are_files_identical(tmpdir):
    file_path1 = os.path.join(str(tmpdir), "file1.txt")
    file_path2 = os.path.join(str(tmpdir), "file2.txt")                          

    with open(file_path1, "w") as f1:
        f1.write("This is file 1")
    with open(file_path2, "w") as f2:
        f2.write("This is file 2")

    assert are_files_identical(file_path1,file_path2) is False


def test_synchronize(tmpdir):    
    # Create source and replica folders
    source_folder = str(tmpdir.join("source"))
    replica_folder = str(tmpdir.join("replica"))

    # Create test files and directories in the source folder
    os.makedirs(os.path.join(source_folder, "dir1"))
    os.makedirs(os.path.join(source_folder, "dir2"))
    with open(os.path.join(source_folder, "file1.txt"), "w") as f:
        f.write("This is file 1")
    with open(os.path.join(source_folder, "file2.txt"), "w") as f:
        f.write("This is file 2")

    # Call the synchronize function
    synchronize(source_folder, replica_folder, "test_log.txt")

    # Check if the replica folder contains the same files and directories as the source folder
    assert os.path.exists(os.path.join(replica_folder, "dir1"))
    assert os.path.exists(os.path.join(replica_folder, "dir2"))
    assert os.path.isfile(os.path.join(replica_folder, "file1.txt"))
    assert os.path.isfile(os.path.join(replica_folder, "file2.txt"))

    # verify contents of files on both source and replica are same 
    with open(os.path.join(replica_folder, "file1.txt"),"r") as f1:
        content1 = f1.read()
    with open(os.path.join(replica_folder, "file2.txt"),"r") as f2:
        content2 = f2.read()

    assert content1 == "This is file 1"
    assert content2 == "This is file 2"    

def test_remove_files_from_replica(tmpdir):

    source_path = str(tmpdir.join("source"))
    replica_path = str(tmpdir.join("replica"))

    os.makedirs(os.path.join(source_path, "dir1"))
    with open(os.path.join(source_path,"file1"), "w") as f:
        f.write("This belongs to source")

    os.makedirs(os.path.join(replica_path,"dir3"))
    with open(os.path.join(replica_path,"file3"), "w") as f:
        f.write("This should be removed from replica")

    # Call the synchronize function
    synchronize(source_path, replica_path, "test_log.txt")

    assert not os.path.isdir(os.path.join(replica_path,"dir3"))
    assert not os.path.exists(os.path.join(replica_path,"file3"))

def test_sync_one_way(tmpdir):

    source_path = str(tmpdir.join("source"))
    replica_path = str(tmpdir.join("replica"))

    os.makedirs(os.path.join(replica_path,"dir3"))
    with open(os.path.join(replica_path,"file3"), "w") as f:
        f.write("This should be removed from replica")

    # Call the synchronize function
    synchronize(source_path, replica_path, "test_log.txt")

    # assert replica folder does not added to source
    assert not os.path.isdir(os.path.join(source_path,"dir3"))
    assert not os.path.exists(os.path.join(source_path,"file3"))