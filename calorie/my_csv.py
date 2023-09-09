import pandas as pd

# Read the first CSV file
menu_df = pd.read_csv('menu.csv')

# Read the second CSV file
topping_df = pd.read_csv('output.csv')

# Merge the two dataframes based on a common column (Menu Name in this case)
combined_df = menu_df.merge(topping_df, on='Menu Name', how='left')

# Save the merged dataframe to a new CSV file
combined_df.to_csv('combined_menu.csv', index=False)

print("Combined CSV file 'combined_menu.csv' has been created.")
