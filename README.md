# Python Latency Analyzer - CPE551 Group Project F25: William TenCate & Johnathan Vu

This program measures latency tests for a given URL and saves the testing session results to a results file that is cumulative with previous tests ran.

The results file is loaded in to the `main.ipynb` file, so it can be used to compare, review, and visualize tests that have been completed.

**Important: There is no CSV provided (since the results are dependant on local connection), you must run the preload / seeding cell or run some testing sessions first.**

The only file you need to use is `src/notebook/main.ipynb`, which is the connecter for all other modules and data files.

There are also test cases in `src/tests` using Pytest. To run these, just type `pytest` into the console while in the project directory after installing dependencies, since the file is named with `test_` it will automatically run.

All user input is sanitized and includes exception handling from a helper function in `src/utils/helpers.py`

# HOW TO USE!

Install dependencies: `pip install -r requirements.txt`

Program entry point (run this file): `src/notebook/main.ipynb`

Program Instructions:

1. Run the setup cell to import needed modules.
2. If needed, run **the seeding cell** to preload the results file with test sessions.
3. Run **test session cell** to be prompted and enter a URL to run and save a session of the testing session into the results file. (The session is saved with session averages, not individual tests).
4. Run cells to view data from the results file in meaningful visual ways and comparisons.
5. There are also helper cells for clearing the saved results, or removing all tests with a specific label, url, etc.

# References Used

https://docs.python.org/3/reference/import.html#package-relative-imports

https://docs.python-requests.org/en/latest/index.html

https://www.geeksforgeeks.org/python/what-is-__init__-py-file-in-python/
https://stackoverflow.com/questions/52119454/how-to-obtain-jupyter-notebooks-path

https://www.geeksforgeeks.org/python/what-is-__init__-py-file-in-python/

https://docs.python.org/3/library/os.html
