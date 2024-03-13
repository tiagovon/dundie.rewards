from dundie.core import load
from tests.constants import PEOPLE_FILE
import pytest


@pytest.mark.unit
@pytest.mark.high
def test_load():
    """test load function"""
    assert len(load(PEOPLE_FILE)) == 2
    #assert load('tests/assets/people.csv')[0][0] =="t"