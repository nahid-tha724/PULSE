import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(10, 4), dpi=300)
participants = [f"P{i:02d}" for i in range(1, 6)]
timepoints = [-7, -1, 1, 3, 7, 10, 14, 21, 28, 42, 56, 70, 84]

for idx, p in enumerate(participants):
    plt.plot(timepoints, [idx] * len(timepoints), marker='o', color='#2b5c8f', ls='-', lw=1.5, markersize=6)

plt.axvline(0, color='#d95f02', ls='--', lw=1.5, label='Ciprofloxacin Exposure')
plt.title("Longitudinal Participant Sampling Schema (PRJNA974858)", fontweight='bold')
plt.yticks(range(len(participants)), participants)
plt.xlabel("Days Relative to Treatment")
plt.legend(loc='upper right', frameon=True)
plt.tight_layout()
plt.savefig("fig1_sampling_schema.png")
plt.show()
