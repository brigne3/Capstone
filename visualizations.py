import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read the csv
df = pd.read_csv("housing_price_dataset.csv")

# Convert 'YearBuilt' column to datetime format
df['YearBuilt'] = pd.to_datetime(df['YearBuilt'], format='%Y').dt.year

# Convert 'Price' column to int64
df['Price'] = df['Price'].astype(np.int64)
# Remove rows with negative prices
df = df[df['Price'] >= 0]

# Convert 'SquareFeet', 'Bedrooms', and 'Bathrooms' to int32
df['Bedrooms'] = df['Bedrooms'].astype(np.int32)
df['Bathrooms'] = df['Bathrooms'].astype(np.int32)
df['SquareFeet'] = df['SquareFeet'].astype(np.int32)

mean_price_by_neighborhood = df.groupby('Neighborhood')['Price'].mean().astype(np.int32)
mean_price_by_bedrooms = df.groupby('Bedrooms')['Price'].mean().astype(np.int32)
mean_price_by_bathrooms = df.groupby('Bathrooms')['Price'].mean().astype(np.int32)

# Create subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

sns.barplot(x=mean_price_by_neighborhood.index, y=mean_price_by_neighborhood.values, ax=axes[0, 0])
axes[0, 0].set_title('Mean Price by Neighborhood')
axes[0, 0].set_xlabel('Neighborhood')
axes[0, 0].set_ylabel('Mean Price')
axes[0, 0].set_ylim(min(mean_price_by_neighborhood.values) - 5000, max(mean_price_by_neighborhood.values) + 5000)

sns.barplot(x=mean_price_by_bedrooms.index, y=mean_price_by_bedrooms.values, ax=axes[0, 1])
axes[0, 1].set_title('Mean Price by Bedrooms')
axes[0, 1].set_xlabel('Number of Bedrooms')
axes[0, 1].set_ylabel('Mean Price')
axes[0, 1].set_ylim(min(mean_price_by_bedrooms.values) - 5000, max(mean_price_by_bedrooms.values) + 5000)

sns.barplot(x=mean_price_by_bathrooms.index, y=mean_price_by_bathrooms.values, ax=axes[1, 0])
axes[1, 0].set_title('Mean Price by Bathrooms')
axes[1, 0].set_xlabel('Number of Bathrooms')
axes[1, 0].set_ylabel('Mean Price')
axes[1, 0].set_ylim(min(mean_price_by_bathrooms.values) - 5000, max(mean_price_by_bathrooms.values) + 5000)

sns.regplot(x='SquareFeet', y='Price', data=df, ax=axes[1, 1], scatter_kws={'s': 5, 'alpha': 0.5})
axes[1, 1].set_title('Linear Regression: Price vs Square Feet')

plt.tight_layout()
plt.show()
