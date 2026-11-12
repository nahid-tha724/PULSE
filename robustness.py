import matplotlib.pyplot as plt

plt.figure(figsize=(7, 4.5), dpi=300)
methods = ['Standard Discrete AR(1)', 'PULSE Time-Aware AR(1)']
errors = [0.284, 0.038]

plt.bar(methods, errors, color=['#e41a1c', '#377eb8'], width=0.45, edgecolor='black', alpha=0.85)
plt.ylabel("Autocorrelation Estimation Error")
plt.title("Robustness Under Irregular Sampling Intervals", fontweight='bold')
for i, v in enumerate(errors):
    plt.text(i, v + 0.01, f"±{v:.3f}", ha='center', fontweight='bold')
plt.ylim(0, 0.35)
plt.tight_layout()
plt.savefig("fig11_robustness.png")
plt.show()
