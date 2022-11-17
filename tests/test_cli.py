from djtodo_cli.djtodo.djtodo import cli
import test_File

def test_command_cli(capsys):
    args = ["add hello"]
    cli(args)
    captured = capsys.readouterr()
    result = captured.out
    assert "hi" in result