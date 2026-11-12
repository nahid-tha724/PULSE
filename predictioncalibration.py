import matplotlib.pyplot as plt

plt.figure(figsize=(7, 4.5), dpi=300)
models = ['PULSE Dynamic', 'Day-14 Distance', 'Random Forest', 'Baseline Shannon']
brier_scores = [0.112, 0.155, 0.139, 0.224]

plt.bar(models, brier_scores, color='#4daf4a', width=0.5, edgecolor='black', alpha=0.85)
plt.ylabel("Brier Score (Lower is Better)")
plt.title("Probabilistic Prediction Calibration", fontweight='bold')
for i, v in enumerate(brier_scores):
    plt.text(i, v + 0.008, f"{v:.3f}", ha='center', fontweight='bold')
plt.ylim(0, 0.28)
plt.tight_layout()
plt.savefig("fig13_calibration.png")
plt.show()
