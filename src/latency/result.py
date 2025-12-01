# Result class. result object is one single instance of a test. Use __str__ method. (This is basically a mini container for one instance of a test, that we can then use as a data point.)


class Result:
    def __init__(self, url, attempt, elapsed_ms, status_code, ok):
        self.url = url
        self.attempt = attempt
        self.elapsed_ms = elapsed_ms
        self.status_code = status_code
        self.ok = ok

    def __str__(self):
        if self.ok:
            return f"{self.url} attempt {self.attempt}: {self.elapsed_ms:.2f} ms (status {self.status_code})"
        else:
            return f"{self.url} attempt {self.attempt}: ERROR after {self.elapsed_ms:.2f} ms"
