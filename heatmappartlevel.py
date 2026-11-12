import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sns.set_theme(style="white")
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Helvetica', 'Arial', 'DejaVu Sans'],
    'font.size': 10,
    'axes.labelsize': 11,
    'axes.titlesize': 12,
    'figure.dpi': 300
})

np.random.seed(42)
sample_matrix = np.random.uniform(0.1, 2.8, (4, 20))

plt.figure(figsize=(10, 4.5))
sns.heatmap(
    sample_matrix,
    cmap="YlGnBu",
    annot=True,
    fmt=".2f",
    cbar_kws={'label': 'Normalized Feature Magnitude'},
    linewidths=0.5,
    linecolor='white'
)

plt.yticks(
    ticks=[0.5, 1.5, 2.5, 3.5],
    labels=[r'Variance ($S^2$)', r'Autocorrelation ($\alpha$)', r'Proximity ($R$)', r'Mahalanobis ($M$)'],
    rotation=0
)

plt.xlabel("Participant Index (Subset $N = 20$)", fontweight='bold')
plt.ylabel("PULSE Dynamic Signals", fontweight='bold')
plt.title("Participant-Level Dynamic Feature Heatmap (Early Warning Phase)", fontweight='bold', pad=15)

plt.tight_layout()
plt.savefig("fig14_participant_heatmap.png", dpi=300, bbox_inches='tight')
plt.show()
