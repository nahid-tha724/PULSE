import matplotlib.pyplot as plt

days_f = [1, 7, 28, 84]
tax_d = [0.88, 0.72, 0.45, 0.31]
func_d = [0.74, 0.48, 0.21, 0.09]

plt.figure(figsize=(8, 4.5), dpi=300)
plt.plot(days_f, tax_d, marker='o', color='#e41a1c', lw=2.5, label='Taxonomic Bray-Curtis Distance')
plt.plot(days_f, func_d, marker='s', color='#377eb8', lw=2.5, label='Functional Pathway Distance (HUMAnN4)')
plt.title("Taxonomic vs. Functional Metabolic Recovery Divergence", fontweight='bold')
plt.xlabel("Days Post-Antibiotic Cessation")
plt.ylabel("Dissimilarity from Baseline")
plt.legend(frameon=True)
plt.tight_layout()
plt.savefig("fig12_functional_recovery.png")
plt.show()
