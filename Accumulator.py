# %%
import matplotlib.pyplot as plt
import numpy as np

N = 512
bits = 8
# Create the Input Sequence
input_values = [50] * N

# Initialize the initial State
sum1 = 0
# %%
# Create the Output by iterating through input values
dac_out = []
for sample in input_values:
    # Completre all synchronus operations
    sum1_d = sum1

    # Complete all asynchronous operations
    sum1 = sample + sum1_d

    # DAC Transaltion
    dac = 3 / 2 ** bits

    # update output
    dac_out.append(dac * sum1_d)

print(dac_out)

# %%
# Create time axis for plotting
time_samples = np.arange(N)

# Create plots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# Plot input values vs time
ax1.plot(time_samples, input_values, 'b-', linewidth=2, label='Input Signal')
ax1.set_xlabel('Sample Number')
ax1.set_ylabel('Input Value')
ax1.set_title('Input Values vs Time')
ax1.grid(True, alpha=0.3)
ax1.legend()

# Plot DAC output vs time
ax2.plot(time_samples, dac_out, 'r-', linewidth=2, label='DAC Output')
ax2.set_xlabel('Sample Number')
ax2.set_ylabel('DAC Output Value')
ax2.set_title('DAC Output vs Time')
ax2.grid(True, alpha=0.3)
ax2.legend()

# Adjust layout and show plots
plt.tight_layout()
plt.show()

# %%
# Print some statistics
print(f"Input signal statistics:")
print(f"  Mean: {np.mean(input_values):.2f}")
print(f"  Min: {np.min(input_values):.2f}")
print(f"  Max: {np.max(input_values):.2f}")
print(f"\nDAC output statistics:")
print(f"  Mean: {np.mean(dac_out):.2f}")
print(f"  Min: {np.min(dac_out):.2f}")
print(f"  Max: {np.max(dac_out):.2f}")
print(f"  Final value: {dac_out[-1]:.2f}")