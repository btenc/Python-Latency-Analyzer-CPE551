# Python Latency Analyzer - CPE551 Group Project F25: William TenCate & Johnathan Vu

This program measures latency tests for a given URL and saves the results to a results file that saves previous tests.

The results file can be used to compare, review, and visualize tests that have been completed.

Important: There is no CSV provided, you must run the preload cell or run some testing sessions first.

# HOW TO USE!

Install dependencies: `pip install -r requirements.txt`

Program entry point: `notebooks/main.ipynb`

Program Instructions:

1. If needed, run **CELL XXXX** to preload the results file with test sessions.
2. Run **CELL XXXX** to be prompted and enter a URL to run and save a summary of the testing session into the results file. (The session is saved with session averages, not individual tests).
3. Run other cells to view data from the results file in meaningful ways and comparisons.
4. There are also cells for clearing the saved results, or removing all tests with a specific label, url, etc.

# References Used

https://docs.python.org/3/reference/import.html#package-relative-imports
https://docs.python-requests.org/en/latest/index.html
https://www.geeksforgeeks.org/python/what-is-__init__-py-file-in-python/

Edit this later but TLDR for now:

The main notebook will take in a site or multiple site urls when ran, run tests on it, then append to the local csv. The notebook then loads up that csv and uses pandas and matplotlib to show stuff about it and compare to previous tests ran.

.py files formatted by "black" for consistency.

1. Notebook file uses latency tester on user input
2. Latency Tester returns object that includes list of Result objects and maybe some other metadata
3. Notebook takes that object and appends it to the csv
4. Csv is used in next cells with pandas and matplotlib to show stuff.
