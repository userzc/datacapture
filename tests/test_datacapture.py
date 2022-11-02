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
def capture_neg():
    "Instantiate DataCapture class"
    capture_neg = DataCapture()
    capture_neg.add(-3)
    capture_neg.add(-9)
    capture_neg.add(-3)
    capture_neg.add(-4)
    capture_neg.add(-6)
    return capture_neg


@pytest.fixture
def stats_b(capture):
    "Instantiate Stats class from filled DataCapture class"
    return capture.build_stats_b()


@pytest.fixture
def stats(capture):
    "Instantiate Stats class from filled DataCapture class"
    return capture.build_stats()


@pytest.fixture
def stats_neg(capture_neg):
    "Instantiate Stats class from filled DataCapture class"
    return capture_neg.build_stats()


@pytest.mark.xfail(
    raises=AssertionError,
    reason="Data input restrictions")
def test_add():
    "Test add validation, expected to fail"
    capture = DataCapture()
    capture.add(3.4)


def test_less_b(stats_b):
    "Should return 2 (only two values 3, 3 are less than 4)"
    assert stats_b.less(0) == 0
    assert stats_b.less(3) == 0
    assert stats_b.less(4) == 2
    assert stats_b.less(3) == 0
    assert stats_b.less(6) == 3
    assert stats_b.less(10) == 5


def test_greater_b(stats_b):
    "Should return 2 (6 and 9 are the only two values greater than 4)"
    assert stats_b.greater(0) == 5
    assert stats_b.greater(4) == 2
    assert stats_b.greater(5) == 2
    assert stats_b.greater(2) == 5
    assert stats_b.greater(3) == 3
    assert stats_b.greater(6) == 1
    assert stats_b.greater(7) == 1
    assert stats_b.greater(9) == 0
    assert stats_b.greater(10) == 0


def test_between_b(stats_b):
    "Should return 4 (3, 3, 4 and 6 are between 3 and 6)"
    assert stats_b.between(3, 6) == 4
    assert stats_b.between(3, 9) == 5
    assert stats_b.between(2, 10) == 5
    assert stats_b.between(4, 9) == 3


@pytest.mark.xfail(
    raises=KeyError,
    reason="Should fail to comply with O(1) time complexity")
def test_non_captured_less(stats):
    "Should fail to comply with O(1) time complexity"
    assert stats.less(5) == 0


def test_less(stats):
    "Should return 2 (only two values 3, 3 are less than 4)"
    assert stats.less(3) == 0
    assert stats.less(4) == 2
    assert stats.less(3) == 0
    assert stats.less(6) == 3


def test_greater(stats):
    "Should return 2 (6 and 9 are the only two values greater than 4)"
    assert stats.greater(4) == 2
    assert stats.greater(3) == 3
    assert stats.greater(6) == 1
    assert stats.greater(9) == 0


def test_between(stats):
    "Should return 4 (3, 3, 4 and 6 are between 3 and 6)"
    assert stats.between(3, 6) == 4
    assert stats.between(3, 9) == 5
    assert stats.between(4, 9) == 3
    assert stats.between(3, 9) == 5


@pytest.mark.xfail(
    raises=AssertionError,
    reason="Should fail when the range is not correct")
def test_betweet_correct_range(stats):
    "Should fail when the range is not correct"
    assert stats.between(3, 9) == 5
    assert stats.between(9, 3) == 5


def test_less_neg(stats_neg):
    "Should return 2 (only two values 3, 3 are less than 4)"
    assert stats_neg.less(-3) == 3
    assert stats_neg.less(-4) == 2
    assert stats_neg.less(-3) == 3
    assert stats_neg.less(-6) == 1


def test_greater_neg(stats_neg):
    "Should return 2 (6 and 9 are the only two values greater than 4)"
    assert stats_neg.greater(-4) == 2
    assert stats_neg.greater(-3) == 0
    assert stats_neg.greater(-6) == 3
    assert stats_neg.greater(-9) == 4


def test_between_neg(stats_neg):
    "Should return 4 (3, 3, 4 and 6 are between 3 and 6)"
    assert stats_neg.between(-6, -3) == 4
    assert stats_neg.between(-9, -3) == 5
    assert stats_neg.between(-9, -4) == 3
    assert stats_neg.between(-9, -3) == 5
