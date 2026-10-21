# Filtering and Subsystem Relational Analysis

Please see the main repository README for a project summary. 
Open `Filtering_Analysis.ipynb` to view the full pipeline.

## Usage
This directory contains three `.npy` arrays containing the linear systems:
* `A_array.npy`: The A matrices for 10 different systems.
* `b_array.npy`: The b matrices for 10 different systems.
* `solutions_array.npy`: The solutions for 10 different systems.

You can use `load_system.py` to load and print a specific system. Set the `index` variable (0 to 9) in the script to select a system, then run it. The script will print the system matrix, the b vector, and the formatted linear equations.
