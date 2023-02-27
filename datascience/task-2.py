# Check for duplicates in the dataset and remove them if necessary.
import pandas as pd

# Load the dataset
df = pd.read_csv('dataset.csv')

# TODO: Input code here

# Save the cleaned dataset
df.to_csv('cleaned_dataset.csv', index=False)
