import pytest

from tiagovondundie.core import read
from tiagovondundie.database import add_person, commit, connect


@pytest.mark.unit
def test_read_with_query():
    db = connect()
    pk = "joe@doe.com"
    data = {"role": "Salesman", "dept": "Sales", "name": "Joe Doe"}
    db = connect()
    _, created = add_person(db, pk, data)
    assert created is True
    commit(db)

    pk = "jin@dow.com"
    data = {
        "role": "'Manger",
        "dept": "Management",
        "name": "Jim Doe",
    }
    _, created = add_person(db, pk, data)
    assert created is True
    commit(db)
    response = read()
    assert len(response) == 2

    response = read(dept="Management")
    assert len(response) == 1
    assert response[0]["name"] == "Jim Doe"

    response = read(email="joe@doe.com")
    assert len(response) == 1
    assert response[0]["name"] == "Joe Doe"
