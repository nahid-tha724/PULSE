import matplotlib.pyplot as plt
import numpy as np

t_axis = [-7, -1, 1, 3, 7, 10, 14, 21, 28, 42, 56, 70, 84, 98, 112, 140]
rec_mean = [0.05, 0.06, 0.52, 0.70, 0.62, 0.48, 0.35, 0.25, 0.18, 0.13, 0.10, 0.08, 0.07, 0.06, 0.05, 0.05]
dev_mean = [0.05, 0.07, 0.58, 0.84, 0.81, 0.77, 0.74, 0.69, 0.66, 0.63, 0.60, 0.58, 0.56, 0.55, 0.54, 0.54]

plt.figure(figsize=(8, 5), dpi=300)
plt.plot(t_axis, rec_mean, color='#2b5c8f', lw=2.5, marker='o', label='Successful Recovery ($N=41$)')
plt.plot(t_axis, dev_mean, color='#d95f02', lw=2.5, marker='s', label='Persistent Deviation ($N=24$)')
plt.axvline(0, color='gray', linestyle='--', label='Ciprofloxacin Exposure')
plt.title("Longitudinal CLR Distance Trajectories", fontweight='bold')
plt.xlabel("Time Relative to Treatment (Days)")
plt.ylabel("Euclidean Distance from Baseline (CLR)")
plt.legend(frameon=True)
plt.tight_layout()
plt.savefig("fig5_clr_trajectories.png")
plt.show()
