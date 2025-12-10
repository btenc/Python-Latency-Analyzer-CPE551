"""
File: test_latency_tester.py
Description: Test latency_tester.py and result.py using pytest
Author: William TenCate
Email: wtencate@stevens.edu
Created: 12/01/25
Last Edited: 12/09/25
"""

import pytest
import sys
import os
import tempfile

here = os.path.dirname(os.path.abspath(__file__))  # cd to this file
src_path = os.path.join(here, "..", "src")  # cd .. (up one directory) then cd src

# Have to do this way instead of hardcoding path so will work on any machine
sys.path.append(src_path)  # let python search for modules inside of src folder.


from latency.latency_tester import LatencyTester
from analysis.data_analyzer import DataAnalyzer


def test_real_url():
    tester = LatencyTester("https://www.google.com", attempts=2)
    tester.run_tests()
    session = tester.create_session_row()

    assert session["url"] == "https://www.google.com"
    assert session["attempts"] == 2
    assert session["successes"] == 2
    assert session["failures"] == 0


def test_fake_url():
    tester = LatencyTester("https://shflksdjflks.com", attempts=2)
    tester.run_tests()
    session = tester.create_session_row()

    assert session["url"] == "https://shflksdjflks.com"
    assert session["attempts"] == 2
    assert session["successes"] == 0
    assert session["failures"] == 2

def test_missing_file():
    with pytest.raises(FileNotFoundError):
        DataAnalyzer("this_file_does_not_exist.csv")

def test_empty_file():
    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".csv") as tmp:
        path = tmp.name

    try:
        with pytest.raises(ValueError):
            DataAnalyzer(path)
    finally:
        os.remove(path)