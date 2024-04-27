# What is before step one?
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("laptops.csv")
print(df.describe)
print(df.info)
# Step 1: Data Loading and Initial Exploration





# Step 2: Data Cleaning
# Check for null values before cleaning
print("\nNull values before cleaning:")
print(df.isnull().sum())


# Handle missing values
# If column is a number, replace with average value of that column
# If column is not a number, drop the data
# You will need to use a for loop
df.dropna(inplace=True)
for col in df.columns:
    if df[col].dtype == "float64" or df[col].dtype == "int64":
        df[col].fillna(df[col].mean(), inplace=True)
    elif df[col].dtype == "object":
        df.dropna(subset=[col])





# Confirm that missing values are handled
print(df.info())
print("\nData types and missing values after handling missing values:")



# Step 3: Data Filtering and Selection
# Question 1: What is the average price of laptops based on different companies?
print("\nAverage price of laptops based on different companies:")
average_price_each_comps = df.groupby("Company")["Price"].mean()
print(average_price_each_comps)



# Question 2: How does the price distribution vary between laptops with SSD and HDD?
print("\nPrice distribution for laptops with SSD and HDD:")
ssd_price = df[df["Memory"].str.contains("SSD", case=False)]["Price"]
hdd_price = df[df["Memory"].str.contains("HDD", case=False)]["Price"]

print("Average SSD price:", ssd_price.mean())
print("Average HDD price:", hdd_price.mean())


# Question 3: Which company has the highest average RAM capacity?
df['Ram'] = df['Ram'].str.extract('(\d+)').astype(float)  # Clean RAM column
average_ram_each_comps = df.groupby("Company")["Ram"].mean()
print("The highest average ram capacity companies:", average_ram_each_comps.max())



# Question 4: How does the weight of laptops vary across different screen resolutions?
df['Weight'] = df['Weight'].str.extract('(\d+\.\d+)').astype(float)  # Clean Weight column
weight_by_resolution = df.groupby("ScreenResolution")["Weight"].mean()
print("weight by resolution:", weight_by_resolution)



# Step 5: Plotting
# Plot questions 1-4 in a 2x2 subplot
fig, ax = plt.subplots(2, 2, figsize=(19,10))

ax[0, 0].bar(average_price_each_comps.index, average_price_each_comps.values)
ax[0, 0].set_title("Average price by each company")
ax[0, 0].set_xlabel("Company")
ax[0, 0].set_ylabel("Average price")
ax[0, 0].tick_params(axis="x", rotation=90)

ax[0, 1].hist([ssd_price, hdd_price], bins=10, label=["SSD", "HDD"])
ax[0, 1].set_title("Average price by HDD and SSD")
ax[0, 1].set_xlabel("SSD and HDD")
ax[0, 1].set_ylabel("Average storage")
ax[0, 1].legend()

ax[1, 0].bar(average_ram_each_comps.index, average_ram_each_comps.values)
ax[1, 0].set_title("Average ram by each company")
ax[1, 0].set_xlabel("Company")
ax[1, 0].set_ylabel("Average ram")
ax[1, 0].tick_params(axis="x", rotation=90)

ax[1, 1].bar(weight_by_resolution.index, weight_by_resolution.values)
ax[1, 1].set_title("Average weight by screen resolution")
ax[1, 1].set_xlabel("resolution")
ax[1, 1].set_ylabel("weight")
ax[1, 1].tick_params(axis="x", rotation=90)

# Show plot
plt.tight_layout()
plt.show()