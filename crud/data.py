import pandas as pd

# Load the dataset
df = pd.read_csv("news_data.csv")

# Check for missing or null values
print(df.isnull().sum())

# Drop or fill missing values
df = df.dropna()  # Alternatively, use df.fillna('') to fill with empty strings

