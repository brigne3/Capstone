import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

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

# Apply ordinal encoding to 'Neighborhood' column
neighborhood_mapping = {'Rural': 1, 'Suburb': 2, 'Urban': 3}
df['Neighborhood'] = df['Neighborhood'].map(neighborhood_mapping)

# Designate the variables
X = df[['Bedrooms', 'Bathrooms', 'SquareFeet', 'Neighborhood', 'YearBuilt']]
y = df['Price']

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=17)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
price_prediction = model.predict(X_test)

bedroom_multiplier = round(model.coef_[0], 2)
bathroom_multiplier = round(model.coef_[1], 2)
sf_multiplier = round(model.coef_[2], 2)
neighborhood_multiplier = round(model.coef_[3], 2)
buildyear_multiplier = round(model.coef_[4], 2)

r2 = r2_score(y_test, price_prediction)
# Uncomment to print the r2 score
# print(f'R2 Score of model: {r2}')

while True:
    print("Enter home data for an estimate. Press -1 on any answer to exit")

    user_bedrooms = input("Number of bedrooms (between 2 and 5): ")
    if user_bedrooms == "-1":
        print("Exiting program")
        break

    user_bathrooms = input("Number of bathrooms (between 1 and 3): ")
    if user_bathrooms == "-1":
        print("Exiting program")
        break

    try:
        user_bathrooms_int = int(user_bedrooms)
    except ValueError:
        print("Invalid entry")
        continue

    user_sf = input("Home square footage (between 1000 and 2999): ")
    if user_sf == "-1":
        print("Exiting program")
        break

    user_neighborhood = input("Neighborhood type (1 for Rural, 2 for Suburb, 3 for Urban): ")
    if user_neighborhood == "-1":
        print("Exiting program")
        break

    user_buildyear = input("Year built (between 1950 and 2021): ")
    if user_buildyear == "-1":
        print("Exiting program")
        break

    try:
        user_bedrooms_int = int(user_bedrooms)
        user_bathrooms_int = int(user_bathrooms)
        user_sf_int = int(user_sf)
        user_neighborhood_int = int(user_neighborhood)
        user_buildyear_int = int(user_buildyear)

    except ValueError:
        print("Invalid entry for one of the inputs. Please enter valid integers.")
        continue

    if user_bedrooms_int < 2 or user_bedrooms_int > 5:
        print("Invalid entry. Bedrooms must be between 2 and 5")
        continue

    if user_bathrooms_int < 1 or user_bathrooms_int > 3:
        print("Invalid entry. Bedrooms must be between 1 and 3")
        continue

    if user_sf_int > 2999 or user_sf_int < 1000:
        print("Invalid entry. Square footage must be between 1000 and 2999.")
        continue

    if user_neighborhood_int < 1 or user_neighborhood_int > 3:
        print("Invalid entry. Neighborhood entry must be 1, 2, oe 3.")
        continue

    if user_buildyear_int > 2021 or user_buildyear_int < 1950:
        print("Invalid entry. Build year must be between 1950 and 2021.")
        continue

    model_beds = user_bedrooms_int
    model_baths = user_bathrooms_int
    model_sf = user_sf_int
    model_neighborhood = user_neighborhood_int
    model_year = user_buildyear_int

    estimate = round(((model_beds * bedroom_multiplier) + (model_baths * bathroom_multiplier) + (model_sf * sf_multiplier)
                + (model_neighborhood * neighborhood_multiplier) + (model_year * buildyear_multiplier)))

    currency_estimate = "{:,}".format(estimate)

    print("Price estimate: $" + str(currency_estimate))
