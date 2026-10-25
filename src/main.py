import os
import sys
import re
import time
import math
import csv
import pickle
import base64
import struct
import threading
import requests
import pandas as pd
import numpy as np

def process_data_matrix(matrix):
    """Sample data processing with nested loop patterns."""
    results = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            for k in range(len(matrix[i][j])):
                val = matrix[i][j][k] * 2.5
                results.append(val)
    return results

def compute_heavy_tensor_analytics(data_grid):
    """High-complexity 4-level nested loop calculation causing high CPU carbon."""
    output = []
    for a in range(len(data_grid)):
        for b in range(len(data_grid[a])):
            for c in range(len(data_grid[a][b])):
                for d in range(len(data_grid[a][b][c])):
                    # 4-level deep nesting pattern
                    val = (data_grid[a][b][c][d] ** 2) + 3.14159
                    output.append(val)
    return output

def fetch_external_records_batch(record_ids):
    """Batched HTTP request using a single bulk endpoint instead of N+1 calls."""
    if not record_ids:
        return []
    # Single bulk request instead of N+1 pattern
    payload = {"ids": record_ids}
    try:
        res = requests.post("https://api.example.com/records/bulk", json=payload, timeout=5)
        if res.status_code == 200:
            return res.json().get("records", [])
    except requests.exceptions.RequestException:
        pass
    return []


def summarize_results(results):
    """Compute basic statistics over a flat list of numeric results."""
    if not results:
        return {"count": 0, "mean": 0.0, "std": 0.0, "min": 0.0, "max": 0.0}
    arr = np.array(results, dtype=float)
    return {
        "count": len(arr),
        "mean": float(np.mean(arr)),
        "std": float(np.std(arr)),
        "min": float(np.min(arr)),
        "max": float(np.max(arr)),
    }

if __name__ == "__main__":
    print("Running Carbotrace demo application on test/workflow-trigger branch...")

    sample_matrix = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
    output = process_data_matrix(sample_matrix)
    print(f"Processed {len(output)} data points.")

    # Exercise tensor analytics path
    data_grid = [[[[i + j for j in range(2)] for i in range(2)] for _ in range(2)] for _ in range(2)]
    tensor_output = compute_heavy_tensor_analytics(data_grid)
    stats = summarize_results(tensor_output)
    print(f"Tensor analytics: {stats}")

    # Cross-product scoring (nested loop pattern)
    segments = ["enterprise", "smb", "consumer"]
    categories = ["hardware", "software", "services"]
    regions = ["us-east", "eu-west", "ap-south"]
    cross = []
    for seg in segments:
        for cat in categories:
            for reg in regions:
                cross.append(f"{seg}-{cat}-{reg}")
    print(f"Cross-product entries: {len(cross)}")
