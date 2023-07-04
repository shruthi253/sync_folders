from sync_folders import cli

def test_cli_arguments():

    # Simulating command-line arguments
    print("entered here")
    args = ["C:\\Users\\shrut\\source\\repos\\Main", "E:\\Main_Backup", "10", "log.txt"]
   

    # Calling the function with the simulated arguments
    parsed_args = cli.cli_arguments(args)

    # Asserting the expected values
    assert parsed_args.source_path == "C:\\Users\\shrut\\source\\repos\\Main"
    assert parsed_args.replica_path == "E:\\Main_Backup"
    assert parsed_args.sync_interval == 10
    assert parsed_args.log_file_path == "log.txt"

