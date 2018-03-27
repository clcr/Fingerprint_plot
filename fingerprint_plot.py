import numpy as np
import matplotlib.pyplot as plt
import csv


def fingerprint_plot(solar_timeseries):
    headings = solar_timeseries[0]
    solar_timeseries.delete(0)


def load_solar_data(csv_filepath):
    with open(csv_filepath, 'r') as csv_file:
        reader = csv.reader(csv_file)
        out = [row for row in reader]
    return np.array(out)


if __name__ == "__main__":
    data = load_solar_data()
    fingerprint_plot(data)