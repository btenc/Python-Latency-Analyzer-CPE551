# DataAnalyzer class. Take in CSV from the data folder and then use pandas to do sstuff to it. 
"""
File: data_analyzer.py
Description: Data analysis class,
    Generate meaningful statistics from collected latency data.
Author: Johnathan Vu
Email: jvu2@stevens.edu
Created: 12/01/25
Last Edited: 12/02/25
"""

import pandas as pd
from utils.io_utils import read_latency_csv

class DataAnalyzer:
    def __init__(self, csv_file_path="../results/results.csv"):
        """
        Initializes DataAnalyzer with latency data from a csv file
        """
        self.csv_file_path = csv_file_path
        # use helper function to read csv file and handle any errors
        self.data = read_latency_csv(csv_file_path)
        
    def per_url_statistics(self):
        """
        Generate meaningful statistics for each URL tested.
        Returns a pandas DataFrame with statistics per URL.
            - Total Attempts
            - Total Successes
            - Total Failures
            - Success Rate (%)
            - Failure Rate (%)
            - Minimum Latency (ms)
            - Maximum Latency (ms)
            - Average Latency (ms)

        Computes additional statistics:
            - Latency range: tells us the spread of latency values. Lower is better.
            - Maximum deviation from average latency: tells us worst-case scenario compared to average. Higher is worse.
            - Coefficient of Variation for latency: shows how consistent the latency is. Lower is better.
            - Performance score: score is based on avg latency and success rate. Higher is better.
        """
        stats = self.data

        # Group data by URL and calculate stats
        per_url = stats.groupby("url").agg(
            attempts_total = ("attempts", "sum"),
            successes_total = ("successes", "sum"),
            failures_total = ("failures", "sum"),
            # special function requirement: lambda to help calculate success/failure rates
            success_rate = ("successes", lambda x: x.sum() / stats.loc[x.index, "attempts"].sum() * 100),
            failure_rate = ("failures", lambda x: x.sum() / stats.loc[x.index, "attempts"].sum() * 100),
            min_latency_ms = ("min_ms", "min"),
            max_latency_ms = ("max_ms", "max"),
            avg_latency_ms = ("avg_ms", "mean"),
            stddev_latency_ms = ("avg_ms", "std")
        )

        # Latency Range: max_latency_ms - min_latency_ms
        per_url["latency_range_ms"] = per_url["max_latency_ms"] - per_url["min_latency_ms"]
        # Maximum Deviation from Average Latency: max_latency_ms - avg_latency_ms
        per_url["max_dev_from_avg"] = per_url["max_latency_ms"] - per_url["avg_latency_ms"]
        # Coefficient of Variation for Latency: (stddev_latency_ms / avg_latency_ms) * 100
        per_url["cv_latency"] = (per_url["stddev_latency_ms"] / per_url["avg_latency_ms"]) * 100
        # Performance Score: (1000 / avg_latency_ms) * (successes_total / attempts_total)
        per_url["performance_score"] = (1000 / per_url["avg_latency_ms"]) * (per_url["successes_total"] / per_url["attempts_total"])

        return per_url
    
    def overall_statistics(self):
        """
        Generate overall statistics across all URLs tested.
        Returns a pandas Series with overall statistics.
            - Total Attempts
            - Total Successes
            - Total Failures
            - Overall Success Rate (%)
            - Overall Average Latency (ms)
            - Overall StdDev Latency (ms)
            - Minimum Latency (ms)
            - Maximum Latency (ms)
        """
        return pd.Series({
            "total_attempts": self.data["attempts"].sum(),
            "total_successes": self.data["successes"].sum(),
            "total_failures": self.data["failures"].sum(),
            "overall_success_rate": self.data["successes"].sum() / self.data["attempts"].sum() * 100,
            "overall_avg_latency_ms": self.data["avg_ms"].mean(),
            "overall_stddev_latency_ms": self.data["avg_ms"].std(),
            "min_latency_ms": self.data["min_ms"].min(),
            "max_latency_ms": self.data["max_ms"].max()
        })
    
    def __str__(self):
        """
        String representation to show per URL stats and overall stats from results data
        """
        stats = self.per_url_statistics()
        overall = self.overall_statistics()
        text = f"Data from {self.csv_file_path}\n\nOverall Stats:\n{overall.to_string()}\n\nPer-URL Stats:\n{stats.to_string(line_width=200)}"
        return text