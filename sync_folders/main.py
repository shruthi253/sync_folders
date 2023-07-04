import sync
import cli
import os
import time
import tomllib
from pprint import pprint


def sync_folders(source_path, replica_path, sync_interval, log_file_path):
    # Synchronize folders periodically
    while True:
        try:
            sync.synchronize(source_path, replica_path, log_file_path)
            time.sleep(sync_interval)

        except Exception as e:
            print("Error occurred during synchronization:", str(e))
            sync.log_operation(log_file_path, "Error occurred during synchronization: " + str(e))


def load_toml() -> dict:    
    # Load TOML data from a file
    with open('..\config.toml', 'rb' ) as cf :
        toml_data: dict = tomllib.load(cf)
        return toml_data
    
# Passing commandline arguments
args = cli.cli_arguments()

# assign the commandline arguments
# Ensure source and replica folder paths are valid
source_path  = os.path.abspath(args.source_path)
replica_path = os.path.abspath(args.replica_path)

#Check for same paths
if source_path == replica_path:
    print("Source and replica cannot be same path")
    exit(1)

# Check if source path exists
if not os.path.exists(source_path):
    print("Source folder does not exist.")
    exit(1)

# Create replica folder if it does not exist
if not os.path.exists(replica_path):
    os.makedirs(replica_path)


sync_folders(args.source_path,args.replica_path, args.sync_interval, args.log_file_path)

if __name__ == '__main__':
    data : dict = load_toml()
    pprint(data, sort_dicts= False)
      
    

