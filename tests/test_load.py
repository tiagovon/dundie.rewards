from dundie.core import load
from tests.constants import PEOPLE_FILE
import pytest
import uuid
import os

@pytest.mark.unit
@pytest.mark.high
def test_load_positive_had_2_people(request):
    """test load function"""
    assert len(load(PEOPLE_FILE)) == 2


@pytest.mark.unit
@pytest.mark.high
def test_load_positive_dirst_name_starts_with_t(request):
    """test load function"""
    assert load(PEOPLE_FILE)[0][0] =="t"