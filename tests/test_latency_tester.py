"""
File: test_latency_tester.py
Description: Test latency_tester.py and result.py using pytest
Author: William TenCate
Email: wtencate@stevens.edu
Created: 12/01/25
Last Edited: 12/01/25
"""

import sys
import os

here = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(here, "..", "src")

# Have to do this way instead of hardcoding path so will work on any machine
sys.path.append(src_path)


from latency.latency_tester import LatencyTester


def test_real_url():
    tester = LatencyTester("https://www.google.com", attempts=2)
    tester.run_tests()
    summary = tester.create_summary_row()

    assert summary["url"] == "https://www.google.com"
    assert summary["attempts"] == 2
    assert summary["successes"] == 2
    assert summary["failures"] == 0


def test_fake_url():
    tester = LatencyTester("https://shflksdjflks.com", attempts=2)
    tester.run_tests()
    summary = tester.create_summary_row()

    assert summary["url"] == "https://shflksdjflks.com"
    assert summary["attempts"] == 2
    assert summary["successes"] == 0
    assert summary["failures"] == 2
