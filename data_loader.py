# data_loader.py
import numpy as np
from datetime import datetime

def parse_data(data):
    """
    Parse dates and position angles from the given data string.

    Parameters:
        data (str): Multiline string containing dates and position angles.

    Returns:
        np.array, np.array: Arrays of decimal years and position angles.
    """
    lines = data.strip().split("\n")
    dates, PA = [], []
    
    for line in lines:
        parts = line.split()
        date_obj = datetime.strptime(parts[0], "%Y-%m-%d")
        year = date_obj.year
        start_of_year = datetime(year, 1, 1)
        end_of_year = datetime(year + 1, 1, 1)
        decimal_year = year + (date_obj - start_of_year).total_seconds() / (end_of_year - start_of_year).total_seconds()
        dates.append(decimal_year)
        PA.append(float(parts[1]))

    return np.array(dates), np.array(PA)

