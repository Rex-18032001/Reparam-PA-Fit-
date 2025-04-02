# config.py

# Initial guess for the parameters: [theta_0, A, T, d_L, d_C]
INITIAL_GUESS = [63.5, 10, 8, 2, 2]

# Parameter bounds
LOWER_BOUNDS = [50, 0, 4, -10, -10]
UPPER_BOUNDS = [70, 30, 20, 10, 10]

# Reference epoch
T0 = 1996

# Measurement error
MEASUREMENT_ERROR = 2.0

