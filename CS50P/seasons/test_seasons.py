from seasons import year
import datetime
import re

def test_year():
    new_year = year(2000, 1, 1)
    assert new_year.year == 2000
    assert new_year.month == 1
    assert new_year.day == 1

def test_minutes():
    y = year(2000, 1, 1)
    expected_minutes = (datetime.date(2024, 8, 10) - datetime.date(2000, 1, 1)).days * 24 * 60
    assert y.getminutes() == expected_minutes
