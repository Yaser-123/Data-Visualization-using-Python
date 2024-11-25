import pandas as pd
import numpy as np

# Sample dataset
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Edward'],
    'Age': [25, np.nan, 35, 29, 200],  # 200 is an outlier
    'Score': [85, 90, 78, np.nan, 85]
}
df = pd.DataFrame(data)

# Display original data
print("Original Data:")
print(df)

# 1. Handle missing values
df['Age'].fillna(df['Age'].median(), inplace=True)  # Replace missing Age with median
df['Score'].fillna(df['Score'].mean(), inplace=True)  # Replace missing Score with mean

# 2. Handle duplicate records
df.drop_duplicates(inplace=True)

# 3. Handle outliers (Assume Age > 120 is an outlier)
df.loc[df['Age'] > 120, 'Age'] = df['Age'].median()  # Replace outlier with median

# Display cleaned data
print("\nCleaned Data:")
print(df)
