# plot_results.py
import numpy as np
import matplotlib.pyplot as plt
from config import MEASUREMENT_ERROR, T0
from fit_position_angle import position_angle_model
from data_loader import parse_data

# Load fit parameters
popt = np.load("fit_parameters.npy")

# Extract fitted parameters
theta_0, A, T, beta, tl, tc, tx = popt

# Generate time arrays for smooth plotting
fitx_L = np.linspace(1996, 2025, 500)   
fitx_C = np.linspace(1996, 2025, 500)
fitx_X = np.linspace(1996, 2025, 500)

# Compute fitted position angles for each band
yfit_L = theta_0 - A * np.sin(2 * np.pi * (fitx_L - tl) / T) + beta * (fitx_L - tl)
yfit_C = theta_0 - A * np.sin(2 * np.pi * (fitx_C - tc) / T) + beta * (fitx_C - tc)
yfit_X = theta_0 - A * np.sin(2 * np.pi * (fitx_X - tx) / T) + beta * (fitx_X - tx)

# Plot all bands with their respective fits
plt.figure(figsize=(20, 10))

# L-band
plt.errorbar(pa_core_1_7ghz_dates, pa_core_1_7ghz_PA, yerr=measurement_error, fmt='o', label='L-band Data', color='#d2691e')
plt.plot(fitx_L, yfit_L, label='L-band Fit', color='#d2691e', linestyle='-')

# C-band
plt.errorbar(pa1_dates, pa1_PA, yerr=measurement_error, fmt='o', label='C-band Data', color='#556b2f')
plt.plot(fitx_C, yfit_C, label='C-band Fit', color='#556b2f', linestyle='-')

# X-band
plt.errorbar(pa4_dates, pa4_PA, yerr=measurement_error, fmt='o', label='X-band Data', color='#4682b4')
plt.plot(fitx_X, yfit_X, label='X-band Fit', color='#4682b4', linestyle='-')

plt.xlabel("Time (year)", fontsize=28)
plt.ylabel("Core Position Angle (deg)", fontsize=28)
plt.legend(fontsize=18, loc="lower right")
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.grid(alpha=0.3)
plt.show()

#plot residuals
plt.figure(figsize=(20, 10))
plt.errorbar(all_dates, residuals, yerr=measurement_error, fmt='o', label='Residuals', color='black')
plt.axhline(0, color='red', linestyle='--', label='Zero Line')
plt.xlabel("Time (year)", fontsize=28)
plt.ylabel("Residuals (deg)", fontsize=28)
plt.legend(fontsize=18, loc="upper right")
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.grid(alpha=0.3)
plt.title("Residuals of Position Angle Fit", fontsize=28)
plt.show()

