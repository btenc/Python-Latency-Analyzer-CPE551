import sys
import os

here = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(here, "..", "src")

# Have to do this way instead of hardcoding path so will work on any machine
sys.path.append(src_path)

from latency.latency_tester import LatencyTester

tester = LatencyTester("https://www.google.com", attempts=3, label="Wifi")
tester.run_tests()

print(tester.create_summary_row())

tester2 = LatencyTester("https://www.gosldhjflkjsd.com", attempts=3, label="Ethernet")
tester2.run_tests()

print(tester2.create_summary_row())
