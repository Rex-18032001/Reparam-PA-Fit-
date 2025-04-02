# plot_results.py
import numpy as np
import matplotlib.pyplot as plt
from config import MEASUREMENT_ERROR, T0
from fit_position_angle import position_angle_model
from data_loader import parse_data

# Load fit parameters
popt = np.load("fit_parameters.npy")

# Define function for individual band plotting
def position_angle_model_band(t, theta_0, A, T, d, t0=T0):
    beta = 0.5
    return theta_0 + A * np.sin(2 * np.pi * (t - (t0 + d)) / T) + beta * (t - (t0 + d))

# Generate plot
plt.figure(figsize=(20, 10))
colors = ["#d2691e", "#556b2f", "#4682b4"]
labels = ["L-band", "C-band", "X-band"]
band_offsets = [0, popt[3], popt[4]]

for dates, PA, color, label, d in zip(
        [pa_L_dates, pa_C_dates, pa_X_dates],
        [pa_L_PA, pa_C_PA, pa_X_PA],
        colors,
        labels,
        band_offsets):

    plt.errorbar(dates, PA, yerr=MEASUREMENT_ERROR, fmt="o", markersize=8, color=color, ecolor="black", label=f"Data {label}")
    fit_x = np.linspace(1996, 2025, 500)
    fit_y = position_angle_model_band(fit_x, *popt[:3], d)
    plt.plot(fit_x, fit_y, color=color, linewidth=3, label=f"Fit {label}")

plt.xlabel("Time (year)")
plt.ylabel("Core Position Angle (deg)")
plt.legend()
plt.grid()
plt.show()

