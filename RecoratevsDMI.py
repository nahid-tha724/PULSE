import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

np.random.seed(42)
x_scat = np.linspace(0.1, 0.25, 30)
y_scat = 1.5 * x_scat + np.random.normal(0.2, 0.04, 30)

plt.figure(figsize=(7, 5), dpi=300)
sns.regplot(x=x_scat, y=y_scat, color='#2b5c8f', scatter_kws={'s':30}, line_kws={'color':'#d95f02', 'lw':2})
plt.title("Recolonization Rate vs. Dynamic Instability Index (DMI)", fontweight='bold')
plt.xlabel("Recolonization Rate")
plt.ylabel("DMI Index")
plt.tight_layout()
plt.savefig("fig9_recolonization_scatter.png")
plt.show()
