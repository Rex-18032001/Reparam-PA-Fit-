# Reparam-PA-Fit-
Interpreting Jet Precession with Position Angle Evolution 


# Position Angle Fitting using Reparameterized Sinusoidal + Linear Drift Model

## Overview
This repository contains a Python implementation for fitting the core position angle of M81* using multi-band VLBI observations. The model assumes a sinusoidal variation in position angle with additional time shifts for different frequency bands (L, C, and X).

## Repository Structure
```
/position_angle_fit
  ├── data_loader.py           # Data parsing utility
  ├── fit_position_angle.py    # Main fitting script
  ├── plot_results.py          # Plotting script
  ├── README.md                # Instructions on usage
```

## Installation & Dependencies
Ensure you have Python installed along with the required dependencies:
```bash
pip install numpy scipy matplotlib
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
# DATA
 Place your .txt band files (e.g., L-band.txt, C-band.txt, X-band.txt) in the directory where the scripts are located. Ensure that the files contain data formatted as shown above.

## Running the Fitting Script
To fit the position angle model, run:
```bash
python fit_position_angle.py
```
This will optimize the sinusoidal model parameters and store the results in `fit_parameters.npy` and `fit_uncertainties.npy`.

## Interpreting Results
Once the fitting script completes, it prints optimized parameters and uncertainties:
```
theta_0: 42.1678 ± 3.8534
A: 4.9340 ± 0.7862
T: 15.7105 ± 0.8118
beta: 0.7456 ± 0.0918
tl: 1975.5380 ± 1.8572
tc: 1974.3148 ± 1.7193
tx: 1975.5346 ± 1.8303
Reduced Chi-square: 4.6592
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

### Final Sequence Summary:
1️⃣ **Prepare Data**: Ensure the `.txt` files for L-band, C-band, and X-band are in the same directory as the scripts and follow the required format.  
2️⃣ **Run `data_loader.py`**: This script will parse and load the position angle data from your files.  
3️⃣ **Run `fit_position_angle.py`**: Executes the fitting process, optimizing parameters for the sinusoidal + linear drift model.  
4️⃣ **Check Fitted Parameters**: Review the output values and uncertainties to assess the fit quality.  
5️⃣ **Run `plot_results.py`**: Generate plots to visualize the position angle evolution and the model fit.  


## Caution
I working on the scripts to make it more robust :D

## License
Feel free to modify and use it :)

