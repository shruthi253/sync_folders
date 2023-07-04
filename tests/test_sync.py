from sync_folders.sync import are_files_identical

def test_are_files_identical():
    f1 = r"C:\Users\shrut\source\repos\Main\file1.txt"
    f2 = r"E:\Main_Backup\file2.xlsx"

    assert are_files_identical(f1,f2) is False

