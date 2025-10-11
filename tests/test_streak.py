import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Test that an empty list returns a streak of 0."""
    assert longest_positive_streak([]) == 0

def test_no_positive_numbers():
    """Test a list with no positive numbers returns a streak of 0."""
    assert longest_positive_streak([-1, -2, 0, -5]) == 0

def test_all_positive_numbers():
    """Test a list with all positive numbers."""
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_single_streak_at_beginning():
    """Test a single streak at the beginning of the list."""
    assert longest_positive_streak([1, 2, 3, -1, -2]) == 3

def test_single_streak_at_end():
    """Test a single streak at the end of the list."""
    assert longest_positive_streak([-1, -2, 1, 2, 3, 4]) == 4

def test_multiple_streaks():
    """Test a list with multiple streaks of positive numbers."""
    assert longest_positive_streak([1, 2, -3, 4, 5, 0, 6, 7, 8, -9, 1]) == 3

def test_list_with_zeros():
    """Test a list containing zeros."""
    assert longest_positive_streak([1, 2, 0, 3, 4, 0, 5]) == 2

def test_longest_streak_is_first():
    """Test when the longest streak is the first one."""
    assert longest_positive_streak([1, 2, 3, 4, -1, 5, 6]) == 4

def test_longest_streak_is_last():
    """Test when the longest streak is the last one."""
    assert longest_positive_streak([1, 2, -1, 3, 4, 5, 6, 7]) == 5

def test_mixed_numbers():
    """Test a list with a mix of positive, negative and zero values."""
    assert longest_positive_streak([1, 0, 2, 3, -4, 5, 6, 7, 0, 8]) == 3