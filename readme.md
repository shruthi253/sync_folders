

# A program that synchronizes two folders: source and replica

- Synchronization must be one-way: after the synchronization content of the 
  replica folder should be modified to exactly match content of the source 
  folder;
- Synchronization should be performed periodically.
- File creation/copying/removal operations should be logged to a file and to the 
  console output;
- Folder paths, synchronization interval and log file path should be provided 
  using the command line arguments; 