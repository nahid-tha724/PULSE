import matplotlib.pyplot as plt
import numpy as np

t_traj = np.array([-7, -1, 3, 7, 14, 28, 56, 84])
actual = np.array([0.15, 0.14, 0.03, 0.02, 0.04, 0.05, 0.06, 0.07])
predicted = np.array([0.15, 0.14, 0.04, 0.03, 0.05, 0.05, 0.06, 0.07])

plt.figure(figsize=(7, 4.5), dpi=300)
plt.plot(t_traj, actual, color='#e41a1c', lw=2.5, marker='o', label='Actual Abundance')
plt.plot(t_traj, predicted, color='#377eb8', lw=2.5, ls='--', marker='s', label='PULSE Predicted')
plt.axvline(0, color='gray', ls=':')
plt.title(r"Eubacterium rectale (C3035) Abundance Trajectory", fontweight='bold')
plt.xlabel("Time (Days)")
plt.ylabel("Relative Abundance")
plt.legend(frameon=True)
plt.tight_layout()
plt.savefig("fig6_eubacterium_trajectory.png")
plt.show()
