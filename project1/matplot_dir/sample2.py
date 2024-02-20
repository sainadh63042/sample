import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('name_height.csv')

heights = df['Height']


mean_height = np.mean(heights)
median_height = np.median(heights)
mode_height = heights.mode().values[0]


plt.hist(heights, bins=8, edgecolor='black')
plt.xlabel('Height')
plt.ylabel('Frequency')

plt.axvline(mean_height, color='red', linestyle='dashed', linewidth=2, label=f"Mean: {mean_height:.2f}")
plt.axvline(median_height, color='green', linestyle='dashed', linewidth=2, label=f"Median: {median_height}")
plt.axvline(mode_height, color='blue', linestyle='dashed', linewidth=2, label=f"Mode: {mode_height}")
plt.legend()
plt.savefig('/home/user/PycharmProjects/project1/plots/plot1.png')
# plt.show()

