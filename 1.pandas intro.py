# Import Pandas
import pandas as pd

# Create a Series
marks = pd.Series([85, 90, 78, 92])

print("Series:")
print(marks)

# Create a DataFrame
student_data = {
    "Name": ["Raja", "Arun", "Priya", "Kavin"],
    "Age": [21, 22, 20, 23],
    "Marks": [85, 90, 78, 92]
}

df = pd.DataFrame(student_data)

print("\nDataFrame:")
print(df)

print("\nShape:", df.shape)
print("\nColumns:", df.columns)
print("\nData Types:")
print(df.dtypes)