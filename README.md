# Reparam-PA-Fit-
Interpreting Jet Precession with Position Angle Evolution 


# Position Angle Fitting using Reparameterized Sinusoidal + Linear Drift Model

## Overview
This repository contains a Python implementation for fitting the core position angle of M81* using multi-band VLBI observations. The model assumes a sinusoidal variation in position angle with additional time shifts for different frequency bands (L, C, and X).

## Repository Structure
```
/position_angle_fit
  ├── fit_position_angle.py    # Main fitting script
  ├── plot_results.py          # Plotting script
  ├── data_loader.py           # Data parsing utility
  ├── config.py                # Configuration file for tunable parameters
  ├── utils.py                 # Utility functions (if needed)
  ├── README.md                # Instructions on usage
```

## Installation & Dependencies
Ensure you have Python installed along with the required dependencies:
```bash
pip install numpy scipy matplotlib
```

## Configuration
All tunable parameters are located in `config.py`:
```python
# Initial guess for the parameters: [theta_0, A, T, d_L, d_C]
INITIAL_GUESS = [63.5, 10, 8, 2, 2]

# Parameter bounds
LOWER_BOUNDS = [50, 0, 4, -10, -10]
UPPER_BOUNDS = [70, 30, 20, 10, 10]

# Reference epoch
T0 = 1996

# Measurement error
MEASUREMENT_ERROR = 2.0
```

## Data Format
The dataset consists of position angle observations from three frequency bands. The `data_loader.py` script is designed to parse data in the following format:
```
YYYY-MM-DD   POSITION_ANGLE
```
Example:
```
2001-01-15   65.2
2003-06-23   62.8
2010-09-11   64.5
```

## Running the Fitting Script
To fit the position angle model, run:
```bash
python fit_position_angle.py
```
This will optimize the sinusoidal model parameters and store the results in `fit_parameters.npy` and `fit_uncertainties.npy`.

## Interpreting Results
Once the fitting script completes, it prints optimized parameters and uncertainties:
```
theta_0 = 63.45 ± 1.23
A       = 9.82 ± 2.11
T       = 7.95 ± 0.84
d_L     = 1.89 ± 0.37
d_C     = 2.12 ± 0.41
Reduced chi-square = 1.02
```

## Plotting Results
To visualize the fit, run:
```bash
python plot_results.py
```
This generates a time series plot comparing observed and fitted position angles for each band.

Customization:

Use Your Own Data: You can replace the provided dataset with your own VLBI or other observations in the correct format.

Modify Frequency Bands: The code is flexible to handle additional bands by adjusting fit_position_angle.py.

Experiment with Models: Modify the function in fit_position_angle.py to explore alternative fitting approaches.

Adjust Parameters: Update config.py to change initial guesses, parameter bounds, or error values.

## Caution
I working on the scripts to make it more robust :D

## License
Feel free to modify and use it :)

