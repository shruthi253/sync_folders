from sync_folders import sync
from sync_folders import cli
import os
import time
import sys
import tomllib
from pprint import pprint


def start_folder_sync(source_path, replica_path, sync_interval, log_file_path):
    # Synchronize folders periodically
    while True:
        try:
            sync.synchronize(source_path, replica_path, log_file_path)
            time.sleep(sync_interval)

        except Exception as e:
            print("There is an error occurred during synchronization:", str(e))
            sync.log_operation(log_file_path, "Error occurred during synchronization: " + str(e))


def check_same_path(source, replica):
    if source == replica:
        print("Source and replica cannot be same path", file = sys.stderr)
        sys.exit(1)


def source_path_exists(source):
    # check if source exists
    if not os.path.exists(source):
        print("Source path does not exist.", file = sys.stderr)
        sys.exit(1)


def create_replica(replica):
    # Create replica folder if it does not exist
    if not os.path.exists(replica):
        os.makedirs(replica)


def call_cli_arguments():
    # Passing commandline arguments
    args = cli.cli_arguments()

    # Ensure source and replica folder paths are valid
    source_path  = os.path.abspath(args.source_path)
    replica_path = os.path.abspath(args.replica_path)

    check_same_path(source_path, replica_path)
    source_path_exists(source_path)
    create_replica(replica_path)

    # call sync function
    start_folder_sync(source_path, replica_path, args.sync_interval, args.log_file_path)


def load_toml() -> dict:    
    # Load TOML data from a file
    with open('.\\config.toml', 'rb' ) as cf :
        toml_data: dict = tomllib.load(cf)
        return toml_data    

if __name__ == '__main__':
    data : dict = load_toml()
    pprint(data, sort_dicts= False)
    call_cli_arguments()  