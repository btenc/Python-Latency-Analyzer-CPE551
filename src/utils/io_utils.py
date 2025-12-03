"""
File: io_utils.py
Description: Handle appending and creating the results data file.
Author: William TenCate
Email: wtencate@stevens.edu
Created: 12/01/25
Last Edited: 12/02/25
"""

## todo: add the delete ones and clearing one?

import csv
import os
import pandas as pd

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
    Append session row to results file and creates if missing.
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

def read_latency_csv(csv_file_path=None):
    """
    Helper function for data analyzer class to read csv file and convert into pandas dataframe.
    If csv_file_path is None, defaults to results_file.
    Returns a pandas DataFrame.
    """
    csv_file_path = csv_file_path or results_file

    # Check if file exists
    if not os.path.exists(csv_file_path):
        raise FileNotFoundError(f"CSV file not found: {csv_file_path}")

    # try to read the CSV
    try:
        df = pd.read_csv(csv_file_path)
    # handle error if file is empty
    except pd.errors.EmptyDataError:
        raise ValueError(f"CSV file is empty: {csv_file_path}")
    # handle error if file can't be parsed
    except pd.errors.ParserError as e:
        raise ValueError(f"CSV file could not be parsed: {csv_file_path}\n{e}")

    # ensure all columns match required ones
    required_columns = ["url", "attempts", "successes", "failures", "min_ms", "max_ms", "avg_ms"]
    # if any required column is missing, raise error
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Missing required column '{col}' in CSV file: {csv_file_path}")

    # clean up URL column by stripping whitespace
    df["url"] = df["url"].str.strip()
    # return the dataframe
    return df
