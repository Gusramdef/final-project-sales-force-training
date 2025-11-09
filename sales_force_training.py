#Membuat DataFrame ‘TransactionAmount’

import pandas as pd

data = [100, 150, 50, 100, 130, 120, 100, 85, 70, 150,
        150, 120, 50, 100, 100, 140, 90, 150, 50, 90,
        120, 100, 110, 75, 65]

df = pd.DataFrame(data, columns=['TransactionAmount'])

#Measure of Central Tendency

mean = df['TransactionAmount'].mean()
median = df['TransactionAmount'].median()
mode = df['TransactionAmount'].mode()[0]

print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")

#Measure of Variability

std_dev = df['TransactionAmount'].std()
variance = df['TransactionAmount'].var()
range_val = df['TransactionAmount'].max() - df['TransactionAmount'].min()

print(f"Standard Deviation: {std_dev}")
print(f"Variance: {variance}")
print(f"Range: {range_val}")
