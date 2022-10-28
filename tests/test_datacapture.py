import pytest
from datacapture import DataCapture


@pytest.fixture
def capture():
    "Instantiate DataCapture class"
    capture = DataCapture()
    capture.add(3)
    capture.add(9)
    capture.add(3)
    capture.add(4)
    capture.add(6)
    return capture


@pytest.fixture
def stats(capture):
    "Instantiate Stats class from filled DataCapture class"
    return capture.build_stats()


def test_less(stats):
    "should return 2 (only two values 3, 3 are less than 4)"
    assert stats.less(4) == 2


def test_greater(stats):
    "should return 2 (6 and 9 are the only two values greater than 4)"
    assert stats.greater(4) == 2


def test_between(stats):
    "should return 4 (3, 3, 4 and 6 are between 3 and 6)"
    assert stats.between(3, 6) == 4
