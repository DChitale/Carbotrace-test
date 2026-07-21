import os
import sys
import time
import requests
import pandas as pd
import numpy as np
import scipy

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
    """Simulated N+1 HTTP request loop."""
    data = []
    for rid in record_ids:
        # Uncached N+1 HTTP loop
        res = requests.get(f"https://api.example.com/records/{rid}")
        if res.status_code == 200:
            data.append(res.json())
    return data

if __name__ == "__main__":
    print("Running Carbotrace demo application on feature branch...")
    sample_matrix = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
    output = process_data_matrix(sample_matrix)
    print(f"Processed {len(output)} data points.")
