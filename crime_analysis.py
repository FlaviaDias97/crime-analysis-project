import requests
import pandas as pd
import matplotlib.pyplot as plt


# Get crime data
url = "https://data.police.uk/api/crimes-street/all-crime?lat=53.8008&lng=-1.5491"

response = requests.get(url)
data = response.json()


# Convert data into a dataframe
df = pd.DataFrame(data)


# View the first few rows and columns
print(df.head())
print(df.columns)


# Analyse crime categories
crime_counts = df["category"].value_counts()

print(crime_counts)


# Create a bar chart
crime_counts.head(10).plot(kind="bar")

plt.title("Top 10 Crime Categories")
plt.xlabel("Crime Type")
plt.ylabel("Number of Crimes")


# Save outputs
df.to_csv("Data/crime_data.csv", index=False)

plt.savefig("outputs/top_crime_categories.png")


# Display chart
# plt.show()

print(df["location"].head())

location_counts = df["location"].value_counts()

print(location_counts.head(10))

print(df["month"].value_counts())

location_counts.head(10).plot(kind="bar")

plt.title("Top 10 Crime Locations")
plt.xlabel("Location")
plt.ylabel("Number of Crimes")

plt.savefig("outputs/top_crime_locations.png")

plt.show()

print(df["month"].value_counts())

