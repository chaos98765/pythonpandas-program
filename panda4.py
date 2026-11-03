import pandas as pd

# Create a DataFrame containing exactly 10 records
data = {
    'Roll_No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Name': ['Rahul', 'Amit', 'Suman', 'Priya', 'Rohan',
             'Sneha', 'Arjun', 'Neha', 'Karan', 'Ankit'],
    'Age': [20, 21, 19, 20, 22, 21, 20, 19, 22, 21]
}

df = pd.DataFrame(data)

# Print the complete DataFrame
print("Original DataFrame:")
print(df)

# Print the middle 3 records (5th, 6th and 7th)
print("\nMiddle 3 Records:")
print(df.iloc[4:7])