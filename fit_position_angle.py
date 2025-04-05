# fit_position_angle.py
import numpy as np
from scipy.optimize import curve_fit
from data_loader import parse_data

# Define the position angle model
def position_angle_model(t, theta_0, A, T, beta, tl, tc, tx):
    """
    Position angle model with linear drift and time shifts for L, C, and X bands.

    Parameters:
        t     : Concatenated time array for L, C, X bands.
        theta_0 : Baseline position angle (deg)
        A     : Sinusoidal amplitude (deg)
        T     : Period (years)
        beta  : Linear drift (deg/year)
        tl    : Time shift for L-band due to core shift effect
        tc    : Time shift for C-band due to core shift effect
        tx    : Time shift for X-band due to core shift effect

    Returns:
        np.array: Model predictions for L, C, X bands.
    """
    
    n_L = len(pa_core_1_7ghz_dates)
    n_C = len(pa1_dates)
    n_X = len(pa4_dates)
    
    t_L = t[:n_L]
    t_C = t[n_L:n_L + n_C]
    t_X = t[n_L + n_C:n_L + n_C + n_X]

    # L-band model
    theta_l = theta_0 - A * np.sin(2 * np.pi * (t_L - tl) / T) + beta * (t_L - tl)
    # C-band model
    theta_c = theta_0 - A * np.sin(2 * np.pi * (t_C - tc) / T) + beta * (t_C - tc)
    # X-band model
    theta_x = theta_0 - A * np.sin(2 * np.pi * (t_X - tx) / T) + beta * (t_X - tx)

    return np.concatenate([theta_l, theta_c, theta_x])


# Load observational data
pa_core_1_7ghz_dates, pa_core_1_7ghz_PA = parse_data(pa_core_1_7ghz)
pa1_dates, pa1_PA = parse_data(pa_core_cycle3C)
pa4_dates, pa4_PA = parse_data(pa_core_cycle3X)

# Concatenate all bands' data
all_dates = np.concatenate([pa_core_1_7ghz_dates, pa1_dates, pa4_dates])
all_PAs = np.concatenate([pa_core_1_7ghz_PA, pa1_PA, pa4_PA])
measurement_error = 2.0  # Uncertainty in measurements

# Initial parameter guess: [theta_0, A, T, beta, tl, tc, tx]
p0 = [65, 11, 18 ,0.5, 1990, 1993, 1996]  

# Perform curve fitting
popt, pcov = curve_fit(position_angle_model, all_dates, all_PAs, p0=p0, maxfev=100000)

# Compute fitted values and uncertainties
yfit = position_angle_model(all_dates, *popt)
perr = np.sqrt(np.diag(pcov))

# Compute reduced chi-square
residuals = (all_PAs - yfit) / measurement_error
redchi2 = np.sum(residuals**2) / (len(all_PAs) - len(popt))
# Save results
np.save("fit_parameters.npy", popt)
np.save("fit_uncertainties.npy", perr)
# Print results
print("Fitted parameters:")
print(f"theta_0: {popt[0]:.4f} ± {perr[0]:.4f}")
print(f"A: {popt[1]:.4f} ± {perr[1]:.4f}")
print(f"T: {popt[2]:.4f} ± {perr[2]:.4f}")
print(f"beta: {popt[3]:.4f} ± {perr[3]:.4f}")
print(f"tl: {popt[4]:.4f} ± {perr[4]:.4f}")
print(f"tc: {popt[5]:.4f} ± {perr[5]:.4f}")
print(f"tx: {popt[6]:.4f} ± {perr[6]:.4f}")
print(f"Reduced Chi-square: {redchi2:.4f}")



