import pytest

from flight_calculator import calculate_flight_time
# Pytest tests for calculate_flight_time

def test_calculate_flight_time_zero_weight():
    assert calculate_flight_time(0) == 180


def test_calculate_flight_time_normal_weight():
    assert calculate_flight_time(100) == 170


def test_calculate_flight_time_heavy_weight():
    assert calculate_flight_time(2500) == 0


def test_calculate_flight_time_negative_weight():
    with pytest.raises(ValueError, match="Weight cannot be negative"):
        calculate_flight_time(-1)
