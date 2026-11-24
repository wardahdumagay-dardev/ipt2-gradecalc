# test_grades.py
import pytest
from grades import compute_final_grade, remark

def test_typical_scores():
    assert compute_final_grade(80, 85, 90) == pytest.approx(85.5)

@pytest.mark.parametrize("prelim, midterm, finals, expected", [
    (70, 75, 80, 75.5),
    (90, 90, 90, 90.0),
    (60, 65, 70, 65.5),
    (85, 85, 85, 85.0),
])
def test_compute_final_grade_normal(prelim, midterm, finals, expected):
    assert compute_final_grade(prelim, midterm, finals) == pytest.approx(expected)

def test_all_zero():
    assert compute_final_grade(0, 0, 0) == 0.0

def test_all_hundred():
    assert compute_final_grade(100, 100, 100) == 100.0

@pytest.mark.parametrize("final_grade, expected", [
    (74.99, "FAILED"),
    (75, "FAILED"),
    (75.01, "PASSED"),
    (0, "FAILED"),
    (100, "PASSED"),
])
def test_remark_boundary(final_grade, expected):
    assert remark(final_grade) == expected

@pytest.mark.parametrize("prelim, midterm, finals", [
    (-1, 80, 80), (101, 80, 80),
    (80, -1, 80), (80, 101, 80),
    (80, 80, -1), (80, 80, 101),
])
def test_invalid_scores_raise_value_error(prelim, midterm, finals):
    with pytest.raises(ValueError):
        compute_final_grade(prelim, midterm, finals)