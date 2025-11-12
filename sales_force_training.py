# sales_force_training.py

# ================================
# CASE STUDY 01: SALES FORCE TRAINING
# ================================

import pandas as pd
import numpy as np
from scipy import stats

# --------------------------------
# 1. Membuat DataFrame
# --------------------------------
data = [100, 150, 50, 100, 130, 120, 100, 85, 70, 150,
        150, 120, 50, 100, 100, 140, 90, 150, 50, 90,
        120, 100, 110, 75, 65]

df = pd.DataFrame(data, columns=['TransactionAmount'])
print("DataFrame:\n", df.head(), "\n")

# --------------------------------
# 2. Measure of Central Tendency
# --------------------------------
mean = df['TransactionAmount'].mean()
median = df['TransactionAmount'].median()
mode = df['TransactionAmount'].mode()[0]

print("=== Measure of Central Tendency ===")
print(f"Mean   : {mean}")
print(f"Median : {median}")
print(f"Mode   : {mode}\n")

# --------------------------------
# 3. Measure of Variability
# --------------------------------
std_dev = df['TransactionAmount'].std()
variance = df['TransactionAmount'].var()
data_range = df['TransactionAmount'].max() - df['TransactionAmount'].min()

print("=== Measure of Variability ===")
print(f"Standard Deviation : {std_dev}")
print(f"Variance           : {variance}")
print(f"Range              : {data_range}\n")

# --------------------------------
# 4. Hipotesis
# --------------------------------
# H0 : Tidak ada peningkatan rata-rata transaksi setelah training (μ = 100)
# H1 : Ada peningkatan rata-rata transaksi setelah training (μ > 100)

mu = 100  # rata-rata sebelum training

# --------------------------------
# 5. One Sample T-Test
# --------------------------------
t_stat, p_value = stats.ttest_1samp(df['TransactionAmount'], mu)

# karena kita ingin menguji peningkatan (one-tailed test):
p_value_one_tailed = p_value / 2

print("=== One Sample T-Test ===")
print(f"T-statistic : {t_stat}")
print(f"P-value (one-tailed) : {p_value_one_tailed}\n")

# --------------------------------
# 6. Kesimpulan
# --------------------------------
alpha = 0.05

if (t_stat > 0) and (p_value_one_tailed < alpha):
    conclusion = "Tolak H0 → Ada peningkatan signifikan setelah training."
else:
    conclusion = "Gagal menolak H0 → Tidak ada peningkatan signifikan setelah training."

print("=== Kesimpulan ===")
print(conclusion)

