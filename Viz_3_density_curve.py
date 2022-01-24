import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# read data
df = pd.read_csv('Viz_3_density_curve.csv')
print(df)
print('Number cells: ' + str(len(df)))

sns.displot(df, x="Hc_80_Cap_Cycles_d", hue="Project", kind="kde", fill=True)
plt.xlabel('Cycles')
plt.xlim(0, )
plt.ylabel('Density')
plt.title("kernel Density Estimation (KDE) Of Cycles By Project")
plt.show()
