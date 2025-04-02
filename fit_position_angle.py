# fit_position_angle.py
import numpy as np
from scipy.optimize import curve_fit
from config import INITIAL_GUESS, LOWER_BOUNDS, UPPER_BOUNDS, T0, MEASUREMENT_ERROR
from data_loader import parse_data

# Define the position angle model
def position_angle_model(t, theta_0, A, T, d_L, d_C):
    """
    Position angle model reparameterized relative to X-band.

    Parameters:
        t     : Concatenated time array for L, C, X bands.
        theta_0 : Baseline position angle (deg)
        A     : Sinusoidal amplitude (deg)
        T     : Period (years)
        d_L   : Time shift for L-band relative to X-band (years)
        d_C   : Time shift for C-band relative to X-band (years)

    Returns:
        np.array: Model predictions for L, C, X bands.
    """
    beta = 0.5  # Linear drift

    n_L, n_C, n_X = len(pa_L_dates), len(pa_C_dates), len(pa_X_dates)
    t_L, t_C, t_X = t[:n_L], t[n_L:n_L+n_C], t[n_L+n_C:]

    M_X = theta_0 + A * np.sin(2 * np.pi * (t_X - T0) / T) + beta * (t_X - T0)
    M_L = theta_0 + A * np.sin(2 * np.pi * (t_L - (T0 + d_L)) / T) + beta * (t_L - (T0 + d_L))
    M_C = theta_0 + A * np.sin(2 * np.pi * (t_C - (T0 + d_C)) / T) + beta * (t_C - (T0 + d_C))

    return np.concatenate([M_L, M_C, M_X])

# Load data (replace these with actual data files or strings)
pa_L_dates, pa_L_PA = parse_data(pa_core_1_7ghz)
pa_C_dates, pa_C_PA = parse_data(pa_core_cycle3C)
pa_X_dates, pa_X_PA = parse_data(pa_core_cycle3X)

# Prepare for fitting
all_dates = np.concatenate([pa_L_dates, pa_C_dates, pa_X_dates])
all_PAs = np.concatenate([pa_L_PA, pa_C_PA, pa_X_PA])

# Perform fitting
popt, pcov = curve_fit(position_angle_model, all_dates, all_PAs, 
                       p0=INITIAL_GUESS, bounds=(LOWER_BOUNDS, UPPER_BOUNDS), 
                       method="trf", maxfev=1000000)

# Compute uncertainties
perr = np.sqrt(np.diag(pcov))

# Compute residuals and reduced chi-square
residuals = (all_PAs - position_angle_model(all_dates, *popt)) / MEASUREMENT_ERROR
redchi = np.sum(residuals**2) / (len(all_dates) - len(popt))

# Save results
np.save("fit_parameters.npy", popt)
np.save("fit_uncertainties.npy", perr)

# Print results
print(f"theta_0 = {popt[0]:.2f} ± {perr[0]:.2f}")
print(f"A       = {popt[1]:.2f} ± {perr[1]:.2f}")
print(f"T       = {popt[2]:.2f} ± {perr[2]:.2f}")
print(f"d_L     = {popt[3]:.2f} ± {perr[3]:.2f}")
print(f"d_C     = {popt[4]:.2f} ± {perr[4]:.2f}")
print(f"Reduced chi-square = {redchi:.2f}")

