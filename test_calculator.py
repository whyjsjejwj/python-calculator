import pytest
from calculator import add, subtract, multiply, divide

@pytest.mark.basic
def test_add_basic():
    assert add(1, 2) == 3


@pytest.mark.basic
def test_subtract_basic():
    assert subtract(5, 3) == 2


@pytest.mark.edge
def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)


@pytest.mark.edge
def test_large_numbers():
    assert multiply(100000, 200000) == 20000000000


@pytest.mark.slow
def test_performance_add(benchmark):
    result = benchmark(add, 1000, 2000)
    assert result == 3000
