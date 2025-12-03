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
Last Edited: 12/02/25
"""

import matplotlib.pyplot as plt
from .data_analyzer import DataAnalyzer

class Plots:
    def __init__(self, data_analyzer: DataAnalyzer):
        self.data_analyzer = data_analyzer
        self.per_url_stats = self.data_analyzer.per_url_statistics()
        self.overall_stats = self.data_analyzer.overall_statistics()

    def plot_avg_latency(self):
        """
        Bar chart of average latency per URL
            X: Each URL
            Y: Average latency
        """
        # get copy of per_url Dataframe
        df = self.per_url_stats.copy()
        # sort Dataframe by average latency in descending order
        df = df.sort_values("avg_latency_ms", ascending=False)
        # create a figure
        plt.figure(figsize=(10, 6))
        # create bar chart with x-axis: url, y-axis: avg latency
        plt.bar(df.index, df["avg_latency_ms"], color="lightskyblue")
        # label y 
        plt.ylabel("Average Latency (ms)")
        # label x
        plt.xlabel("URLs")
        # label title
        plt.title("Average Latency per URL")
        # rotate urls in x-axis for readability
        plt.xticks(rotation=45, ha="right")
        # auto adjust subplot parameters to fit nicely
        plt.tight_layout()
        # show the plot
        plt.show()

    def plot_performance_score(self):
        """
        Bar chart of performance score per URL
            X: Each URL
            Y: Performance score
        """
        # get copy of per_url Dataframe
        df = self.per_url_stats.copy()
        # sort Dataframe by performance score in descending order
        df = df.sort_values("performance_score", ascending=False)
        # create a figure
        plt.figure(figsize=(10, 6))
        # create bar chart with x-axis: url, y-axis: performance score
        plt.bar(df.index, df["performance_score"], color="wheat")
        # label y
        plt.ylabel("Performance Score")
        # label x
        plt.xlabel("URLs")
        # label title
        plt.title("Performance Score per URL")
        # rotate urls in x-axis for readability
        plt.xticks(rotation=45, ha="right")
        # auto adjust subplot parameters to fit nicely
        plt.tight_layout()
        # show the plot
        plt.show()