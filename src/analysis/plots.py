# Matplotlib helpers here. take in the dataframe from pandas.
"""
File: plots.py
Description: Matplotlib helper for data analysis,
    Take in pandas dataframe and plot graphs of latency data.
    Composition Relationship with DataAnalyzer class.
    Plots has a DataAnalyzer.
Author: Johnathan Vu
Email: jvu2@stevens.edu
Created: 12/01/25
Last Edited: 12/07/25
"""

import matplotlib.pyplot as plt
from .data_analyzer import DataAnalyzer

class Plots:
    def __init__(self, data_analyzer: DataAnalyzer):
        """
        Initializes Plots class with DataAnalyzer instance
        """
        self.data_analyzer = data_analyzer
        # compute per_url and overall stats
        self.per_url_stats = self.data_analyzer.per_url_statistics()
        self.overall_stats = self.data_analyzer.overall_statistics()

    def plot_stat(self, column: str, ylabel: str, title: str, color: str = None):
        """
        Generic bar chart for per-URL statistic.
            column: The column in per_url_stats to plot.
            ylabel: Y-axis label.
            title: Plot title.
            color: Bar color. If None, Matplotlib chooses.
        """
        # get copy of per_url Dataframe
        df = self.per_url_stats.copy()

        # check if column is actually there
        if column not in df.columns:
            raise ValueError(f"Column '{column}' not found in per_url_stats")

        # sort Dataframe by average latency in descending order
        df = df.sort_values(column, ascending=True)
        values = df[column].values
        urls = df.index

        # create the bar chart
        plt.figure(figsize=(12, max(4, len(df) * 0.5)))
        plt.barh(urls, values, color=color)
        plt.xlabel(ylabel)
        plt.title(title)

        for i, v in enumerate(values):
            plt.text(v, i, f" {v:.2f}", va="center", fontsize=9)

        plt.grid(axis='x', linestyle='--', alpha=0.5)
        plt.gca().invert_yaxis()  # largest bar on top
        plt.tight_layout()
        plt.show()
        

    def plot_performance_vs_latency(self):
        """
        Scatter plot comparing performance score to average latency.
            X-axis: Average Latency (ms)
            Y-axis: Performance Score

        High-latency, low-score URLs stand out immediately.
        Helps identify URLs that perform well despite high latency (or the opposite).
        """
        df = self.per_url_stats.copy()


        plt.figure(figsize=(10, 6))
        # create scatter plot
        plt.scatter(df["avg_latency_ms"], df["performance_score"])

        plt.xlabel("Average Latency (ms)")
        plt.ylabel("Performance Score")
        plt.title("Performance Score vs Average Latency")

        # label points to know which URL is which
        for url, row in df.iterrows():
            plt.annotate(url, (row["avg_latency_ms"], row["performance_score"]),
                        textcoords="offset points", xytext=(5, 3), fontsize=8)

        plt.tight_layout()
        plt.show()
    
    def plot_success_rate(self):
        """
        Bar chart of success rate per URL
            X: Each URL
            Y: Success Rate
        """
        self.plot_stat(
            column="success_rate",
            ylabel="Success Rate (%)",
            title="Success Rate per URL",
            color="#006400"
        )

    def plot_avg_latency(self):
        """
        Bar chart of average latency per URL
            X: Each URL
            Y: Average latency
        """
        self.plot_stat(
            column="avg_latency_ms",
            ylabel="Average Latency (ms)",
            title="Average Latency per URL",
            color="#8B0000"
        )

    def plot_latency_range(self):
        """
        Bar chart of latency range per URL
            X: Each URL
            Y: Latency Range
        """
        self.plot_stat(
            column="latency_range_ms",
            ylabel="Latency Range (ms)",
            title="Latency Range per URL",
            color="#4B0082"
        )

    def plot_cv_latency(self):
        """
        Bar chart of latency consistency per URL
            X: Each URL
            Y: Coefficient of Variation
        """
        self.plot_stat(
            column="cv_latency",
            ylabel="Coefficient of Variation (%)",
            title="Latency Consistency per URL",
            color="#00008B"
        )

    def plot_performance_score(self):
        """
        Bar chart of performance score per URL
            X: Each URL
            Y: Performance score
        """
        self.plot_stat(
            column="performance_score",
            ylabel="Performance Score",
            title="Performance Score per URL",
            color="#FF8C00"
        )