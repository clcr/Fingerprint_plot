import numpy as np
import matplotlib.pyplot as plt
import csv
from datetime import datetime


def fingerprint_plot(solar_timeseries):
    headings = solar_timeseries[0]
    solar_timeseries = solar_timeseries[1:]

    date_view = solar_timeseries[:, 1]
    dates = [np.datetime64(dt) for dt in date_view]
    time_res = dates[1] - dates[0]
    y_axis = np.arange(np.timedelta64('00', 'h'), np.timedelta64('24', 'h'), time_res)
    x_axis = np.arange(dates[0], dates[-1], np.timedelta64('1', 'D'))

    data_view = solar_timeseries[:, 2]
    for dp in np.nditer(data_view, op_flags=['readwrite']):
        dp[...] = filter_na(dp)
    data = data_view.astype(np.float)
    surf = data.reshape([x_axis.size, y_axis.size])
    iris_plot = plt.contourf(x_axis, y_axis, surf.T)
    plt.show()


def filter_na(in_string):
    if in_string == 'NA':
        return '0'
    else:
        return in_string


def load_solar_data(csv_filepath):
    with open(csv_filepath, 'r') as csv_file:
        reader = csv.reader(csv_file)
        out = [row for row in reader]
    return np.array(out)


if __name__ == "__main__":
    data = load_solar_data()
    fingerprint_plot(data)
