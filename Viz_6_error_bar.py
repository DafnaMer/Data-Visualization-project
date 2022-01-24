import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.transforms import Affine2D

# read data
df = pd.read_csv('Viz_6a_error_bar.csv')
df.drop(df.index[201:], inplace=True)
df.drop([0], inplace=True)
print(df)
print('Number cells: ' + str(len(df)))

fig, ax = plt.subplots()

def errorbar_by_group(group, color, shift, label):
    sub_df = df[df.columns[df.columns.str.startswith(group)]]
    print(sub_df)
    # sub_df.dropna(how='all', inplace=True)
    sub_df[group + '-AVG'] = sub_df.apply(np.nanmean, axis=1)
    sub_df[group + '-STD'] = sub_df.apply(np.nanstd, axis=1)
    print(sub_df[[group + '-AVG', group + '-STD']])
    trans1 = Affine2D().translate(-0.25 * shift, 0.0) + ax.transData
    ax.errorbar(sub_df.index, sub_df[group + '-AVG'], yerr=sub_df[group + '-STD'], transform=trans1, color=color, label=label)


errorbar_by_group('EL1939', 'g', 3, 'Control - EL1939 (0% FEC)')
errorbar_by_group('EL1986/350uL', 'r', 0, 'EL1986 (0.5% FEC)')
errorbar_by_group('EL1986 / 420uL', 'grey', 1, 'EL1987 (2% FEC)')
errorbar_by_group('EL1986 / 600uL', 'b', 2, 'EL1988 (5% FEC)')

plt.legend()
plt.xlabel('Cycle')
plt.ylabel('Capacity Retention [%]')
plt.yticks(np.arange(80, 101, 2.5))
plt.title("Experiment ID-2743: Capacity Retention By Cycle")
plt.show()

df2 = pd.read_csv('Viz_6b_error_bar.csv')
trans2 = Affine2D().translate(0.0, -0.25 * 3) + ax.transData
ax1 = df2.plot(kind='scatter', x='Cycle', y='EL1939 CD / Control', color='g', label='Control - EL1939 (0% FEC)', alpha=0.5)
ax2 = df2.plot(kind='scatter', x='Cycle', y='EL1986/350uL', color='r', ax=ax1, label='EL1986 (0.5% FEC)', alpha=0.5)
ax3 = df2.plot(kind='scatter', x='Cycle', y='EL1986 / 420uL', color='grey', ax=ax1, label='EL1987 (2% FEC)', alpha=0.5)
ax4 = df2.plot(kind='scatter', x='Cycle', y='EL1986 / 600uL', color='b', ax=ax1, label='EL1988 (5% FEC)', alpha=0.5)

plt.xlabel('Cycle')
plt.ylabel('Cell Count')
plt.legend()
plt.title("Experiment ID-2743: Cell Count By Cycle")
plt.show()
