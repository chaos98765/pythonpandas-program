
import pandas as pd

# Create a DataFrame with 10 student records
data = {
    'Name': ['Rahul', 'Priya', 'Amit', 'Sneha', 'Rohit',
             'Neha', 'Karan', 'Pooja', 'Vikash', 'Anjali'],
    'Age': [20, 21, 19, 22, 20, 21, 23, 19, 22, 20],
    'City': ['Kolkata', 'Delhi', 'Mumbai', 'Chennai', 'Pune',
             'Kolkata', 'Delhi', 'Mumbai', 'Pune', 'Chennai'],
    'Marks': [85, 92, 78, 88, 95, 81, 76, 89, 84, 91]
}

# Create the DataFrame
df = pd.DataFrame(data)

# Display the complete DataFrame
print("Complete DataFrame:")
print(df)

# Display the top 3 records
print("\nTop 3 Records:")
print(df.head(3))

# Display the bottom 3 records
print("\nBottom 3 Records:")
print(df.tail(3))
