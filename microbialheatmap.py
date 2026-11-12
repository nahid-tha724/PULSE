import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

np.random.seed(42)
heatmap_data = np.random.normal(0, 1, (8, 6))

plt.figure(figsize=(8, 6), dpi=300)
sns.heatmap(heatmap_data, cmap="YlGnBu", cbar=True, annot=True, fmt=".2f",
            xticklabels=[f"Sample {i}" for i in range(1, 7)],
            yticklabels=[f"Taxon {i}" for i in range(1, 9)])
plt.title("Hierarchical Microbial Feature Heatmap", fontweight='bold')
plt.tight_layout()
plt.savefig("fig7_feature_heatmap.png")
plt.show()
