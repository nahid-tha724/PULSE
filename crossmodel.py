import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(8, 5), dpi=300)
models = ['PINN', 'LASSO', 'Q-net', 'Random Forest', 'ElasticNet', 'PULSE (Ours)']
pearson = [0.42, 0.48, 0.45, 0.52, 0.50, 0.78]
rmse = [0.12, 0.15, 0.13, 0.11, 0.12, 0.07]

x = np.arange(len(models))
fig, ax1 = plt.subplots(figsize=(8, 5), dpi=300)

ax1.bar(x, pearson, color='#aec7e8', edgecolor='black', width=0.55, label='Pearson Correlation (Left)')
ax1.set_ylabel("Pearson Correlation Coefficient")
ax1.set_xticks(x)
ax1.set_xticklabels(models, rotation=20)
ax1.set_ylim(0, 1.0)

ax2 = ax1.twinx()
ax2.plot(x, rmse, color='#d95f02', marker='s', lw=2.5, label='RMSE (Right)')
ax2.set_ylabel("Root Mean Square Error (RMSE)", color='#d95f02')
ax2.set_ylim(0, 0.20)

plt.title("Cross-Model Predictive Benchmarking", fontweight='bold')
plt.tight_layout()
plt.savefig("fig2_cross_model_benchmarking.png")
plt.show()
