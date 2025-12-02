"""
File: io_utils.py
Description: Handle appending and creating the results data file.
Author: William TenCate
Email: wtencate@stevens.edu
Created: 12/01/25
Last Edited: 12/01/25
"""

## todo: add the delete ones and clearing one?

import csv
import os

here = os.path.dirname(os.path.abspath(__file__))  # cd to current directory
project_root = os.path.join(
    here, "..", ".."
)  # cd .. and then cd .. again (go up two directories from current one)
results_folder = os.path.join(
    project_root, "results"
)  # results folder is project_root/results
results_file = os.path.join(
    results_folder, "results.csv"
)  # results file is results_folder/results.csv


def append_session_row(row):
    """
    Append  session row to results file and creates if missing.
    """
    # check if file exists or not
    file_exists = os.path.exists(results_file)

    with open(results_file, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=row.keys())

        # if the file didn't exist yet, it wont have the header.
        if not file_exists:
            writer.writeheader()

        # else just simple row write
        writer.writerow(row)
