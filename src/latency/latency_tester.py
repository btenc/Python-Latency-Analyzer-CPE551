"""
File: latency_tester.py
Description: URL Latency testing class,
    Send assigned amount of requests to a designated URL.
    Compute dictionary of statistics from session of tests.
    The test sessions are what is appended to the results csv file
    to then show stats.

Author: William TenCate
Email: wtencate@stevens.edu
Created: 12/01/25
Last Edited: 12/01/25
"""

import requests
import time
import datetime
from latency.result import Result


class LatencyTester:
    """
    Latency testing suite and session management / row export
    """

    def __init__(
        self, url="https://www.google.com", attempts=5, timeout=5, label="Default"
    ):
        self.url = url
        self.attempts = attempts
        self.timeout = timeout
        self.label = label
        self.run_started_at = datetime.datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )  # need to format time since it's gibberish originally
        self.results = []  # will store Result objects

    def run_tests(self):
        """
        Run test suite according to parameters set in object's instance
            (attempts is the amount of times, url is the url being tested, etc)
        This completes the "session" of tests.
        """
        attempt_number = 1

        while attempt_number <= self.attempts:
            start = time.time()

            try:
                response = requests.get(self.url, timeout=self.timeout)
                end = time.time()
                elapsed_ms = (end - start) * 1000

                # on success
                result = Result(
                    self.url, attempt_number, elapsed_ms, response.status_code, True
                )

            except Exception:
                end = time.time()
                elapsed_ms = (end - start) * 1000

                # on failure
                result = Result(self.url, attempt_number, elapsed_ms, None, False)

            self.results.append(result)
            attempt_number = attempt_number + 1

    def create_session_row(self):
        """
        Return dictionary summarizing the entire testing session.
        Note: does not return individual tests, it's a summary of the
            whole "session" of "attempts"
        """
        # list comprehension requirement
        times = [r.elapsed_ms for r in self.results if r.ok]

        successes = len(times)
        failures = len(self.results) - successes

        if successes > 0:
            minimum = min(times)
            maximum = max(times)

            total = 0
            for t in times:
                total = total + t

            average = total / successes

            minimum = round(minimum, 2)
            maximum = round(maximum, 2)
            average = round(average, 2)
        else:
            minimum = None
            maximum = None
            average = None

        # row to be appended to CSV
        row = {
            "run_started_at": self.run_started_at,
            "label": self.label,
            "url": self.url,
            "attempts": self.attempts,
            "successes": successes,
            "failures": failures,
            "min_ms": minimum,
            "max_ms": maximum,
            "avg_ms": average,
        }

        return row

    def __str__(self):
        """
        Return summary of the session in clean format
        """
        session = self.create_session_row()

        text = (
            f"Testing Session Complete...\n"
            f"Run started at: {session['run_started_at']}\n"
            f"Label: {session['label']}\n"
            f"URL: {session['url']}\n"
            f"Attempts: {session['attempts']}\n"
            f"Successes: {session['successes']}\n"
            f"Failures: {session['failures']}\n"
            f"Min (ms): {session['min_ms']}\n"
            f"Max (ms): {session['max_ms']}\n"
            f"Avg (ms): {session['avg_ms']}"
        )

        return text
