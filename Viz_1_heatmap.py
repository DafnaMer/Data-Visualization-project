import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# read data
df = pd.read_csv('Viz_1_Heatmap.csv').reset_index()
print(df)
print('Number cells: ' + str(len(df)))

result = pd.pivot_table(df, index='Cell_Type', columns='Researcher_ID', values='Cell_Count')
result.index = pd.CategoricalIndex(result.index, categories=['Coin', 'Pouch', 'Pack'])
result.sort_index(axis=0, inplace=True)
print(result)
sns.heatmap(result)
plt.xlabel('Researcher ID')
plt.ylabel('Cell Type')
plt.title("Cell Count By Cell Type and Researcher ID")
plt.show()
