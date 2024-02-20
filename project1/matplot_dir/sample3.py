import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data from the CSV file
df = pd.read_csv('name_height.csv')

# Extract the 'Age' column
ages = df['Age']

# Calculate mean, median, and mode
mean_age = np.mean(ages)
median_age = np.median(ages)
mode_age = ages.mode().values[0]

# Print the results
print(f"Mean Age: {mean_age}")
print(f"Median Age: {median_age}")
print(f"Mode Age: {mode_age}")

# Create a histogram for the Age data
plt.hist(ages, bins=10, edgecolor='black', alpha=0.7)
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age Distribution')
plt.savefig('/home/user/PycharmProjects/project1/plots/plot2.png')
plt.show()
