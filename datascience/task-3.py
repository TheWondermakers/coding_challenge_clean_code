# Convert the Date column to a datetime format.
import pandas as pd


# Load the dataset
df = pd.read_csv('dataset.csv')


# TODO: input your code here


# Save the updated dataset
df.to_csv('updated_dataset.csv', index=False)
