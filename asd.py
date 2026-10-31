import pandas as pd

# Create a DataFrame containing student records
data = {
    'Student_ID': [101, 102, 103, 104, 102, 105, 103],
    'Name': ['Rahul', 'Priya', 'Amit', 'Neha', 'Priya', 'Riya', 'Amit'],
    'Age': [20, 21, 22, 20, 21, 23, 22],
    'Marks': [85, 90, 78, 88, 90, 95, 78]
}

df = pd.DataFrame(data)

# Display original DataFrame
print("Original Student Records:")
print(df)

# Identify all duplicate rows
duplicates = df[df.duplicated(keep=False)]

# Display duplicate records
print("\nDuplicate Records:")
print(duplicates)