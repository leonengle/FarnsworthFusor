import numpy as np
import matplotlib.pyplot as plt

# Hardcoded resistor value (ohms)
R4 = 470e3

# Sweep R5 (log scale is more useful)
R5_values = np.logspace(4, 7, 200)  # 1k to 10M

# Constants
V_EN_RISING = 1.45
V_EN_FALLING = 1.12

def parallel(Ra, Rb):
    return (Ra * Rb) / (Ra + Rb)

V_rising = []
V_falling = []

for R5 in R5_values:
    Req_rising = parallel(1.8e6, R5)
    Req_falling = parallel(2.8e6, R5)

    V_rising.append((1 + R4 / Req_rising) * V_EN_RISING)
    V_falling.append((1 + R4 / Req_falling) * V_EN_FALLING)

r5_guess = 33e3  # Initial guess for R5
Req_rising = parallel(1.8e6, r5_guess)
Req_falling = parallel(2.8e6, r5_guess)

V_rising_guess = (1 + R4 / Req_rising) * V_EN_RISING
V_falling_guess = (1 + R4 / Req_falling) * V_EN_FALLING

print(f"R5 = {r5_guess:.2e} Ω: V_INUV Rising = {V_rising_guess:.3f} V, V_INUV Falling = {V_falling_guess:.3f} V")

# Plot
plt.figure()
plt.plot(R5_values, V_rising, label="V_INUV Rising")
plt.plot(R5_values, V_falling, label="V_INUV Falling")

plt.xscale('log')
plt.xlabel("R5 (Ohms)")
plt.ylabel("Voltage (V)")
plt.title(f"UVLO Threshold vs R5 (R4 = {R4:.0f} Ω)")
plt.legend()
plt.grid(True)

plt.show()