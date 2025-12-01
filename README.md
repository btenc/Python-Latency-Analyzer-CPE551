# Python Latency Analyzer

CPE551 Group Project F25: William TenCate & Johnathan Vu

Install dependencies: `pip install -r requirements.txt`

Program entry point: `notebooks/main.ipynb`

.py files formatted by "black" for consistency.

Edit this later but TLDR for now:

The main notebook will take in a site or multiple site urls when ran, run tests on it, then append to the local csv. The notebook then loads up that csv and uses pandas and matplotlib to show stuff about it and compare to previous tests ran.

1. Notebook file uses latency tester on user input
2. Latency Tester returns object that includes list of Result objects and maybe some other metadata
3. Notebook takes that object and appends it to the csv
4. Csv is used in next cells with pandas and matplotlib to show stuff.

# References Used

https://docs.python.org/3/reference/import.html#package-relative-imports
https://docs.python-requests.org/en/latest/index.html
https://www.geeksforgeeks.org/python/what-is-__init__-py-file-in-python/
