# Create a new column for the total transaction amount by 
# multiplying Quantity and Price columns.
import pandas as pd


# Load the dataset
df = pd.read_csv('dataset.csv')


# TODO: Input your code here


# Save the updated dataset
df.to_csv('updated_dataset.csv', index=False)
