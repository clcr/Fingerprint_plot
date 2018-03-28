import numpy as np
import matplotlib.pyplot as plt
import csv
from datetime import datetime


def fingerprint_plot(solar_timeseries):
    headings = solar_timeseries[0]
    solar_timeseries = solar_timeseries[1:]
    # convert to datetime object
    time_format = "%Y-%m-%d %H:%M:%S"
    dateview = solar_timeseries[:, 1]
    for timestamp in np.nditer(dateview)



def load_solar_data(csv_filepath):
    with open(csv_filepath, 'r') as csv_file:
        reader = csv.reader(csv_file)
        out = [row for row in reader]
    return np.array(out)


if __name__ == "__main__":
    data = load_solar_data()
    fingerprint_plot(data)
