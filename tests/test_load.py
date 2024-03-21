import pytest

from dundie.core import load
from tests.constants import PEOPLE_FILE


@pytest.mark.unit
def test_load_positive_had_2_people(request):
    """test load function"""
    assert len(load(PEOPLE_FILE)) == 2


@pytest.mark.unit
def test_load_positive_dirst_name_starts_with_t(request):
    """test load function"""
    assert load(PEOPLE_FILE)[0][0] == "t"
