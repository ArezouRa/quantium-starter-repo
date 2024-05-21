import pandas as pd
import os

data_directory = "./data"
output_file = "./formatted_data.csv"

# Create an empty DataFrame to store the combined data
combined_data = pd.DataFrame(columns=["sales", "date", "region"])

# Iterate through all files in the data directory
for file_name in os.listdir(data_directory):
    file_path = os.path.join(data_directory, file_name)
    # Read the CSV file into a DataFrame
    content = pd.read_csv(file_path)

    # Filter rows where product is "pink morsel" using .loc
    pink_morsel_data = content.loc[
        content["product"] == "pink morsel"
    ].copy()  # Use .copy() to avoid modifying the original DataFrame

    # Process the filtered data and calculate sales
    pink_morsel_data["price"] = pink_morsel_data
    ["price"].str[1:].astype(float)
    pink_morsel_data["sales"] = pink_morsel_data
    ["price"] * pink_morsel_data["quantity"]

    # Keep only relevant columns
    pink_morsel_data = pink_morsel_data.loc[:, ["sales", "date", "region"]]
    # [:  indicates that we want to select all rows

    # Append filtered data to the combined DataFrame
    # excluding empty or all-NA columns
    combined_data = combined_data._append(
        pink_morsel_data.dropna(), ignore_index=True)


# Sort the combined DataFrame by date in ascending order (ASC)
combined_data = combined_data.sort_values(by="date", ascending=True)

# Write the sorted DataFrame to the output CSV file
combined_data.to_csv(output_file, index=False)
