from main import check_same_path,source_path_exists,create_replica
import pytest
import os


def test_check_same_path(capsys, tmpdir):
    # Prepare test case data
    source_path = str(tmpdir.join("source"))
    replica_path = str(tmpdir.join("source"))

    # Call the function
    with pytest.raises(SystemExit) as exc_info:
        check_same_path(source_path, replica_path)

    # Assert the output and exit code
    out, err = capsys.readouterr()
    assert "Source and replica cannot be same path" in err
    assert out == ""
    assert exc_info.type == SystemExit
    assert exc_info.value.code == 1


def test_source_path_exists(capsys):
    # Prepare test case data
    source_path = str("")

    # Call the function
    with pytest.raises(SystemExit) as exc_info:
        source_path_exists(source_path)

    # Assert the output and exit code
    out, err = capsys.readouterr()
    assert "Source path does not exist." in err
    assert out == ""
    assert exc_info.type == SystemExit
    assert exc_info.value.code == 1


def test_create_replica(tmpdir):
    replica_folder = str(tmpdir.join("replica"))
    create_replica(replica_folder)

    assert os.path.exists(os.path.join(replica_folder))