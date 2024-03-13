from subprocess import  check_output
import pytest

@pytest.mark.integration
@pytest.mark.medium
def test_load():
    """test commmand load """
    out=check_output(["dundie","load","tests/assets/people.csv"]).decode("utf-8").split("\n")
    assert len(out)==2