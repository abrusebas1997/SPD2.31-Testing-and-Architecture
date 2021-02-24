import pytest
from ..exercise4 import extract_position

@pytest.fixture
def error():
    return "error x:21.432"

@pytest.fixture
def debug():
    return "debug y:324"

@pytest.fixture
def valid():
    return "Spot here x:239.84629"

def test_extract_position_error(error):
    assert extract_position(error) == None

def test_extract_position_debug(debug):
    assert extract_position(debug) == None

def test_extract_position_valid(valid):
    assert extract_position(valid) == "239.84629"
