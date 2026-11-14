import pytest
from fare import fare_cents


def test_short_trip_adult_pays_base_fare():
    # Arrange
    distance_km = 3
    # Act
    result = fare_cents(distance_km, "adult")
    # Assert
    assert result == 200

def test_exactly_5_km_is_still_base_fare():
    assert fare_cents(5, "adult") == 200


def test_each_extra_km_costs_50_cents():
    assert fare_cents(8, "adult") == 350


def test_student_pays_half():
    assert fare_cents(8, "student") == 175


def test_child_rides_free():
    assert fare_cents(20, "child") == 0


def test_negative_distance_raises_error():
    with pytest.raises(ValueError):
        fare_cents(-1, "adult")


def test_unknown_rider_type_raises_error():
    with pytest.raises(ValueError):
        fare_cents(3, "pilot")