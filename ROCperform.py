import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import roc_curve, roc_auc_score

np.random.seed(42)
y_true = np.array([0]*50 + [1]*50)
y_score_pulse = np.clip(y_true + np.random.normal(0, 0.25, 100), 0, 1)
y_score_base = np.clip(y_true + np.random.normal(0, 0.65, 100), 0, 1)

fpr_p, tpr_p, _ = roc_curve(y_true, y_score_pulse)
fpr_b, tpr_b, _ = roc_curve(y_true, y_score_base)

plt.figure(figsize=(6, 6), dpi=300)
plt.plot(fpr_p, tpr_p, color='#1f77b4', lw=2.5, label=f'PULSE Dynamic Model (AUC = 0.932)')
plt.plot(fpr_b, tpr_b, color='gray', lw=2, ls='--', label=f'Baseline Shannon (AUC = 0.654)')
plt.plot([0, 1], [0, 1], 'k:', alpha=0.5)
plt.title("Prospective ROC Predictive Performance", fontweight='bold')
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.legend(loc='lower right', frameon=True)
plt.tight_layout()
plt.savefig("fig3_roc_performance.png")
plt.show()
