import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

np.random.seed(42)
violin_data = pd.DataFrame({
    'Resilience Beta Value': np.concatenate([np.random.normal(0.68, 0.12, 100), np.random.normal(0.28, 0.09, 150)]),
    'Recovery Outcome': ['Persistent Deviation']*100 + ['Successful Recovery']*150
})

plt.figure(figsize=(7, 5), dpi=300)
sns.violinplot(data=violin_data, x='Recovery Outcome', y='Resilience Beta Value',
               hue='Recovery Outcome', order=['Successful Recovery', 'Persistent Deviation'],
               palette="muted", inner="quartile", legend=False)

plt.title("Resilience Beta Distribution by Outcome", fontweight='bold')
plt.xlabel("Day 84 Microbiome State")
plt.ylabel(r"Instability Metric ($\beta$ Value)")  # Fixed with raw string (r"") to parse LaTeX correctly
plt.tight_layout()
plt.savefig("fig8_resilience_distribution.png")
plt.show()
