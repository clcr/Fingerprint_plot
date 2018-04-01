import numpy as np
import matplotlib.pyplot as plt
import csv
from datetime import datetime


def fingerprint_plot(solar_timeseries):
    headings = solar_timeseries[0]
    solar_timeseries = solar_timeseries[1:]
    date_view = solar_timeseries[:, 1]
    data_view = solar_timeseries[:, 2]  # Watch out for date_ and data_
    dates = [np.datetime64(dt) for dt in date_view]
    time_res = dates[1] - dates[0]
    y_axis = np.arange(np.timedelta64('00', 'h'), np.timedelta64('24', 'h'), time_res)
    x_axis = np.arange(dates[0], dates[-1], np.timedelta64('1', 'D'))
    surf = data_view.reshape([x_axis.size, y_axis.size])
    iris_plot = plt.contourf(x_axis, y_axis, surf)
    plt.show()


def load_solar_data(csv_filepath):
    with open(csv_filepath, 'r') as csv_file:
        reader = csv.reader(csv_file)
        out = [row for row in reader]
    return np.array(out)


if __name__ == "__main__":
    data = load_solar_data()
    fingerprint_plot(data)
