from datacapture import DataCapture

def test_add():
    capture = DataCapture()
    capture.add(3)
    capture.add(9)
    capture.add(3)
    capture.add(4)
    capture.add(6)
    stats = capture.build_stats()
    assert stats.less(4) == 2 # should return 2 (only two values 3, 3 are less than 4)
    assert stats.between(3, 6) == 4 # should return 4 (3, 3, 4 and 6 are between 3 and 6)
    assert stats.greater(4) == 2 # should return 2 (6 and 9 are the only two values greater
    # than 4)
