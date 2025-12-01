# LatencyTester class. Should take a domain, send the requests, and measure the time. Repeat tests, etc. Uses result objects and basically will have an attribute that is a list of result objects. This object will get appended to CSV.


import requests
import time
import datetime
from latency.result import Result


class LatencyTester:
    def __init__(self, url, attempts=5, timeout=5, label="Default"):
        self.url = url
        self.attempts = attempts
        self.timeout = timeout
        self.label = label
        self.run_started_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.results = []  # will store Result objects

    def run_tests(self):
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

    def create_summary_row(self):
        times = []

        for r in self.results:
            if r.ok:
                times.append(r.elapsed_ms)

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
