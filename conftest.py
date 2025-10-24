import pytest

from praktikum.burger import Burger
from praktikum.database import Database


@pytest.fixture
def db():
    db = Database()
    return db

@pytest.fixture
def burger():
    burger = Burger()
    return burger