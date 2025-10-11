import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Test that an empty list returns a streak of 0."""
    assert longest_positive_streak([]) == 0

def test_multiple_streaks_longest_in_middle():
    """Test a list where the longest streak is in the middle."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_multiple_streaks_longest_is_first():
    """Test a list where the longest streak is at the beginning."""
    assert longest_positive_streak([1, 2, 3, 4, -1, 5, 6]) == 4

def test_multiple_streaks_longest_is_last():
    """Test a list where the longest streak is at the end."""
    assert longest_positive_streak([1, 2, -1, 3, 4, 5, 6, 7]) == 5

def test_with_zeros():
    """Test that zeros break the streak."""
    assert longest_positive_streak([1, 2, 0, 3, 4, 0, 5]) == 2

def test_with_negatives():
    """Test that negative numbers break the streak."""
    assert longest_positive_streak([1, 2, -3, 4, 5, -1, 1]) == 2

def test_no_positive_numbers():
    """Test a list with no positive numbers, including zeros and negatives."""
    assert longest_positive_streak([-1, -2, 0, -5]) == 0

def test_all_positive_numbers():
    """Test a list that consists only of positive numbers."""
    assert longest_positive_streak([1, 1, 1, 2, 3]) == 5

def test_single_element_list_positive():
    """Test a list with a single positive number."""
    assert longest_positive_streak([5]) == 1

def test_single_element_list_non_positive():
    """Test a list with a single non-positive number."""
    assert longest_positive_streak([-5]) == 0
    assert longest_positive_streak([0]) == 0