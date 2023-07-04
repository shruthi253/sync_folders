from sync_folders.cli import cli_arguments


def test_cli_arguments(tmpdir):
    # Simulating command-line arguments
    source_folder = str(tmpdir.join("source"))
    replica_folder = str(tmpdir.join("replica"))
    args = [source_folder, replica_folder, "10", "log.txt"]   

    # Calling the function with the simulated arguments
    parsed_args = cli_arguments(args)

    # Asserting the expected values
    assert parsed_args.source_path == source_folder
    assert parsed_args.replica_path == replica_folder
    assert parsed_args.sync_interval == 10
    assert parsed_args.log_file_path == "log.txt"