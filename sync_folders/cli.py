import argparse

# Parse command line arguments
def cli_arguments(argv=None):
    parser = argparse.ArgumentParser(description="Folder Synchronization Program")
    parser.add_argument("source_path", help="Path to the source folder")
    parser.add_argument("replica_path", help="Path to the replica folder")
    parser.add_argument("sync_interval", type=int, help="Synchronization interval in seconds", default=10)
    parser.add_argument("log_file_path", help="Path to the logfile")
    return parser.parse_args(argv)
   

    
    

