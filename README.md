# Description

In this repository there is a python class to generate a DataCapture
python object that accepts numbers and returns an object for querying
statistics about the inputs. Specifically, the returned object
supports querying how many numbers in the collection are less than a
value, greater than a value, or within a range.

# Usage

``` python
capture = DataCapture()
capture.add(3)
capture.add(9)
capture.add(3)
capture.add(4)
capture.add(6)
stats = capture.build_stats()
stats.less(4)
stats.between(3, 6)
stats.greater(4)
```

## Note

The class has two different stats objects:

* `Stats`, on which the methods are $O(1)$ time complexity based on range query algorithms, but only works for data already captured.
* `StatsB`, on which the methods are $O(log(n))$ time complexity based on bisect algorithms, any int value.

# Tests

## Environment setup
To run the tests, it is recommended create a test python environment using too
development was made using [`virtualenvwrapper`](https://virtualenvwrapper.readthedocs.io/en/latest/).

The first time the environment is created we can run:

``` shell
mkvirtualenv datacapture
pip install -r requirements
```

once the environment is set, to work on it again we can use:

``` shell
workon datacapture
```

### Test execution

At the repo root, run the tests with:

``` shell
PYTHONPATH=src/ pytest -v
```
