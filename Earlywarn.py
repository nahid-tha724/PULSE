import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(2, 2, figsize=(10, 8), dpi=300)
t_sub = np.array([1, 3, 7, 10, 14])

axes[0, 0].plot(t_sub, [0.1, 0.45, 0.85, 0.65, 0.4], color='#d95f02', lw=2.5, marker='o')
axes[0, 0].set_title(r"A. Rolling Abundance Variance ($S^2$)")
axes[0, 0].set_ylabel("Variance (CLR Space)")

axes[0, 1].plot(t_sub, [0.05, 0.3, 0.75, 0.82, 0.68], color='#7570b3', lw=2.5, marker='s')
axes[0, 1].set_title(r"B. Temporal Autocorrelation ($\alpha$)")
axes[0, 1].set_ylabel("Lag-1 Autocorrelation")

axes[1, 0].plot(t_sub, [0.95, 0.7, 0.3, 0.4, 0.55], color='#1b9e77', lw=2.5, marker='^')
axes[1, 0].set_title(r"C. Baseline Proximity ($\Phi$)")
axes[1, 0].set_xlabel("Days Post-Antibiotic")
axes[1, 0].set_ylabel("Proximity Score")

axes[1, 1].plot(t_sub, [0.2, 0.8, 1.9, 1.6, 1.2], color='#e7298a', lw=2.5, marker='d')
axes[1, 1].set_title(r"D. Regularized Mahalanobis Distance ($M$)")
axes[1, 1].set_xlabel("Days Post-Antibiotic")
axes[1, 1].set_ylabel("Mahalanobis Displacement")

for ax in axes.flat:
    ax.grid(True, linestyle='--', alpha=0.6)

plt.suptitle("Multi-Signal Early-Warning Indicator Evolution (Days 1–14)", fontsize=13, fontweight='bold')
plt.tight_layout()
plt.savefig("fig4_multisignal_evaluation.png")
plt.show()
