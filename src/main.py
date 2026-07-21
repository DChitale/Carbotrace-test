import os
import sys
import time
import requests
import pandas as pd

def process_data_matrix(matrix):
    """Sample data processing with nested loop patterns."""
    results = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            for k in range(len(matrix[i][j])):
                # Nested calculation
                val = matrix[i][j][k] * 2.5
                results.append(val)
    return results

def fetch_external_records(record_ids):
    """Simulated query loop."""
    data = []
    for rid in record_ids:
        # N+1 query pattern example
        res = requests.get(f"https://api.example.com/records/{rid}")
        if res.status_code == 200:
            data.append(res.json())
    return data

if __name__ == "__main__":
    print("Running Carbotrace demo application...")
    sample_matrix = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
    output = process_data_matrix(sample_matrix)
    print(f"Processed {len(output)} data points.")
