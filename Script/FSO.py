import csv
import math
import random

data = []

# Function to convert dBm to watts
def dbm_to_watts(dbm):
    return 10 ** ((dbm - 30) / 10)

# Function to determine visibility condition
def get_visibility_condition(vis_range_km):
    if 0.1 <= vis_range_km <= 0.769:
        return "Heavy Fog"
    elif 0.77 <= vis_range_km <= 1:
        return "Light Fog"
    elif 1 < vis_range_km <2:
        return "Under Thin Fog"
    elif vis_range_km == 2:
        return "Thin Fog"
    elif 2 <= vis_range_km < 2.8:
      return "Under Haze"
    elif 2.8 <= vis_range_km <= 4:
        return "Haze"
    elif 4 < vis_range_km <= 5.8:
      return "Medium Haze"
    elif 5.8 < vis_range_km <= 10:
        return "Light Haze"
    elif 10 < vis_range_km < 18:
      return "Almost Clear Weather"
    elif 18 <= vis_range_km <= 20:
        return "Clear Weather"
    else:
        return "Unknown"
#Visibilty Loss Calc
def calculate_pointing_loss(pointing_angle, lambda_val, diameter_transmitting_m):
    theta_3d = 70 * (lambda_val) / diameter_transmitting_m
    pointing_loss = 12 * (pointing_angle / theta_3d) ** 2  # in dB
    return pointing_loss


# Generate data for the "Visibility Range" column (from 0.1 km to 20 km in 0.02 km increments)
visibility_range_values = [0.1 + 0.02 * i for i in range(int((20 - 0.1) / 0.02) + 1)]

# Constants and parameters (all converted to meters)
laser_power_dbm = 2
laser_power_watts = dbm_to_watts(laser_power_dbm)
diameter_receiving_m = 20 / 100
diameter_transmitting_m = 5 / 100
R_m = 1 * 1000

# Loop through each visibility range value
for vis_fs in visibility_range_values:
    # Determine visibility condition based on the provided criteria
    visibility_condition = get_visibility_condition(vis_fs)

    # Calculate q_FS based on the provided logic
    if vis_fs > 50:
        q_fs = 1.6
    elif 6 < vis_fs <= 50:
        q_fs = 1.3
    elif 1 < vis_fs <= 6:
        q_fs = 0.67 * vis_fs + 0.34
    elif 0.5 < vis_fs <= 1:
        q_fs = vis_fs + 0.5
    elif vis_fs <= 0.5:
        q_fs = 0
    else:
        q_fs = 0

    # Calculate beta_lambda using the updated formula
    beta_lambda = (3.91 / vis_fs) * (1550 / 550) ** (-q_fs)

    theta_mrad = 2  # Constant value of 2 mrad

    # Calculate power using beta_lambda
    power = (
        laser_power_watts
        * (diameter_receiving_m ** 2)
        * (10 ** (-beta_lambda) * (R_m / 10))
    ) / ((((diameter_transmitting_m) + (theta_mrad / 1000) * R_m)) ** 2)
    power_dB = 10 * math.log10(power)

    # Calculate pointing loss
    pointing_angle = random.uniform(1, 10)
    lambda_val = 1550  # wavelength in nanometers
    pointing_loss = calculate_pointing_loss(pointing_angle, lambda_val, diameter_transmitting_m)

    # Calculate effective power in decibels
    effective_power = power_dB - pointing_loss
    effective_power_watts = dbm_to_watts(effective_power)

    # SNR CALC BEGINS NOW
    response = 1  # Optical responsivity (R_d)
    charge_of_electron = 1.60217663e-19
    i_d = 1e-9
    B = 10e9
    T = 273
    k = 1.38e-23  # Boltzmann constant in J/K
    R_load = 1000  # Load resistance in ohms

    # Calculate SNR based on the provided formula
    i_d_squared = 2 * (charge_of_electron * B * i_d ** 2)
    i_th_squared = 2 * (charge_of_electron * power * response)
    i_sh_squared = (4 * k * T * B) / R_load

    SNR = (effective_power_watts * R_m) ** 2 / (i_d_squared + i_th_squared + i_sh_squared)
    SNR_in_Db = 10 * math.log10(power)

    # Generate a random efficiency value between 0.75 and 0.90
    efficiency_antenna = 0.85  # fixed value taken as efficiency

    # Adjust power based on efficiency
    effective_power *= efficiency_antenna

    # Append the data to the list
    data.append([vis_fs, visibility_condition, efficiency_antenna, pointing_angle, pointing_loss, effective_power, SNR_in_Db])

# Specify the CSV file name
csv_file = "FSO.csv"

# Open the CSV file in write mode
with open(csv_file, mode="w", newline="") as file:
    # Create a CSV writer object with column names
    csv_writer = csv.writer(file)
    csv_writer.writerow(["Visibility Range(in kms)", "Visibility Condition", "Efficiency", "Pointing Angle", "Pointing Loss(in dB)", "Effective Power(in dB)", "SNR (in dB)"])  # Header row

    # Write the data to the CSV file row by row
    for row in data:
        csv_writer.writerow(row)

print(f"CSV file '{csv_file}' has been created successfully.")
