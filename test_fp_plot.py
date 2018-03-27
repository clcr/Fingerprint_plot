import fingerprint_plot as fplot

def test_fingerprint_plot():
    test_data = fplot.load_solar_data('solar.csv') # shouldn't do this normally
    fplot.fingerprint_plot(test_data)