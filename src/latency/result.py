"""
File: result.py
Description: Result class for an individual test (every "attempt")
    in LatencyTester class.
Author: William TenCate
Email: wtencate@stevens.edu
Created: 12/01/25
Last Edited: 12/01/25
"""


class Result:
    def __init__(self, url, attempt, elapsed_ms, status_code, ok):
        self.url = url
        self.attempt = attempt
        self.elapsed_ms = elapsed_ms
        self.status_code = status_code
        self.ok = ok

    def __str__(self):  # str formatting for debug purposes
        if self.ok:
            return f"{self.url} attempt {self.attempt}: {self.elapsed_ms:.2f} ms (status {self.status_code})"
        else:
            return f"{self.url} attempt {self.attempt}: ERROR after {self.elapsed_ms:.2f} ms"
