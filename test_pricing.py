import pytest

from pricing import total


def test_total_without_discount():
    assert total([1.25, 2.50]) == 3.75


def test_total_with_discount():
    assert total([10.0, 10.0], discount=0.25) == 15.0


def test_rejects_bad_discount():
    with pytest.raises(ValueError):
        total([1.0], discount=1.5)
