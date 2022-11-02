from typing import List
from bisect import (bisect_left, bisect_right)
from collections import Counter


class Stats:
    def __init__(self, data: List[int]):
        """Stats constructor, O(n + log(n) ) time complexity, only supports
        captured data

        """
        self.counter = Counter(data)
        self.keys = list(self.counter)
        # Only this key sorting gives O(n + log(n) ) complexity
        # If data is already sorted, this could have O(n) complexity
        self.keys.sort()
        self.inv_keys = {}
        acc = 0
        for idx, key in enumerate(self.keys):
            self.counter[key] += acc
            acc = self.counter[key]
            self.inv_keys[key] = idx
        self.total = acc

    def less(self, value: int) -> int:
        """Return number of elements less than value, O(1) time complexity,
         only for values already on data

        """
        assert isinstance(value, int)
        idx = self.inv_keys[value]
        return self.counter[self.keys[idx - 1]] if idx > 0 else 0

    def greater(self, value: int) -> int:
        assert isinstance(value, int)
        """Return number of elements greater than value, O(1) time complexity,
         only for values already on data

        """
        idx = self.inv_keys[value]
        idx += 1
        return self.total - self.counter[self.keys[idx - 1]] if idx > 0 else self.total

    def between(self, low: int, upper: int) -> int:
        """Return number of elements in the [low, upper] range, O(1) time
         complexity, only for values already on data

        """
        assert low <= upper
        return self.total - self.greater(upper) - self.less(low)


class StatsB:
    def __init__(self, data: List[int]):
        """Stats constructor, O(n) time complexity, relies on bisectiion
        search, supports arbitrary data

        """
        data.sort()
        self.counter = Counter(data)
        self.keys = list(self.counter)
        acc = 0
        for key in self.keys:
            self.counter[key] += acc
            acc = self.counter[key]
        self.total = acc

    def less(self, value: float) -> int:
        """Return number of elements less than value, O(n * log(n)) time
         complexity, for any int values

        """
        idx = bisect_left(self.keys, value)
        return self.counter[self.keys[idx - 1]] if idx > 0 else 0

    def greater(self, value: float) -> int:
        """Return number of elements greater than value, O(n * log(n)) time
         complexity, for any int values

        """
        idx = bisect_right(self.keys, value)
        return self.total - self.counter[self.keys[idx - 1]] if idx > 0 else self.total

    def between(self, low: float, upper: float) -> int:
        """Return number of elements in the range [low, upper], O(n * log(n)) time
         complexity, for any int values

        """
        assert low <= upper
        return self.total - self.greater(upper) - self.less(low)


class DataCapture:
    def __init__(self):
        "DataCapture constructor"
        self.data_elems = []

    def add(self, elem: int):
        "Add elements, O(1) time complexity"
        assert isinstance(elem, int)
        self.data_elems.append(elem)

    def build_stats(self) -> Stats:
        """Build stats of captured data, O(n) time complexity, only for values
        already in data

        """
        return Stats(self.data_elems)

    def build_stats_b(self) -> StatsB:
        """Build stats of captured data, O(n) time complexity, useful for any values

        """
        return StatsB(self.data_elems)
