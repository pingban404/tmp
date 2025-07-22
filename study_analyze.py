import pandas as pd
import numpy as np

df = pd.read_csv("./business-financial-data-march-2025-quarter-csv.csv")
print("Period列的数据:")
print(df['Period'])

print(f"\n原始数据行数: {len(df)}")
print(f"Period列唯一值数量: {df['Period'].nunique()}")

# 方法1: 基于Period列去重，保留第一次出现的记录
df_dedup_first = df.drop_duplicates(subset=['Period'], keep='first')
print(f"\n去重后数据行数 (保留第一次): {len(df_dedup_first)}")

# 方法2: 基于Period列去重，保留最后一次出现的记录
df_dedup_last = df.drop_duplicates(subset=['Period'], keep='last')
print(f"去重后数据行数 (保留最后一次): {len(df_dedup_last)}")

# 方法3: 基于Period列去重，删除所有重复的记录
df_dedup_none = df.drop_duplicates(subset=['Period'], keep=False)
print(f"去重后数据行数 (删除所有重复): {len(df_dedup_none)}")

# 查看去重后的Period列
print("\n去重后的Period列 (保留第一次):")
print(df_dedup_first['Period'].sort_values())

# 保存去重后的数据
df_dedup_first.to_csv("./df_dedup_first.csv", index=False, encoding='utf-8-sig')
print(f"\n去重后的数据已保存到 df_dedup_first.csv")

# 查看重复的Period值
duplicates = df[df.duplicated(subset=['Period'], keep=False)]
print(f"\n重复的Period值数量: {len(duplicates)}")
if len(duplicates) > 0:
    print("重复的Period值:")
    print(duplicates['Period'].value_counts().head(10))