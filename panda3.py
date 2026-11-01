
import pandas as pd
import numpy as np

# Step 1: Create a DataFrame with 10 records
data = {
    'Name': ['Rahul', 'Priya', 'Amit', 'Sneha', None,
             'Rahul', 'Karan', 'Neha', 'Amit', 'Priya'],

    'Age': [21, 22, np.nan, 24, 23,
            21, np.nan, 25, 23, 22],

    'City': ['Kolkata', 'Delhi', 'Mumbai', None, 'Pune',
             'Kolkata', 'Chennai', 'Delhi', 'Mumbai', 'Delhi'],

    'Marks': [85, 90, 78, np.nan, 88,
              85, 92, 95, 78, 90]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Step 2: Identify missing values
print("\nMissing Values:")
print(df.isnull())

print("\nTotal Missing Values in Each Column:")
print(df.isnull().sum())

# Step 3: Fill missing numeric values with column mean
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Marks'] = df['Marks'].fillna(df['Marks'].mean())

# Step 4: Fill missing text values with 'Unknown'
df['Name'] = df['Name'].fillna('Unknown')
df['City'] = df['City'].fillna('Unknown')

print("\nDataFrame After Filling Missing Values:")
print(df)

# Step 5: Check whether duplicate records exist
print("\nAre Duplicate Records Present?")
print(df.duplicated().any())

# Step 6: Display duplicate records
print("\nDuplicate Records:")
print(df[df.duplicated()])
