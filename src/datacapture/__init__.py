from bisect import (insort, bisect_left, bisect_right)
from collections import Counter


class Stats:
    def __init__(self, sorted_data):
        "Stats constructor"
        self.counter = Counter(sorted_data)
        self.keys = list(self.counter)
        print(f'keys: {self.keys}')
        print(f'counter: {self.counter}')
        acc = 0
        for key in self.keys:
            self.counter[key] += acc
            acc = self.counter[key]
        self.total = acc
        print(f'updated counter: {self.counter}')

    def less(self, value):
        "Return number of elements less than value"
        idx = bisect_left(self.keys, value)
        print(f'idx: {idx}')
        print(f'key: {self.keys[idx]}')
        return self.counter[self.keys[idx - 1]] if idx > 0 else 0

    def greater(self, value):
        "Return number of elements greater than value"
        idx = bisect_right(self.keys, value)
        print(f'idx: {idx}')
        print(f'key: {self.keys[idx]}')
        return self.total - self.counter[self.keys[idx - 1]] if idx > 0 else 0

    def between(self, low, upper):
        return self.less(upper + 1) - self.greater(low - 1)


class DataCapture:
    def __init__(self):
        "DataCapture constructor"
        self.data_elems = []
        # self.set_elems = set()

    def add(self, elem):
        # self.data_elems.append(elem)
        insort(self.data_elems, elem)
        # self.set_elems.add(elem)

    def build_stats(self):
        "Build stats of captured data"
        return Stats(self.data_elems)
