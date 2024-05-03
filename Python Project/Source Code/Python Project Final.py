import math

calculation_history=[] #global list variable to store calculation history

def save_to_history(calculation_name, inputs, result):
    calculation_history.append({
        "name": calculation_name,
        "inputs": inputs,
        "result": result
    })

def calculate_numerical_aperture(core_radius, refractive_index_core, refractive_index_cladding):
    # Calculate the critical angle
    critical_angle = math.asin(refractive_index_cladding / refractive_index_core)
    # Calculate the numerical aperture
    numerical_aperture = math.sqrt(refractive_index_core**2 - refractive_index_cladding**2)
    return numerical_aperture

def calculate_photon_energy(wavelength):
    # Calculate the energy of a photon using Planck's equation
    h = 6.62607015e-34  # Planck's constant in J·s
    c = 3e8  # Speed of light in m/s
    energy = h * c / wavelength
    return energy

def calculate_pulse_dispersion(material_dispersion, waveguide_dispersion, pulse_width):
    # Calculate the total dispersion
    total_dispersion = material_dispersion + waveguide_dispersion
    # Calculate the pulse spread
    pulse_spread = total_dispersion * pulse_width
    return pulse_spread

def calculate_acceptance_angle(refractive_index_core, refractive_index_cladding):
    # Calculate the acceptance angle in degrees
    acceptance_angle = math.degrees(math.asin(refractive_index_cladding / refractive_index_core))
    return acceptance_angle

def calculate_population_ratio(energy_state_1, energy_state_2, temperature):
    # Calculate the ratio of population in two states using the Boltzmann distribution
    k = 8.6173e-5  # Boltzmann constant in eV/K
    population_ratio = math.exp(-(energy_state_2 - energy_state_1) / (k * temperature))
    return population_ratio

def optical_fiber_calculation():
    print("Select an option for Optical Fiber Calculation:")
    print("1. Numerical Aperture (NA)")
    print("2. Pulse Spread Due to Dispersion")
    print("3. Acceptance Angle")
    option = input("Enter your choice: ")
    if option == "1":
        print("Numerical Aperture (NA) Calculation:")
        print("The numerical aperture (NA) of an optical fiber is a measure of its ability to gather light.")
        print("It is calculated using the formula:")
        print("NA = √(core^2 - clad^2)")
        core_radius = float(input("Enter the core radius of the optical fiber (in micrometers): "))
        refractive_index_core = float(input("Enter the refractive index of the core: "))
        refractive_index_cladding = float(input("Enter the refractive index of the cladding: "))
        if refractive_index_core > refractive_index_cladding:
            numerical_aperture = calculate_numerical_aperture(core_radius, refractive_index_core, refractive_index_cladding)
            print("Numerical Aperture:", numerical_aperture)
            save_to_history("Numerical Aperture", {"Core Radius": core_radius, "Refractive Index Core": refractive_index_core, "Refractive Index Cladding": refractive_index_cladding}, numerical_aperture)
        else:
            print("Refractive Index of Core Must be Greater Than Cladding")
    elif option == "2":
        print("Pulse Spread Due to Dispersion Calculation:")
        print("Pulse spread due to dispersion refers to the broadening of an optical pulse as it propagates through a fiber.")
        print("It is calculated using the formula:")
        print("Pulse Spread = (Material Dispersion + Waveguide Dispersion) * Pulse Width")
        # Material dispersion validation
        material_dispersion = 0
        while material_dispersion <= 0:
            material_dispersion = float(input("Enter the material dispersion (in ps/nm-km): "))
            if material_dispersion <= 0:
                print("Material dispersion must be a positive value.")
        # Waveguide dispersion validation
        waveguide_dispersion = 0
        while waveguide_dispersion <= 0:
            waveguide_dispersion = float(input("Enter the waveguide dispersion (in ps/nm-km): "))
            if waveguide_dispersion <= 0:
                print("Waveguide dispersion must be a positive value.")
        # Pulse width validation
        pulse_width = 0
        while pulse_width <= 0:
            pulse_width = float(input("Enter the pulse width (in picoseconds): "))
            if pulse_width <= 0:
                print("Pulse width must be a positive value.")
        pulse_spread = calculate_pulse_dispersion(material_dispersion, waveguide_dispersion, pulse_width)
        print("Pulse Spread (in micrometers):", pulse_spread)
        save_to_history("Pulse Spread Due to Dispersion", {"Material Dispersion": material_dispersion, "Waveguide Dispersion": waveguide_dispersion, "Pulse Width": pulse_width}, pulse_spread)
    elif option == "3":
        print("Acceptance Angle Calculation:")
        print("The acceptance angle of an optical fiber is the maximum angle at which light can enter the fiber and still be guided along the core.")
        print("It is calculated using the formula:")
        print("Acceptance Angle (θ) = arcsin(n_clad / n_core)")
        # Refractive index validation
        refractive_index_core = float(input("Enter the refractive index of the core: "))
        refractive_index_cladding = float(input("Enter the refractive index of the cladding: "))
        if refractive_index_core > refractive_index_cladding:
            acceptance_angle = calculate_acceptance_angle(refractive_index_core, refractive_index_cladding)
            print("Acceptance Angle (in degrees):", acceptance_angle)
            save_to_history("Acceptance Angle", {"Refractive Index Core": refractive_index_core, "Refractive Index Cladding": refractive_index_cladding}, acceptance_angle)
        else:
            print("Error: Refractive Index of Core must be greater than Refractive Index of Cladding")
    else:
        print("Invalid option. Please select either '1', '2' or '3'.")

def laser_calculation():
    print("Select an option:")
    print("1. Threshold Length")
    print("2. Energy Of Photon")
    print("3. Population Ratio")
    laser_option = input("Enter your choice: ")
    if laser_option == "1":
        print("Threshold Length Calculation:")
        print("The threshold length of a laser is the length of the laser cavity required to reach the threshold gain.")
        print("It is calculated using the formula:")
        print("Threshold Length (Lth) = Threshold Gain (Gth) / Material Gain Coefficient (α)")
        # Material gain coefficient validation
        material_gain = 0
        while material_gain <= 0:
            material_gain = float(input("Enter the material gain coefficient (in cm^-1): "))
            if material_gain <= 0:
                print("Material gain coefficient must be a positive value.")
        # Threshold gain validation
        threshold_gain = float(input("Enter the threshold gain of the laser (in dB/cm): "))
        threshold_length = threshold_gain / material_gain
        print("Threshold Length:", threshold_length)
        save_to_history("Threshold Length", {"Material Gain Coefficient": material_gain, "Threshold Gain": threshold_gain}, threshold_length)
    elif laser_option == '2':
        print("Photon Energy Calculation:")
        print("Calculate the energy of a photon based on its wavelength using Planck's equation.")
        # Wavelength validation
        wavelength = 0
        while wavelength <= 0:
            wavelength = float(input("Enter the wavelength of the photon (in meters): "))
            if wavelength <= 0:
                print("Wavelength must be a positive value.")
        energy = calculate_photon_energy(wavelength)
        print("Photon Energy (in Joules):", energy)
        save_to_history("Photon Energy", {"Wavelength": wavelength}, energy)
    elif laser_option == "3":
        print("Population Ratio Calculation:")
        print("Calculate the ratio of population in two energy states using the Boltzmann distribution.")
        energy_state_1 = float(input("Enter the energy of state 1 (in eV): "))
        energy_state_2 = float(input("Enter the energy of state 2 (in eV): "))
        temperature = float(input("Enter the temperature (in K): "))
        population_ratio = calculate_population_ratio(energy_state_1, energy_state_2, temperature)
        print("Population Ratio (n2/n1):", population_ratio)
        save_to_history("Population Ratio", {"Energy State 1": energy_state_1, "Energy State 2": energy_state_2, "Temperature": temperature}, population_ratio)
    else:
        print("Invalid option. Please select a valid option (1, 2, or 3).")

def display_history():
    print("Calculation History:")
    if not calculation_history:
        print("No calculations performed yet.")
    else:
        for entry in calculation_history:
            print(f"Calculation: {entry['name']}")
            print("Inputs:")
            for key, value in entry['inputs'].items():
                print(f"{key}: {value}")
            print(f"Result: {entry['result']}")
            print("\n")

def main():
    while True:
        print("Select an option:")
        print("1. Optical Fiber Calculation")
        print("2. Laser Calculation")
        print("3. Display Calculation History")
        print("4. Exit")
        option = input("Enter your choice: ")
        if option == "1":
            print("Optical Fiber Calculation:")
            optical_fiber_calculation()
        elif option == "2":
            print("Laser Calculation:")
            laser_calculation()
        elif option == "3":
            display_history()
        elif option == "4":
            print("Bye Bye 🤫🤫🧏🧏‍🗣️🗣️")
            break
        else:
            print("Invalid option. Please select either '1', '2', '3', or '4'.")


main()
