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
    assert stats.less(0) == 0
    assert stats.less(3) == 0
    assert stats.less(4) == 2
    assert stats.less(3) == 0
    assert stats.less(6) == 3
    assert stats.less(10) == 5


def test_greater(stats):
    "should return 2 (6 and 9 are the only two values greater than 4)"
    assert stats.greater(0) == 5
    assert stats.greater(4) == 2
    assert stats.greater(5) == 2
    assert stats.greater(2) == 5
    assert stats.greater(3) == 3
    assert stats.greater(6) == 1
    assert stats.greater(7) == 1
    assert stats.greater(9) == 0
    assert stats.greater(10) == 0


def test_between(stats):
    "should return 4 (3, 3, 4 and 6 are between 3 and 6)"
    assert stats.between(3, 6) == 4
    assert stats.between(3, 9) == 5
    assert stats.between(2, 10) == 5
    assert stats.between(4, 9) == 3
