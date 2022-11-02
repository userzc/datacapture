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

## Stats classes

The class has two different stats objects due to the trade-off between time complexity compliance and support for non-captured values on the class methods:

### `Stats`
Obtained from `DataCapture` instance by running `capture.build_stats()`.

Methods are $O(1)$ time complexity based on *range query algorithms*, but only works for data already captured in order to comply with that restriction.

> Note: It is possible to have this class constructor to run on $O(n)$
> but it would require that the captured data would be already sorted.



### `StatsB`
Obtained from `DataCapture` instance by running `capture.build_stats_b()`.

Methods are $O(log(n))$ time complexity based on *bisect algorithms*, and can receive any float value.

> Note: The class constructor for this class has $O(n)$ time
> complexity and the class methods have $O(n * log(n))$ time
> complexity in exchange for non-captured values support.

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

At the repo root and with the environment active, run the tests with:

``` shell
PYTHONPATH=src/ pytest -v
```
