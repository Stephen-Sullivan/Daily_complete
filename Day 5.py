# Day 5 assignment adding ability to quit   
# Stephen Sullivan (100526624)
# TPRG2131
# September 19th 2023 
# This program is strictly my own work. Any material 
# beyond course learning materials that is taken from 
# the Web or other sources is properly cited, giving 
# credit to the original author(s). 
# The program calculates resonant frequency, bandwidth,
# Q factor, parallel resistance and RC time constance
# The program can now quit with a case insensative "q"


import math

# Function to calculate series LCR values
def calculate_series_lrc(inductance, capacitance, resistance):
    resonant_frequency = 1 / (2 * math.pi * math.sqrt(inductance * capacitance))
    bandwidth = resistance / (2 * math.pi * inductance)
    q_factor = 1 / resistance * math.sqrt(inductance / capacitance)
    return resonant_frequency, bandwidth, q_factor

# Function to calculate parallel resistance
def calculate_parallel_resistance(resistor1, resistor2):
    parallel_resistance = 1 / ((1 / resistor1) + (1 / resistor2))
    return parallel_resistance

# Function to calculate RC time constant
def calculate_rc_time_constant(resistor, capacitance):
    rc_time_constant = resistor * (capacitance / 1000000 )
    return rc_time_constant

# Function to calculate series resistance
def calculate_series_resistance(resistor1, resistor2):
    series_resistance = resistor1 + resistor2
    return series_resistance

# Main program
print("LCR and RC Calculator")

while True:
    print("Select an option:")
    print("1. Calculate Series LCR")
    print("2. Calculate Parallel Resistance")
    print("3. Calculate RC Time Constant")
    print("4. Calculate Series Resistance")
    print("5. Quit")


    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '5' or choice.lower() == "q":
        # Quit the program
        break

    if choice == '1':
        try:
            # Calculate Series LCR
            inductance_mH = float(input("What is the inductance in mH? "))
            capacitance_uF = float(input("What is the capacitance in uF? "))
            resistance_ohms = float(input("What is the resistance in ohms? "))

            resonant_freq, bandwidth, q_factor = calculate_series_lrc(inductance_mH / 1000, capacitance_uF / 1000000, resistance_ohms)

            print("Resonant Frequency: {:.3f} Hz".format(resonant_freq))
            print("Bandwidth: {:.3f} Hz".format(bandwidth))
            print("Q Factor: {:.3f}".format(q_factor))
        except ValueError:
            print("Invalid input. Please enter valid numeric values.")
    
    elif choice == '2':
        try:
            # Calculate Parallel Resistance
            resistor1 = float(input("Enter the value of the first resistor in ohms: "))
            resistor2 = float(input("Enter the value of the second resistor in ohms: "))

            parallel_resistance = calculate_parallel_resistance(resistor1, resistor2)
            print("Parallel Resistance: {:.2f} ohms".format(parallel_resistance))
        except ValueError:
            print("Invalid input. Please enter valid numeric values.")

    elif choice == '3':
        try:
            # Calculate RC Time Constant
            resistor = float(input("Enter the resistor value in ohms: "))
            capacitance = float(input("Enter the capacitance value in uF: "))

            rc_time_constant = calculate_rc_time_constant(resistor, capacitance)
            print("RC Time Constant: {:.3f} seconds".format(rc_time_constant))
        except ValueError:
            print("Invalid input. Please enter valid numeric values.")

    elif choice == '4':
        try:
            # Calculate Series Resistance
            resistor1 = float(input("Enter the value of the first resistor in ohms: "))
            resistor2 = float(input("Enter the value of the second resistor in ohms: "))

            series_resistance = calculate_series_resistance(resistor1, resistor2)
            print("Series Resistance: {:.2f} ohms".format(series_resistance))
        except ValueError:
            print("Invalid input. Please enter valid numeric values.")

    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")
    
    print("\n")
