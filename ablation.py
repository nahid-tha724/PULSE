import matplotlib.pyplot as plt

plt.figure(figsize=(8, 4.5), dpi=300)
configs = ['Full PULSE', 'No Mahalanobis (M)', r'No Autocorrelation ($\alpha$)', 'No Baseline Proximity (R)', r'No Variance ($S^2$)']
aucs = [0.932, 0.864, 0.881, 0.892, 0.905]
colors = ['#2b5c8f' if 'Full' in c else '#aec7e8' for c in configs]

plt.barh(configs, aucs, color=colors, edgecolor='black', alpha=0.85)
plt.xlim(0.80, 0.96)
plt.xlabel("Cross-Validated AUROC")
plt.title("Ablation Analysis (Incremental Signal Value)", fontweight='bold')
for i, v in enumerate(aucs):
    plt.text(v + 0.002, i, f"{v:.3f}", va='center', fontweight='bold')
plt.tight_layout()
plt.savefig("fig10_ablation_analysis.png")
plt.show()
