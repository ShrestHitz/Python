speed_of_light = 300000000

def calculate_energy(mass):
    energy = mass * (speed_of_light ** 2)
    return energy

mass_in_kg = float(input("Enter mass in kilograms: "))

energy_in_joules = calculate_energy(mass_in_kg)

integer_output = int(energy_in_joules)

# print(f"The energy equivalent of {mass_in_kg} kg is {integer_output} joules.")
print(integer_output)