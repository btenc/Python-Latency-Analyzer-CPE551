# Python Latency Analyzer - CPE551 Group Project F25

# Group Members: : William TenCate (wtencate@stevens.edu) & Johnathan Vu (jvu2@stevens.edu)

## The problem:

Due to the offloading of many programs and data systems into the cloud, stable connections between a user and server are more critical than ever. Latency, described as the delay between a request and response between a user and server, is a key indicator that affects the experience and performance of an online system. Additionally, dropped packets, which is information lost in the transfer between the client and server, can lead to data loss, failed connections, or unusable system experiences.
Measuring and analyzing latency and connection stability provides an important KPI (key performance indicator) and allows the ability to diagnose connectivity issues and determine whether the client connection or server connection are weak. Therefore, our project proposal is a “Web Latency Analysis Tool”, implemented in Python to measure response times between user inputted and default testing domains, saving the results between tests in a cumulative CSV file for analysis.

## Program Structure:

This program measures latency tests for a given URL and saves the testing session results to a results file that is cumulative with previous tests ran.

The results file is loaded in to the `main.ipynb` file, so it can be used to compare, review, and visualize tests that have been completed.

- `notebook/main.ipynb` is the main entry point of the program, and what is used to interface with all other modules.

- `results/` is where the results.csv file will be written to and loaded from, whether or not the file exists yet.

- `tests/` is where the Pytest testing module is.

### SRC folder.

All other `.py` source code is located in the `src/` directory.

- `src/latency/` holds the latency testing modules that use requests to perform latency tests on the designated URL, handled by a class that is saved to the results file.

- `src/analysis/` holds the modules that perform data manipulation on the results file, cumulatively summarizing different results by URL or a comparison between multiple.

- `src/utils/` holds helper functions that are used to validate input, and safely handle writing to and managing the `./results/results.csv file, and more.

### Other info.

**Important: There is no CSV provided (since the results are dependant on local connection), you must run the preload / seeding cell or run some testing sessions first.**

The only file you need to use is `src/notebook/main.ipynb`, which is the connecter for all other modules and data files.

There are also test cases in `src/tests` using Pytest. To run these, just type `pytest` into the console while in the project directory after installing dependencies, since the file is named with `test_` it will automatically run.

All user input is sanitized and includes exception handling from a helper function in `src/utils/helpers.py`

## HOW TO USE!

Install dependencies: `pip install -r requirements.txt`

Program entry point (run this file): `src/notebook/main.ipynb`

Program Instructions:

1. Run the setup cell to import needed modules.
2. If needed, run **the seeding cell** to preload the results file with test sessions.
3. Run **test session cell** to be prompted and enter a URL to run and save a session of the testing session into the results file. (The session is saved with session averages, not individual tests).
4. Run cells to view data from the results file in meaningful visual ways and comparisons.
5. There are also helper cells for clearing the saved results, or removing all tests with a specific label, url, etc.

## Team Member (Main Contributions) (We both kinda worked on everything)

### William

- Project file structure and program flow planning.
- `src/latency` modules
- `src/utils` input cleaning and validation, `results/results.csv` CSV R/W logic.
- `src/latency` implementation into `notebook/main.ipynb`

### Johnathan

- `src/analysis` modules
- `src/analysis` implementation into `notebook/main.ipynb`
- `src/utils` read_latency_csv helper function

## References Used

https://docs.python.org/3/reference/import.html#package-relative-imports

https://docs.python-requests.org/en/latest/index.html

https://www.geeksforgeeks.org/python/what-is-__init__-py-file-in-python/
https://stackoverflow.com/questions/52119454/how-to-obtain-jupyter-notebooks-path

https://www.geeksforgeeks.org/python/what-is-__init__-py-file-in-python/

https://docs.python.org/3/library/os.html
