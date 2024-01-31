temperature = 50
pressure = 20
rho = (
    1000
    - (1.93 * 10**-2) * temperature
    + (1.3 * 10**-4) * temperature**2
    - (9.5 * 10**-7) * temperature**3
    + (3.2 * 10**-9) * temperature**4
    + (1.93 * 10**-2) * pressure
    - (5.8 * 10**-5) * temperature * pressure
    - (4.9 * 10**-8) * temperature**2 * pressure
    + (4.1 * 10**-10) * temperature**3 * pressure
)

print(f"The density of water at {pressure} kPa and {temperature}°C is {rho:.3f} kg/m³.")
